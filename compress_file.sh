#!/bin/bash

# Check if input file or directory is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <input_file_or_directory>"
  exit 1
fi

input="$1"

# Check if input is a directory
if [ -d "$input" ]; then
  echo "Processing all files in directory: $input"
  
  # Loop through all files recursively in the directory
  for file in $(find "$input" -type f); do
    echo "Processing: $file"
    
    # Skip files that already have "_out" in their name
    if [[ "$file" =~ _out\. ]]; then
      echo "Skipping already processed file: $file"
      continue
    fi
    
    # Input file and output file
    output_file="${file%.*}_out.${file##*.}"
    
    # Compress the video using ffmpeg
    ffmpeg -i "$file" -vcodec libx264 -preset fast -crf 28 "$output_file"
    
    # Check if the compression was successful
    if [ $? -eq 0 ]; then
      echo "Compression successful: $output_file"
    else
      echo "Compression failed for: $file"
    fi
  done
  
elif [ -f "$input" ]; then
  echo "Processing single file: $input"
  
  # Input file and output file
  output_file="${input%.*}_out.${input##*.}"
  
  # Compress the video using ffmpeg
  ffmpeg -i "$input" -vcodec libx264 -preset fast -crf 28 "$output_file"
  
  # Check if the compression was successful
  if [ $? -eq 0 ]; then
    echo "Compression successful: $output_file"
  else
    echo "Compression failed!"
  fi
  
else
  echo "Error: '$input' is neither a file nor a directory!"
  exit 1
fi
