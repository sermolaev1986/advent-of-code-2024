def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end="")
        print()

def is_coordinate_valid(coordinate, grid):
    return 0 <= coordinate[0] < len(grid) and 0 <= coordinate[1] < len(grid[0])

if __name__ == '__main__':
    grid = []
    with open("input/8.txt") as file:
        for line in file.readlines():
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            grid.append(row)

    # print_grid(grid)

    antennas = {}
    antinode_grid = [['.' for _ in row] for row in grid]

    # print()
    # print_grid(antinode_grid)

    for row_index in range(len(grid)):
        row = grid[row_index]
        for column_index in range(len(row)):
            char = row[column_index]
            if char != '.':
                if char in antennas:
                    # print("found antenna {} at {}".format(char, (row_index, column_index)))
                    for antenna in antennas[char]:
                        # print(antenna)
                        row_diff = abs(row_index - antenna[0])
                        column_diff = column_index - antenna[1]
                        # print(row_diff, column_diff)
                        antinode_1 = (antenna[0] - row_diff, antenna[1] - column_diff)
                        antinode_2 = (row_index + row_diff, column_index + column_diff)

                        if is_coordinate_valid(antinode_1, grid):
                            # print("adding antinode at {}".format(antinode_1))
                            antinode_grid[antinode_1[0]][antinode_1[1]] = '#'
                        if is_coordinate_valid(antinode_2, grid):
                            # print("adding antinode at {}".format(antinode_2))
                            antinode_grid[antinode_2[0]][antinode_2[1]] = '#'

                        # print()
                        # print_grid(antinode_grid)
                    antennas[char].append((row_index, column_index))
                else:
                    antennas[char] = [(row_index, column_index)]

    # print(antennas)
    # print_grid(antinode_grid)

    result = 0
    for row in antinode_grid:
        for char in row:
            if char == '#':
             result += 1

    print(result)
