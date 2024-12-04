def part_1(left, right):
    result = 0
    for l, r in zip(sorted(left), sorted(right)):
        result += abs(l - r)

    return result


def part_2(left, right):
    count_dict = {}

    for a in right:
        count_dict[a] = count_dict.get(a, 0) + 1

    result = 0
    for a in left:
        result += count_dict.get(a, 0) * a
    return result

def calculate(file_name):
    left = []
    right = []

    with open(file_name) as file:
        for line in file:
            split_line = line.split()
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))

    print("part 1: {}".format(part_1(left, right)))
    print("part 2: {}".format(part_2(left, right)))


if __name__ == '__main__':
    print("test set")
    calculate("1_test.txt")

    print()

    print("real set")
    calculate("1.txt")
