def get_grid(file_name):
    grid = []
    with open(file_name) as file:
        for line in file.readlines():
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            grid.append(row)
    return grid


def task1(file_name):
    grid = get_grid(file_name)

    print("RESULT: {}".format(Task1XmasFinder(grid).find()))

def task2(file_name):
    grid = get_grid(file_name)

    print("RESULT: {}".format(Task2XmasFinder(grid).find()))

class XmasFinder:
    def __init__(self, grid):
        self.grid = grid

    def is_dimension_valid(self, dimension):
        return 0 <= dimension < len(self.grid)

    def is_coordinate_valid(self, coordinate):
        return self.is_dimension_valid(coordinate[0]) and self.is_dimension_valid(coordinate[1])

class Task1XmasFinder(XmasFinder):
    def check_a(self, row, col, row_diff, col_diff):
        potential_s_row = row + row_diff
        potential_s_col = col + col_diff
        return self.is_coordinate_valid((potential_s_row, potential_s_col)) and self.grid[potential_s_row][potential_s_col] == 'S'

    def check_m(self, row, col, row_diff, col_diff):
        potential_a_row = row + row_diff
        potential_a_col = col + col_diff
        if self.is_coordinate_valid((potential_a_row, potential_a_col)) and self.grid[potential_a_row][
            potential_a_col] == 'A':
            return self.check_a(potential_a_row, potential_a_col, row_diff, col_diff)
            # if result:
            #     print("M ({},{}) -> A ({},{})".format(row, col, potential_a_row, potential_a_col))

    def check_x(self, row, col):
        neighbors = [(row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                     (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        neighbors = [x for x in neighbors if self.is_coordinate_valid(x)]

        result = 0
        for (neighbor_row, neighbor_col) in neighbors:
            if self.grid[neighbor_row][neighbor_col] == 'M':
                if self.check_m(neighbor_row, neighbor_col, neighbor_row - row, neighbor_col - col):
                    # print("X ({},{}) -> M ({},{})".format(row, col, neighbor_row, neighbor_col))
                    # print()
                    # print()

                    result += 1

        return result

    def find(self):
        result = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 'X':
                    result += self.check_x(row, col)

        return result


class Task2XmasFinder(XmasFinder):
    def check_diagonal(self, diagonal):
        required_chars = {'M', 'S'}
        actual_chars = set()
        for coordinate in diagonal:
            if not self.is_coordinate_valid(coordinate):
                return False
            else:
                actual_chars.add(self.grid[coordinate[0]][coordinate[1]])
        return required_chars.issubset(actual_chars)

    def check_a(self, row, col):
        diagonal_1 = [(row - 1, col - 1), (row + 1 , col + 1)]
        diagonal_2 = [(row + 1, col - 1), (row - 1 , col + 1)]

        return self.check_diagonal(diagonal_1) and self.check_diagonal(diagonal_2)

    def find(self):
        result = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 'A':
                    if self.check_a(row, col):
                        result += 1

        return result

if __name__ == '__main__':
    print("-----TASK 1-------")

    print("test set")
    task1("4_test.txt")

    print()

    print("real set")
    task1("4.txt")

    print("-----TASK 2-------")

    print("test set")
    task2("4_test.txt")

    print()

    print("real set")
    task2("4.txt")
