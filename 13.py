import re

import numpy as np


def is_integer(a_float):
    return a_float.is_integer()


def solve(a, b, prize):
    # print(a, b, prize)
    matrix = np.array([a, b])
    coefficients = np.array(prize)

    det = np.linalg.det(matrix)
    if det == 0:
        return 0,0

    X = np.linalg.solve(matrix, coefficients)
    X = np.round(X, decimals=2)
    if np.all(np.mod(X, 1) == 0):
        x1 = int(X[0])
        x2 = int(X[1])
        if x1 > 0 and x2 > 0:
            print("solution is ", a, b, prize, x1, x2)
            return x1, x2

    return 0,0

button_pattern = re.compile(r"X\+(\d+), Y\+(\d+)")
prize_pattern = re.compile(r"X=(\d+), Y=(\d+)")

def count_tokens(a, b):
    return a * 3 + b

def calculate(prize_offset):
    with open("input/13.txt") as file:
        lines = file.readlines()

    result = 0
    a = []
    b = []
    prize = []
    for line in lines:
        if line.startswith("Button A"):
            search = button_pattern.search(line)
            a.append(int(search.group(1)))
            b.append(int(search.group(2)))
        elif line.startswith("Button B"):
            search = button_pattern.search(line)
            a.append(int(search.group(1)))
            b.append(int(search.group(2)))
        elif line.startswith("Prize"):
            search = prize_pattern.search(line)
            prize = [int(search.group(1)) + prize_offset, int(search.group(2)) + prize_offset]

            a_times, b_times = solve(a, b, prize)
            result += count_tokens(a_times, b_times)
        else:
            a = []
            b = []
            prize = []

    print(result)

if __name__ == '__main__':
    calculate(0)
    calculate(10000000000000)
