#!/usr/bin/env python3
import re

INPUT = 'day10/test_input.txt'
INPUT = 'day10/test_input_2.txt'
INPUT = 'day10/input.txt'

# 140x140 grid
# example 5x5
# from S, traverse loop in one direction

def find_next(grid, current, previous):
    (y, x) = current
    current_char = grid[y][x]
    next_dir = (0,0)
    north = (y-1, x)
    south = (y+1, x)
    east  = (y, x+1)
    west  = (y, x-1)
    if (current_char == "S"):
        dirs = [("N", north), ("S", south), ("E", east), ("W", west)]
    if (current_char == "|"):
        dirs = [("N", north), ("S", south)]
    if (current_char == "-"):
        dirs = [("E", east), ("W", west)]
    if (current_char == "L"):
        dirs = [("N", north), ("E", east)]
    if (current_char == "J"):
        dirs = [("N", north), ("W", west)]
    if (current_char == "7"):
        dirs = [("S", south), ("W", west)]
    if (current_char == "F"):
        dirs = [("S", south), ("E", east)]
    for direction in dirs:
        coords = direction[1]
        if (coords[0] != -1 and coords[0] < len(grid)):
            if (coords[1] != -1 and coords[1] < len(grid)):
                if (previous != coords and coords != current):
                    if (is_connected(grid, direction[0], direction[1])):
                        next_dir = direction[1]
    return next_dir

def is_connected(grid, char_direction, coordinates):
    cell = grid[coordinates[0]][coordinates[1]]
    if (cell == "S"): return True
    if (char_direction == "N"):
        if (cell == "|" or cell == "7" or cell == "F"):
            return True
    if (char_direction == "S"):
        if (cell == "|" or cell == "L" or cell == "J"):
            return True
    if (char_direction == "E"):
        if (cell == "-" or cell == "J" or cell == "7"):
            return True
    if (char_direction == "W"):
        if (cell == "-" or cell == "L" or cell == "F"):
            return True
    return False

def find_start(grid):
    x = 0
    y = 0
    for row in grid:
        y = 0
        for letter in row:
            if (letter == "S"):
                return (x, y)
            y+=1
        x+=1

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    grid = []

    for line in Lines:
        print(line.strip())
        grid.append(list(line.strip()))

    start = find_start(grid)
    previous = start
    current = find_next(grid, start, start)
    values.append(current)

    while current != start:
        previous_hold = current
        current = find_next(grid, current, previous)
        values.append(current)
        previous = previous_hold

    print (values)
    print (len(values)/2)


if __name__ == '__main__':
    main()
