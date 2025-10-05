#!/usr/bin/env python3
import os
import re

# Regex pattern to match most emojis
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U00002700-\U000027BF"  # Dingbats
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U00002600-\U000026FF"  # Misc symbols
    "\U00002B00-\U00002BFF"  # Misc symbols and arrows
    "]+",
    flags=re.UNICODE
)

def strip_emojis(text: str) -> str:
    """Remove all emojis from a given string."""
    return emoji_pattern.sub(r'', text)

def process_files(root="."):
    total_files = 0
    modified_files = 0

    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_files += 1
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                cleaned = strip_emojis(content)
                if content != cleaned:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(cleaned)
                    modified_files += 1
                    print(f" Stripped emojis from: {filepath}")
            except UnicodeDecodeError:
                print(f"⏭️ Skipping binary file: {filepath}")
            except Exception as e:
                print(f"️ Error processing {filepath}: {e}")

    print("\n Summary:")
    print(f"   Total files scanned:   {total_files}")
    print(f"   Files modified:        {modified_files}")

if __name__ == "__main__":
    process_files(".")
