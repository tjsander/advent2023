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

def dirty(line):
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    return line

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    for line in Lines:
        # line = numstring_to_digit(line.strip())
        line = dirty(line.strip())

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
