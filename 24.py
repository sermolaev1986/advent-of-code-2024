import re

def calc_and(a, b):
    return int(a and b)


def calc_or(a, b):
    return int(a or b)


def calc_xor(a, b):
    return int(a != b)

if __name__ == '__main__':
    with open("input/24.txt") as file:
        lines = file.readlines()

    results = {}

    # x00 AND y00 -> z00
    pattern = re.compile(r"(.+)\s([A-Z]+)\s(.+)\s->\s(.+)")
    known = set()
    input = []
    is_parsing_gates = True
    for line in lines:
        line = line.strip()
        if not line:
            is_parsing_gates = False
            continue

        if is_parsing_gates:
            split = line.strip().split(":")
            known.add((split[0]))
            results[split[0]] = int(split[1])
        else:
            input.append(pattern.findall(line)[0])

    print(known)
    print(input)

    graph = []
    while input:
        for element in input:
            if element[0] in known and element[2] in known:
                known.add(element[3])
                graph.append(element)
                input.remove(element)

    print(graph)

    gates = {'AND': calc_and, 'OR': calc_or, 'XOR': calc_xor}

    for operand1, gate, operand2, result_node in graph:
        results[result_node] = gates[gate](results[operand1], results[operand2])

    print(results)

    zs = []
    for key in results:
        if key.startswith('z'):
            zs.append(key)

    zs.sort(reverse=True)
    print(zs)

    binary_string = ''
    for z in zs:
        binary_string += str(results[z])

    print(int(binary_string, 2))