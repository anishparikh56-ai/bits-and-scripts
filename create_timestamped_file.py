### This script was to create a timestamped file with a header for personal journaling purposes.
import os
from datetime import datetime

def get_ordinal(n):
    if 11 <= n <= 13:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')

now = datetime.now()
day = now.day
ordinal = get_ordinal(day)

filename_date = now.strftime(f"%B {day}{ordinal}, %Y")
filename = f"{filename_date}.txt"

header_time = now.strftime(f"%B {day}{ordinal}, %Y %-I:%M %p")
header = header_time[:-2] + header_time[-2:].lower()  # am/pm lowercase

if not os.path.exists(filename):
    # File doesn't exist, create and write header
    with open(filename, "w") as file:
        file.write(header + "\n")
    print(f"Created file '{filename}' with header:\n{header}")
else:
    # File exists, append header
    with open(filename, "a") as file:
        file.write(header + "\n")
    print(f"Appended header to existing file '{filename}':\n{header}")
