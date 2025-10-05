import os

# Roman numeral to decimal mapping
roman_to_decimal = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
    "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
    "XXI": 21
}

# Loop through all files in the current directory
for filename in os.listdir('.'):
    if not os.path.isfile(filename):
        continue

    if '.' not in filename:
        continue

    parts = filename.split('.', 1)
    roman = parts[0].strip()
    rest = parts[1].strip()

    if roman in roman_to_decimal:
        number = roman_to_decimal[roman]
        new_name = f"{number}. {rest}"
        if filename != new_name:
            print(f"Renaming: '{filename}' -> '{new_name}'")
            os.rename(filename, new_name)

