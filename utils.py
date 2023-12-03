def read_input(folder):
    input_file = open(f"{folder}/input", "r")
    file_content = input_file.read()
    input_file.close()
    return file_content


def read_example(folder):
    input_file = open(f"{folder}/input_example", "r")
    file_content = input_file.read()
    input_file.close()
    return file_content
