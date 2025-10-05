#!/bin/bash
# List all markdown files excluding README*, sort by timestamp, and rename with prefix numbering

# Collect files with timestamps using stat
files=$(for f in *.md; do
    [[ "$f" =~ ^[Rr][Ee][Aa][Dd][Mm][Ee]\.md$ ]] && continue
    ts=$(stat -f "%m" "$f")   # modification time (epoch)
    echo "$ts $f"
done | sort -n | awk '{print $2}')

count=1
for f in $files; do
    newname="$(printf "%d. %s" "$count" "$f")"
    mv "$f" "$newname"
    echo "Renamed: $f -> $newname"
    count=$((count + 1))
done

