with open("input.txt", "r", encoding="utf-8") as file:
    instructions = file.readlines()

pos = 50
counter = 0
SIZE = 100

for instruction in instructions:
    instruction = instruction.strip()
    if not instruction:
        continue

    direction = instruction[0].upper()
    value = int(instruction[1:])

    full_rotations = value // SIZE
    remainder = value % SIZE

    counter += full_rotations

    if direction == "R":
        if pos + remainder >= SIZE and pos != 0:
            counter += 1
        pos = (pos + remainder) % SIZE

    elif direction == "L":
        if pos - remainder <= 0 and pos != 0:
            counter += 1
        pos = (pos - remainder) % SIZE


    print(f"instruction : {instruction}\n"
          f"pos {pos}\n"
          f"counter {counter}")
