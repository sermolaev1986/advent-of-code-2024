from enum import Enum

class Direction(Enum):
    INCREASE = 1
    DECREASE = 2

def calculate_direction(diff):
    return Direction.INCREASE if diff > 0 else Direction.DECREASE

def check_nums(nums):
    direction = None

    for i in range(len(nums) - 1):
        previous = nums[i]
        current = nums[i + 1]
        diff = current - previous

        if direction is None:
            direction = calculate_direction(diff)

        if abs(diff) > 3 or abs(diff) < 1 or calculate_direction(diff) != direction:
            return False

    return True

def check_line(line, tolerate_error):
    nums = [int(n) for n in line.split()]

    check_result = check_nums(nums)
    if check_result is True:
        return True
    else:
        if tolerate_error is True:
            for i in range(len(nums)):
                check_result = check_nums(nums[:i] + nums[i+1:])
                if check_result is True:
                    return True


def check(file_name, tolerate_error):
    result = 0
    with open(file_name) as file:
        for line in file:
            if check_line(line, tolerate_error):
                result += 1

    return result


def calculate(file_name):
    print("part 1: {}".format(check(file_name, tolerate_error=False)))
    print("part 2: {}".format(check(file_name, tolerate_error=True)))


if __name__ == '__main__':
    print("test set")
    calculate("2_test.txt")

    print()

    print("real set")
    calculate("2.txt")
