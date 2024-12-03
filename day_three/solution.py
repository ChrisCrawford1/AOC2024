import re


def _read_instructions_from_file() -> str:
    try:
        file = open("./day_three/instructions.txt", "r")
        allLines = file.readlines()

        return "".join(allLines)
    except:
        print("Error parsing text file, try again")
        quit()


def get_valid_instructions() -> list[tuple[str, str]]:
    # This pattern will only identify valid mul instructions
    # in the format of mul(x, y)
    pattern = r'mul\((\d{1,3}),\s*(\d{1,3})\)'

    raw_instructions = _read_instructions_from_file()
    matches = re.findall(pattern, raw_instructions)

    return matches


def calculate_total_value() -> int:
    valid_instructions = get_valid_instructions()

    total = 0
    for instruction in valid_instructions:
        a, b = map(int, instruction)
        total += a * b

    return total


total = calculate_total_value()
print("Total value is {}".format(total))
