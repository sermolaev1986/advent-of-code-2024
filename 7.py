import time


def int_to_base(number, base, total_digits):
    if number == 0:
        return "0" * total_digits
    digits = []
    while number:
        digits.append(str(number % base))
        number //= base
    base_representation = ''.join(reversed(digits))
    return base_representation.zfill(total_digits)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def concatenate(a, b):
    return int(str(a) + str(b))


operators = [add, multiply, concatenate]


def apply(n_base_string, numbers):
    result = 0
    for i in range(len(n_base_string)):
        operator = operators[int(n_base_string[i])]
        if i == 0:
            result = operator(numbers[0], numbers[1])
        else:
            result = operator(result, numbers[i + 1])

    return result


def validate(test_value, numbers, base):
    n = len(numbers) - 1

    for i in range(pow(base, n)):
        n_base_string = int_to_base(i, base, n)
        # did not bring any performance gain
        # if base == 3 and '2' not in n_base_string:
        #     continue
        if apply(n_base_string, numbers) == test_value:
            return True

    return False


def parse(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    result = []

    for line in lines:
        split = line.split(":")
        test_value = int(split[0])
        numbers = [int(number) for number in split[1].strip().split(" ")]
        result.append((test_value, numbers))

    return result


def calculate(lines, base):
    result = 0
    failed = []

    for line in lines:
        test_value, numbers = line
        if validate(test_value, numbers, base):
            result += test_value
        else:
            failed.append(line)

    return result, failed


def task1(file_name):
    lines = parse(file_name)
    start = time.time()

    result, failed = calculate(lines, 2)

    print("task 1: {}".format(result))
    result2, failed = calculate(failed, 3)
    print("task 2: {}".format(result + result2))

    end = time.time()
    print(end - start, "secs.")


if __name__ == '__main__':
    print("test set")
    task1("input/7_test.txt")

    print()

    print("real set")
    task1("input/7.txt")
