def print_grid(grid):
    print()
    for row in grid:
        for column in row:
            print(column, end="")
        print()
    print()


def is_coordinate_valid(coordinate, grid):
    return 0 <= coordinate[0] < len(grid) and 0 <= coordinate[1] < len(grid[0])

def get_score(row, column, grid):
    number = grid[row][column]
    if number == 9:
        # print("found 9 at {}".format((row, column)))
        return 1
    else:
        neighbours = get_valid_neighbours(row, column, grid)
        score = 0
        for neighbour in neighbours:
            if grid[neighbour[0]][neighbour[1]] == number + 1:
                # print("found potential path from {} to {}, on number {}".format((row, column), neighbour, number + 1))
                score += get_score(neighbour[0], neighbour[1], grid)
        return score

def get_valid_neighbours(row, column, grid):
    neighbours = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
    return [neighbour for neighbour in neighbours if is_coordinate_valid(neighbour, grid)]

if __name__ == '__main__':
    grid = []
    with open("input/10.txt") as file:
        for line in file.readlines():
            row = []
            for number in line:
                if number != "\n":
                    row.append(int(number))
            grid.append(row)

    # print_grid(grid)

    total_score = 0
    for row_index in range(len(grid)):
        row = grid[row_index]
        for column_index in range(len(row)):
            number = row[column_index]
            if number == 0:
                score = get_score(row_index, column_index, grid)
                # print("score of {} is {}".format((row_index, column_index), score))
                total_score += score

    print(total_score)