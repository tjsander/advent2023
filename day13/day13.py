#!/usr/bin/env python3
import re
import numpy

INPUT = 'day13/test_input.txt'
INPUT = 'day13/input.txt'

def get_reflections(puzzles):
    reflections = []
    for puzzle in puzzles:
        puzzle = numpy.copy(puzzle)
        reflections.append(100* find_vertical(puzzle))
        reflections.append(find_horizontal(puzzle))
    return reflections

def get_reflections_2(puzzles):
    reflections = []
    for puzzle in puzzles:
        puzzle = numpy.copy(puzzle)
        old_value = 100* find_vertical(puzzle)
        if (old_value == 0):
            old_value = find_horizontal(puzzle)
        value = get_new_reflection(puzzle, old_value)
        reflections.append(value)
    return reflections

def get_new_reflection(puzzle, old_value):
    i = 0
    old_val_found = 0
    zero_found = 0
    for y in range(0,len(puzzle)):
        for x in range(0,len(puzzle[0])):
            i += 1
            new_puzzle = permute(puzzle, y, x)
            new_value = 100* find_vertical(new_puzzle)
            if (new_value == old_value):
                old_val_found += 1
            else:
                if (new_value != 0):
                    return new_value
                else:
                    zero_found += 1
            new_value = find_horizontal(new_puzzle)
            if (new_value == old_value):
                old_val_found += 1
            else:
                if(new_value != 0):
                    return new_value
                else:
                    zero_found += 1
    return old_value

def permute(puzzle,y,x):
    new_puzzle = []
    new_puzzle = numpy.copy(puzzle)
    if puzzle[y][x] == "#":
        new_puzzle[y][x] = "."
    else:
        new_puzzle[y][x] = "#"
    return new_puzzle

def find_horizontal(puzzle):
    value = 0
    converted = []
    for i in range(len(puzzle[0])):
        converted.append([])
    # convert to vertical and find_vertical
    for i in range (0,len(puzzle)):
        for j in range(0,len(puzzle[0])):
            converted[j].append(puzzle[i][j])
    return find_vertical(converted)

def find_vertical(puzzle):
    for i in range (1, len(puzzle)):
        retval = 0
        if (numpy.array_equal(puzzle[i-1], puzzle[i])):
            for j in range (1, i+1):
                if (i+j > len(puzzle)-1 or i-j-1 < 0):
                    return i
                else:
                    if not (numpy.array_equal(puzzle[i+j], puzzle[i-j-1])):
                        break
            # return i
    return retval

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    numbers = []
    symbols = []
    values = []

    data = [list(x.strip()) for x in Lines]
    puzzles = []
    puzzle = []
    for line in data:
        if (line):
            puzzle.append(line)
        else:
            puzzles.append(puzzle)
            puzzle = []
    puzzles.append(puzzle)

    values = get_reflections(puzzles)
    print (sum(values))

    values = get_reflections_2(puzzles)
    # 17478 too low
    # 20686 too low
    print (sum(values))

if __name__ == '__main__':
    main()
