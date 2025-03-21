def blink(numbers):
    i = 0
    while i < len(numbers):
        number = numbers[i]
        if number == 0:
            numbers[i] = 1
        elif len(str(number)) % 2 == 0:
            number_as_string = str(number)
            middle_index = len(number_as_string) // 2

            numbers[i] = int(number_as_string[:middle_index])
            # print("inserting {} at {}".format(number_as_string[middle_index:], i + 1))
            numbers.insert(i + 1, int(number_as_string[middle_index:]))
            i += 1
        else:
            numbers[i] *= 2024
        i += 1


if __name__ == '__main__':
    with open("input/11.txt") as file:
        line = file.read()

    numbers = [int(x) for x in line.split(" ")]
    # print(numbers)

    for _ in range(25):
        blink(numbers)
        print(numbers)

    print(len(numbers))
