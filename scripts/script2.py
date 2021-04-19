from braille import charDict
for key, value in charDict.items():
    print(
        f"({tuple(value[0])},\n"
        f" {tuple(value[1])},\n"
        f" {tuple(value[2])}): \"{key}\","
    )