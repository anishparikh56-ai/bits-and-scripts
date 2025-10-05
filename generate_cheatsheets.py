#!/usr/bin/env python3
"""
Generate concise, interview-ready cheat sheets for a list of commands
in both Markdown and HTML formats using OpenAI's GPT-4o via the Responses API.
One .md and one .html file per command.

Only generates missing files — skips commands if both files already exist.

Usage:
  python generate_cheatsheets.py \
      --input {linux|windows}_commands.txt \
      --outdir cheatsheets \
      --model gpt-4o \
      --platform Linux \
      --max-workers 4

Env:
  OPENAI_API_KEY must be set.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import os
import re
from pathlib import Path
from typing import List

from openai import OpenAI, APIError, APIConnectionError, RateLimitError
from bs4 import BeautifulSoup

PROMPT_TEMPLATE = (
    """Explain the {platform} command `{command}` in a clear, concise way. Skip the full man page format and focus on the most useful options. Provide:

A short description of the command.

A table of the most common options with explanations.

Realistic usage examples for everyday tasks.

A compact cheat sheet in a few lines for quick reference.
"""
)

MARKDOWN_INSTRUCTIONS = (
    "You are a concise {platform} expert. Output valid, well-formatted Markdown only, using proper headings, tables, and fenced code blocks."
)

HTML_INSTRUCTIONS = (
    "You are a concise {platform} expert. Output valid, indented HTML only, with semantic tags (h1, h2, table, code, pre). Do not include extra explanations or markdown code fences."
)

def load_commands(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"Command list not found: {path}")
    cmds: List[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        cmds.append(line)
    if not cmds:
        raise ValueError("No commands found in the input file.")
    return cmds

def filename_for_command(cmd: str, ext: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", cmd.strip())
    safe = safe.strip("-._") or "command"
    return f"{safe}.{ext}"

def build_prompt(cmd: str, platform: str) -> str:
    return PROMPT_TEMPLATE.format(command=cmd, platform=platform)

def call_gpt(client: OpenAI, model: str, prompt: str, instructions: str) -> str:
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=prompt,
    )
    return response.output_text

def beautify_html(html: str) -> str:
    html = re.sub(r"^```html\s*|```$", "", html.strip(), flags=re.MULTILINE)
    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify()

def beautify_markdown(md: str) -> str:
    lines = [line.rstrip() for line in md.splitlines()]
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"

def generate_one(client: OpenAI, model: str, cmd: str, outdir: Path, platform: str, retries: int = 2) -> List[Path]:
    md_path = outdir / filename_for_command(cmd, "md")
    html_path = outdir / filename_for_command(cmd, "html")

    if md_path.exists() and html_path.exists():
        print(f"⏩ Skipping {cmd} (both files exist)")
        return [md_path, html_path]

    prompt = build_prompt(cmd, platform)
    attempt = 0
    last_exc: Exception | None = None
    while attempt <= retries:
        try:
            if not md_path.exists():
                md = call_gpt(client, model, prompt, MARKDOWN_INSTRUCTIONS.format(platform=platform))
                md = beautify_markdown(md)
                md_path.write_text(md, encoding="utf-8")
            if not html_path.exists():
                html = call_gpt(client, model, prompt, HTML_INSTRUCTIONS.format(platform=platform))
                html = beautify_html(html)
                html_path.write_text(html, encoding="utf-8")
            return [md_path, html_path]
        except (RateLimitError, APIConnectionError, APIError) as e:
            last_exc = e
            attempt += 1

    if not md_path.exists():
        md_path.write_text(f"# {cmd}\n\nGeneration failed after retries: {last_exc}", encoding="utf-8")
    if not html_path.exists():
        html_path.write_text(f"<h1>{cmd}</h1><p>Generation failed after retries: {last_exc}</p>", encoding="utf-8")
    return [md_path, html_path]

def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", "-i", type=Path, default=Path("commands.txt"))
    p.add_argument("--outdir", "-o", type=Path, default=Path("cheatsheets"))
    p.add_argument("--model", "-m", default="gpt-4o")
    p.add_argument("--platform", type=str, default="Linux", choices=["Linux", "Windows"])
    p.add_argument("--max-workers", "-w", type=int, default=os.cpu_count() or 4)
    p.add_argument("--retries", type=int, default=2)
    args = p.parse_args(argv)

    args.outdir.mkdir(parents=True, exist_ok=True)

    client = OpenAI()

    commands = load_commands(args.input)
    print(f"Generating {len(commands)} Markdown & HTML cheat sheets for {args.platform} to {args.outdir.resolve()} using {args.model}...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        futures = [
            pool.submit(generate_one, client, args.model, cmd, args.outdir, args.platform, args.retries)
            for cmd in commands
        ]
        for fut in concurrent.futures.as_completed(futures):
            paths = fut.result()
            for path in paths:
                print(f"✔ Wrote {path.name}")

    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
