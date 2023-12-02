#!/usr/bin/env python3
import re

# INPUT = 'day2/test_input.txt'
INPUT = 'day2/input.txt'

# 12 red cubes, 13 green cubes, and 14 blue cubes
RED = 12
GREEN = 13
BLUE = 14

def is_possible(i, color):
    if (color == "red" and i > RED): return False
    if (color == "green" and i > GREEN): return False
    if (color == "blue" and i > BLUE): return False
    return True

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    i = 0
    for line in Lines:
        i += 1
        qualified = 0
        line = line.strip().split(': ')[1]
        examples = line.split('; ')
        for example in examples:
            # print (example)
            pairs = example.split(", ")
            # print (pairs)
            for pair in pairs:
                # print (pair)
                pair = pair.split(" ")
                if not is_possible(int(pair[0]), pair[1]):
                    qualified = 1
                    print(pair)
        if qualified == 0: values.append(i)


    print (sum(values))



if __name__ == '__main__':
    main()
