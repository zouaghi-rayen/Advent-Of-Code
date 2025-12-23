with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

id_ranges = [number_range.strip() for number_range in content.split(',')]

def is_invalid(number):
    string_number, length_number = str(number), len(str(number))
    for size in range(1, length_number// 2 + 1):
        if length_number % size == 0:
            pattern = string_number[:size]
            if pattern * (length_number // size) == string_number:
                return True
    return False

def is_invalid_part_one(number):
    string_number, length_number = str(number), len(str(number))
    return string_number[:length_number//2] == string_number[length_number//2:]

invalid_ids = []

for id_range in id_ranges:
    min_id, max_id = id_range.split('-')
    min_id = int(min_id)
    max_id = int(max_id)

    for id in range(min_id, max_id + 1):
        if is_invalid(id):
            invalid_ids.append(id)

print(sum(invalid_ids))