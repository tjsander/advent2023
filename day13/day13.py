#!/usr/bin/env python3
import re

INPUT = 'day13/test_input.txt'
# INPUT = 'day13/input.txt'

def get_reflections(puzzles):
    reflections = []
    for puzzle in puzzles:
        reflections.append(find_horizontal(puzzle))
        reflections.append(100* find_vertical(puzzle))
    return reflections

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
        if (puzzle[i-1] == puzzle[i]):
            for j in range (1, i+1):
                if (i+j > len(puzzle)):
                    return j
            return 0
    return 0

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

    # 12488 too low
    print (sum(values))

if __name__ == '__main__':
    main()
