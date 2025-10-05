import markdown
import os
import re

def clean_markdown(content):
    # Remove YAML frontmatter only
    return re.sub(r"^---[\s\S]*?---\n", "", content, flags=re.MULTILINE).strip()


def markdown_to_html(md_path, output_html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    cleaned_md = clean_markdown(raw_md)
    html_body = markdown.markdown(cleaned_md, extensions=['fenced_code', 'tables'])

    html_template = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; padding: 2em; line-height: 1.6; }}
            h1, h2, h3 {{ color: #222; }}
            code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; }}
            pre {{ background: #f0f0f0; padding: 10px; overflow-x: auto; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            a {{ color: #0366d6; text-decoration: none; }}
        </style>
        <title>Writeup</title>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"✅ Converted {md_path} → {output_html_path}")

def convert_all_index_md():
    base_dir = os.getcwd()
    for root, dirs, files in os.walk(base_dir):
        if 'index.md' in files:
            dir_name = os.path.basename(root)
            md_path = os.path.join(root, 'index.md')
            output_html = os.path.join(base_dir, f"{dir_name}.html")
            markdown_to_html(md_path, output_html)

if __name__ == "__main__":
    convert_all_index_md()

