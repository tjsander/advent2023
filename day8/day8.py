#!/usr/bin/env python3
import re

# INPUT = 'day8/test_input.txt'
INPUT = 'day8/input.txt'

def next_node():
    return node

def parse_nodes(lines):
    nodes = {}
    for line in lines:
        name = line.split(" = ")[0]
        dest = line.split(" = (")[1].split(", ")

        nodes[name + 'L'] = dest[0]
        nodes[name + "R"] = dest[1][:3]

    return nodes

# def next_node(destination, nodes):
#     return nodes[destination]

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    instructions = Lines[0].strip()

    nodes = parse_nodes(Lines[2:])

    current_node = "AAA"
    i = 0
    while (current_node[:3] != "ZZZ"):
        current_node = nodes[current_node + instructions[i % len(instructions)]]
        i += 1

    print (i)


if __name__ == '__main__':
    main()
