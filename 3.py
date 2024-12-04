import re

def task1(file_name):
    pattern = re.compile(r'mul\((\d+),(\d+)\)')

    with open(file_name) as file:
        result = 0
        for line in file.readlines():
            for (first, second) in re.findall(pattern, line):
                result += int(first) * int(second)

        print(result)

def task2(file_name):
    pattern = re.compile(r'mul\((\d+),(\d+)\)|(don\'t\(\)|(do\(\)))')

    with open(file_name) as file:
        result = 0
        enable = True
        for line in file.readlines():
            for (first, second, dont, do) in re.findall(pattern, line):
                if dont == 'don\'t()':
                    enable = False
                elif do == 'do()':
                    enable = True
                elif enable:
                    result += int(first) * int(second)

        print(result)

if __name__ == '__main__':
    print("task 1")

    print("test set")
    task1("3_test.txt")

    print()

    print("real set")

    print()
    task1("3.txt")
    print()

    print("task 2")

    print("test set")
    task2("3_test.txt")

    print()

    print("real set")
    task2("3.txt")