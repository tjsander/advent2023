#!/usr/bin/env python3
import re

INPUT = 'day21/test_input.txt'
# INPUT = 'day21/input.txt'


def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    for line in Lines:
        print (line.strip())
        value = 0
        values.append(value)

    print (values)
    print (sum(values))


if __name__ == '__main__':
    main()
