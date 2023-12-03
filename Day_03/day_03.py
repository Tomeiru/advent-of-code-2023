import utils


def get_number_info(line, ii):
    number = []
    last_index = ii
    for i in range(ii, len(line)):
        if not line[i].isdigit():
            break
        number.append(line[i])
        last_index = i
    return (ii, last_index), int("".join([str(x) for x in number]))


def get_symbols_and_numbers():
    symbols = []
    numbers = []
    for i, line in enumerate(lines):
        for ii, char in enumerate(line):
            if not char.isdigit() and char != '.':
                symbols.append((i, ii, char))
            if len(numbers) != 0:
                last_number = numbers[-1]
                if i == last_number[0] and last_number[1][0] <= ii <= last_number[1][1]:
                    continue
            if char.isdigit():
                span, number = get_number_info(line, ii)
                numbers.append((i, span, number))
    return symbols, numbers


def are_adjacent(symbol, number):
    return symbol[0] - 1 <= number[0] <= symbol[0] + 1 and number[1][0] - 1 <= symbol[1] <= number[1][1] + 1


def part_1():
    result = 0
    for number in numbers:
        for symbol in symbols:
            if are_adjacent(symbol, number):
                result += number[2]
    print(result)


def part_2():
    result = 0
    for symbol in symbols:
        if symbol[2] != '*':
            continue
        adjacent = []
        for number in numbers:
            if are_adjacent(symbol, number):
                adjacent.append(number[2])
        if len(adjacent) == 2:
            result += adjacent[0] * adjacent[1]
    print(result)


if __name__ == "__main__":
    # file_content = utils.read_example("Day_03")
    file_content = utils.read_input("Day_03")
    lines = file_content.splitlines()
    symbols, numbers = get_symbols_and_numbers()
    part_1()
    part_2()
