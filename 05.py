def parse_rules_and_instructions(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    rules = []
    instructions = []
    for line in lines:
        line = line.replace("\n", "")
        # print(line)
        if '|' in line:
            split = line.split("|")
            rules.append((split[0], split[1]))
        elif ',' in line:
            instruction = line.split(',')
            # print(instruction)
            instructions.append(instruction)

    print("--------------")

    return rules, instructions


def is_instruction_valid(instruction, rules):
    for rule in rules:
        if rule[0] in instruction and rule[1] in instruction:
            if instruction.index(rule[0]) > instruction.index(rule[1]):
                return False
    return True


def repair_instruction(instruction, rules):
    swap_count = -1
    while swap_count != 0:
        swap_count = 0
        for rule in rules:
            left = rule[0]
            right = rule[1]
            if left in instruction and right in instruction:
                right_index = instruction.index(right)
                left_index = instruction.index(left)
                if right_index < left_index:
                    instruction[right_index] = left
                    instruction[left_index] = right
                    swap_count += 1

    return instruction


def get_middle(instruction):
    return int(instruction[int(len(instruction) / 2)])


def task1(file_name):
    rules, instructions = parse_rules_and_instructions(file_name)

    result = 0
    for instruction in instructions:
        if is_instruction_valid(instruction, rules):
            result += get_middle(instruction)
    print(result)


def task2(file_name):
    rules, instructions = parse_rules_and_instructions(file_name)

    result = 0
    for instruction in instructions:
        if not is_instruction_valid(instruction, rules):
            instruction = repair_instruction(instruction, rules)
            result += get_middle(instruction)
    print(result)


if __name__ == '__main__':
    print("-----TASK 1-------")

    print("test set")
    task1("input/5_test.txt")

    print()

    print("real set")
    task1("input/5.txt")

    print("-----TASK 2-------")

    print("test set")
    task2("input/5_test.txt")

    print()

    print("real set")
    task2("input/5.txt")
