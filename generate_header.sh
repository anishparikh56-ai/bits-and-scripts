#!/bin/bash

# List of topics (use underscore _ instead of spaces)
topics=(
	### Topics
)

# Path to the markdown generator script
GEN_SCRIPT="./header.sh"

# Check if the generator script exists
if [ ! -x "$GEN_SCRIPT" ]; then
  echo "Error: $GEN_SCRIPT not found or not executable."
  exit 1
fi

# Loop through topics and generate markdowns
for topic in "${topics[@]}"; do
  echo "▶ Generating markdown for: $topic"
  "$GEN_SCRIPT" "$topic"
done

