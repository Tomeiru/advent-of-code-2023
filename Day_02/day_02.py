import utils

bag_content = {
    "blue": 14,
    "green": 13,
    "red": 12,
}


def get_game_number(game_title):
    _, game_number = game_title.split(" ")
    return int(game_number)


def parse_set(cube_set):
    cubes = cube_set.split(",")
    cube_set = {}
    for cube in cubes:
        number, color = cube.split()
        cube_set[color] = int(number)
    return cube_set


def is_cube_set_valid(cubes):
    for color, number in cubes.items():
        if bag_content[color] < number:
            return False
    return True


def part_1():
    result = 0
    for line in lines:
        valid = True
        game_title, cube_sets = line.split(":")
        game_number = get_game_number(game_title)
        cube_sets = cube_sets.split(";")
        for cube_set in cube_sets:
            cube_set = parse_set(cube_set)
            if not is_cube_set_valid(cube_set):
                valid = False
                break
        if valid:
            result += game_number
    print(result)


def update_max_cube_set(max_cubes, cubes):
    for color, number in cubes.items():
        if max_cubes[color] < number:
            max_cubes[color] = number


def part_2():
    result = 0
    for line in lines:
        _, cube_sets = line.split(":")
        cube_sets = cube_sets.split(";")
        max_cube_set = {"red": 0, "blue": 0, "green": 0}
        for cube_set in cube_sets:
            cube_set = parse_set(cube_set)
            update_max_cube_set(max_cube_set, cube_set)
        result += max_cube_set["red"] * max_cube_set["green"] * max_cube_set["blue"]
    print(result)


if __name__ == "__main__":
    # file_content = utils.read_example("Day_02")
    file_content = utils.read_input("Day_02")

    lines = file_content.splitlines()
    part_1()
    part_2()
