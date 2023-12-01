#!/usr/bin/env python3
import re

# INPUT = 'day1/test_input.txt'
# INPUT = 'day1/test_input2.txt'
INPUT = 'day1/input.txt'

NUMSTRINGS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# On each line, the calibration value can be found by
# combining the first digit and the last digit (in that order)
# to form a single two-digit number.

def remove_item(list, item):
    res = [i for i in list if i != item]
    return res


def numstring_to_digit(line):
    line = line + ""
    # print (line)

    loopbreak = 0
    for x in range(0, len(line)):
        if (loopbreak == 1): break
        if (line[x].isdigit()): break
        for y in range(0, 10):
            if (line[x:len(NUMSTRINGS[y])+x] == NUMSTRINGS[y]):
                print (line + " found " + NUMSTRINGS[y])
                line = line.replace(NUMSTRINGS[y], str(y), 1)
                loopbreak = 1
                break

    loopbreak = 0
    for x in range(0, len(line)):
        if (loopbreak == 1): break
        z = len(line) - x
        for y in range(0, 10):
            if (line[z-len(NUMSTRINGS[y]):z] == NUMSTRINGS[y]):
                print (line + " found " + NUMSTRINGS[y])
                line = line.replace(NUMSTRINGS[y], str(y))
                loopbreak = 1
                break
    return line

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    for line in Lines:
        line = numstring_to_digit(line.strip())

        newline = re.split('[a-zA-Z]', line.strip())
        newline = remove_item(newline, '')
        print (newline)
        value = int(newline[0][0] + newline[-1][-1])
        print (value)
        values.append(value)

    print (values)
    # print (len(values))
    print (sum(values))


if __name__ == '__main__':
    main()
