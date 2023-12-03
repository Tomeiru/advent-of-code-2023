import utils


def get_first_num_index(string: str):
    for index, letter in enumerate(string):
        if letter.isdigit():
            return index
    return -1


def part_1():
    result = 0
    for line in lines:
        first_index = get_first_num_index(line)
        reversed_line = line[::-1]
        second_index = len(line) - get_first_num_index(reversed_line) - 1
        result += int(line[first_index] + line[second_index])
    print(result)


numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def my_isdigit(string: str, idx):
    if string[idx].isdigit():
        return int(string[idx])
    if len(string) - 1 < idx + 2:
        return -1
    for ii in range(3, 6):
        substr = string[idx : idx + ii]
        if substr in numbers_str:
            return numbers[numbers_str.index(substr)]
    return -1


def part_2():
    result = 0
    for line in lines:
        first = -1
        last = 0
        for i in range(0, len(line)):
            digit = my_isdigit(line, i)
            if digit != -1:
                last = digit
                if first == -1:
                    first = digit
        result += int(str(first) + str(last))
    print(result)


if __name__ == "__main__":
    # file_content = utils.read_example("Day_01")
    file_content = utils.read_input("Day_01")
    lines = file_content.splitlines()
    part_1()
    part_2()
