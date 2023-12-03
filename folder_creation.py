import argparse
import os
import sys


def create_aoc_folder(day_number: int):
    formatted_day_number = str(day_number).zfill(2)
    folder_name = f"Day_{formatted_day_number}"
    file_content = (
        "import utils\n\n\n"
        "def part_1():\n"
        "    result = 0\n"
        "    print(result)\n\n\n"
        "def part_2():\n"
        "    result = 0\n"
        "    print(result)\n\n\n"
        'if __name__ == "__main__":\n'
        f'    # file_content = utils.read_example("{folder_name}")\n'
        f'    file_content = utils.read_input("{folder_name}")\n'
        "    lines = file_content.splitlines()\n"
        "    part_1()\n"
        "    part_2()\n"
    )
    os.mkdir(folder_name)
    open(f"{folder_name}/__init__.py", "w").close()
    open(f"{folder_name}/input", "w").close()
    open(f"{folder_name}/input_example", "w").close()
    code_file = open(f"{folder_name}/day_{formatted_day_number}.py", "w")
    code_file.write(file_content)
    code_file.close()


parser = argparse.ArgumentParser(
    prog="python3 folder_creation.py",
    description="This script create a folder with everything required for an Advent of Code day in Python",
)
parser.add_argument(
    "day",
    help="day number of the folder you want to create",
    type=int,
    choices=range(1, 26),
)

args = parser.parse_args()

create_aoc_folder(args.day)
