with open("input.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

def find_biggest_number(bank): # bank = line here
    """
    finds the biggest number in a line in O(n^2) time complexity
    :param bank:
    :return:
    """
    biggest_number = 0
    for index, first_number in enumerate(bank):
        for second_number in bank[index + 1:]:
            number = int(first_number + second_number)
            if number > biggest_number:
                biggest_number = number

    return biggest_number


def find_biggest_number_window(bank, window=12):
    biggest_number = 0

    for index in range(len(bank) - window + 1):
        # Start with the current window
        result = []
        available = bank[index:]

        for pos in range(window):
            remaining_needed = window - pos - 1
            max_look_ahead = len(available) - remaining_needed

            best_digit = max(available[:max_look_ahead])
            best_index = available.index(best_digit)

            result.append(best_digit)
            available = available[best_index + 1:]

        number = int(''.join(result))
        if number > biggest_number:
            biggest_number = number

    return biggest_number if biggest_number > 0 else None

sum_of_biggest_numbers = 0

for line in lines:
    sum_of_biggest_numbers += find_biggest_number_window(line, 12)
print(sum_of_biggest_numbers)

