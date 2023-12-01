#!/usr/bin/env python3
import re

# INPUT = 'day1/test_input.txt'
INPUT = 'day1/input.txt'

# On each line, the calibration value can be found by 
# combining the first digit and the last digit (in that order) 
# to form a single two-digit number.


def remove_item(list, item): 
    res = [i for i in list if i != item] 
    return res

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    for line in Lines:
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
