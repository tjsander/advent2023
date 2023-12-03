#!/usr/bin/env python3
import re

# INPUT = 'day3/test_input.txt'
INPUT = 'day3/input.txt'

def is_adjacent():
    return true

def get_numbers(data):
    ret_numbers = []
    y = 0
    for row in data:
        x = 0
        row = re.sub('[^0-9a-zA-Z.]+', '.', row)

        x = 0
        # for x in range (0,len(row)):
        while x < len(row):
            if row[x] != ".":
                retme = ""
                xone = x
                while x < len(row) and row[x] != ".":
                    retme += row[x]
                    x+=1
                ret_numbers.append([int(retme), xone, y, x-1])
            else:
                x += 1
        y+=1
    return ret_numbers

def get_symbols(data):
    ret_numbers = []
    y = 0
    for row in data:
        row = re.sub('[0-9]', '.', row)
        for x in range (0,len(row)):
            if row[x] != ".":
                ret_numbers.append([row[x], x, y, x])
        y+=1
    return ret_numbers

def is_plus_minus(num1, num2):
    if abs(num2 - num1) >= 2:
        return False
    return True

def is_symbol_adjacent(number, symbols):
    for symbol in symbols:
        if is_plus_minus(number[2], symbol[2]):
            if is_plus_minus(number[1], symbol[1]) or is_plus_minus(number[3], symbol[3]):
                # if (number[0] < 10):
                if (number[0] == 95):
                    print("WHAT")
                return True
    return False

def get_values(numbers, symbols):
    values = []
    for number in numbers:
        if is_symbol_adjacent(number, symbols):
            values.append(int(number[0]))
    return values

def get_ratios(symbols, numbers):
    ratios = []
    for symbol in symbols:
        if symbol[0] == "*":
            gears = []
            for number in numbers:
                newsymbols = []
                newsymbols.append(symbol)
                if is_symbol_adjacent(number, newsymbols):
                    gears.append(number[0])
            if len(gears) == 2:
                ratios.append(gears[0]*gears[1])
    return ratios

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    numbers = []
    symbols = []
    values = []

    data = [x.strip() for x in Lines]
    numbers = get_numbers(data)
    symbols = get_symbols(data)

    values = get_values(numbers, symbols)
    print (sum(values))

    gear_ratios = get_ratios(symbols, numbers)
    print (sum(gear_ratios))

if __name__ == '__main__':
    main()
