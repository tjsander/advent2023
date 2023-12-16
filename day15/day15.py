#!/usr/bin/env python3
import re

INPUT = 'day15/test_input.txt'
INPUT = 'day15/input.txt'

def get_hash_values(problems):
    values = []
    for problem in problems:
        current_val = 0
        for char in problem:
            current_val += ord(char)
            current_val = current_val * 17
            current_val = current_val % 256
        values.append(current_val)
    return values

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    problems = []

    for line in Lines:
        problems = list(line.strip().split(","))
        print(line)

    values = get_hash_values(problems)

    print(sum(values))



if __name__ == '__main__':
    main()
