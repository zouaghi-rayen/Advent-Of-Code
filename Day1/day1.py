#!/usr/bin/python3

with open("input.txt", "r", encoding="utf-8") as file:
    instructions = file.readlines()

pos = 50
counter = 0
for instruction in instructions:
    instruction = instruction.strip()
    if not instruction:
        continue

    direction = instruction[0].upper()
    value = int(instruction[1:])
    print(f"direction {direction} : value {value}")

    if direction == "L":
        pos = (pos - value) % 100
    elif direction == "R":
        pos = (pos + value) % 100
    if pos == 0:
        counter += 1
print(counter)
