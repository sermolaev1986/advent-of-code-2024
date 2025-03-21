from functools import cache

def apply_rule(number):
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        number_as_string = str(number)
        middle_index = len(number_as_string) // 2
        return [int(number_as_string[:middle_index]), int(number_as_string[middle_index:])]
    else:
        return [number * 2024]

@cache
def do_blink(numbers, times):
    if times == 0:
        return len(numbers)

    result = 0
    for number in numbers:
        result += do_blink(tuple(apply_rule(number)), times - 1)
    return result

if __name__ == '__main__':
    with open("input/11.txt") as file:
        line = file.read()

    numbers = [int(x) for x in line.split(" ")]

    result = do_blink(tuple(numbers), 75)

    print(result)
