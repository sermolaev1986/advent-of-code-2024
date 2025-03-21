import re

result = []

def adv(operand, registers, pointer):
    registers[0] = registers[0] // pow(2, int(get_combo_operand(operand, registers)))
    return pointer + 1

def bxl(operand, registers, pointer):
    registers[1] = registers[1] ^ operand
    return pointer + 1

def bst(operand, registers, pointer):
    registers[1] = get_combo_operand(operand, registers) % 8
    return pointer + 1

def jnz(operand, registers, pointer):
    if registers[0] == 0:
        return pointer + 1
    else:
        return operand

def bxc(operand, registers, pointer):
    registers[1] = registers[1] ^ registers[2]
    return pointer + 1

def out(operand, registers, pointer):
    result.append(get_combo_operand(operand, registers) % 8)
    return pointer + 1

def bdv(operand, registers, pointer):
    registers[1] = registers[0] // pow(2, int(get_combo_operand(operand, registers)))
    return pointer + 1

def cdv(operand, registers, pointer):
    registers[2] = registers[0] // pow(2, int(get_combo_operand(operand, registers)))
    return pointer + 1

def get_combo_operand(operand, registers):
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6:
        return registers[operand - 4]
    else:
        raise IndexError

def execute(program, registers):
    result.clear()
    instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    pointer = 0
    while pointer < len(program):
        opcode, operand = program[pointer]
        # print("pointer", pointer)
        # print("registers", registers)
        # print("operand", operand)
        # print("opcode", opcode)
        pointer = instructions[int(opcode)](int(operand), registers, pointer)

    return ",".join(map(str, result))

def task1(program, registers):
    print(execute(program, registers))

def task2(program, program_string):
    i = 0
    while True:
        registers = [i, 0, 0]
        if execute(program, registers) == program_string:
            print(i)
            break
        else:
            i += 1

if __name__ == '__main__':
    with open("input/17.txt") as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("Register A"):
            a = int(re.compile(r"Register A: (\d+)").search(line).group(1))
        elif line.startswith("Register B"):
            b = int(re.compile(r"Register B: (\d+)").search(line).group(1))
        elif line.startswith("Register C"):
            c = int(re.compile(r"Register C: (\d+)").search(line).group(1))
        elif line.startswith("Program"):
            program_string = re.compile(r"Program: (.+)").search(line).group(1)

    # print(a, b, c)
    registers = []
    registers.append(a)
    registers.append(b)
    registers.append(c)

    program_array = program_string.split(",")
    # print(program_array)

    program = []
    for i in range(0, len(program_array), 2):
        program.append((program_array[i], program_array[i + 1]))

    task1(program, registers)
    # task2(program, program_string)