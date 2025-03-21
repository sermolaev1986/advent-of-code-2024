def prepare_array(file_name):
    with open(file_name) as file:
        input = file.read()

    array = []
    for i in range(len(input)):
        if i % 2 == 0:
            array += int(input[i]) * [int(i / 2)]
        else:
            array += int(input[i]) * ['.']
    return array


def task1(file_name):
    array = prepare_array(file_name)

    result = 0
    i = 0
    j = len(array) - 1
    while i <= j:
        if array[j] == '.':
            j -= 1
            continue

        if array[i] == '.':
            result += int(array[j]) * i
            j -= 1
        else:
            result += int(array[i]) * i

        i += 1

    print(result)


def task2(file_name):
    with open(file_name) as file:
        input = file.read()

    files = []
    free_spaces = []
    array = []
    current_index = 0
    for i in range(len(input)):
        if i % 2 == 0:
            files.append((int(i / 2), int(input[i]), current_index))
            array += int(input[i]) * [int(i / 2)]
            current_index += int(input[i])
        else:
            free_spaces.append((current_index, int(input[i])))
            current_index += int(input[i])
            array += int(input[i]) * ['.']

    def find_next_space_index(file, spaces):
        for i in range(len(spaces)):
            if file[1] <= spaces[i][1] and spaces[i][0] < file[2]:
                return i

    while files:
        file = files.pop()
        space_index = find_next_space_index(file, free_spaces)

        if space_index is not None:
            space = free_spaces[space_index]
            # print(f"File {file} fits in space {space}")
            array[space[0]:space[0] + file[1]] = [file[0]] * file[1]
            array[file[2]:file[2] + file[1]] = ['.'] * file[1]
            left_space = space[1] - file[1]
            if left_space == 0:
                free_spaces.pop(space_index)
            else:
                free_spaces[space_index] = (space[0] + file[1], space[1] - file[1])

    # print(free_spaces)
    # print(''.join([str(x) for x in array]))
    # print(array)

    result = 0
    for i in range(len(array)):
        if array[i] != '.':
            result += int(array[i]) * i
    print(result)


if __name__ == '__main__':
    task1("input/9.txt")
    task2("input/9.txt")


