#!/usr/bin/env python3
import re

INPUT = 'day10/test_input.txt'
INPUT = 'day10/test_input_2.txt'
INPUT = 'day10/test_input_3.txt'
INPUT = 'day10/test_input_4.txt'
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
            if (coords[1] != -1 and coords[1] < len(grid[0])):
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

## PART 2... WHAT THE ACTUAL EFFFFFFFFF

def char_big(character):
    if character == "|": return [".x.",".x.",".x."]
    if character == "-": return ["...","xxx","..."]
    if character == "L": return [".x.",".xx","..."]
    if character == "J": return [".x.","xx.","..."]
    if character == "7": return ["...","xx.",".x."]
    if character == "F": return ["...",".xx",".x."]
    if character == ".": return ["...","...","..."]
    if character == "S": return [".x.","xSx",".x."]

def print_larger_grid(area_grid):
    big_grid = []
    for grid_y in area_grid:
        for y in range(0,3):
            big_grid_x = ""
            for x in range (0,len(area_grid[0])):
                big_grid_x += char_big(grid_y[x])[y]
            big_grid.append(big_grid_x)
    return big_grid

def remove_edges(large_area_grid):
    grid = []
    for row in large_area_grid:
        grid.append(list(row))

    empty_spaces = [(0,0)]
    empty_spaces = find_all_empty_spaces(empty_spaces, empty_spaces, large_area_grid)

    for space in empty_spaces:
        grid[space[0]][space[1]] = " "

    grid = shrink_grid(grid)

    return grid

def shrink_grid(grid):
    smol = []

    for y in range(1, len(grid), 3):
        y_str = ""
        for x in range (1, len(grid[0]), 3):
            y_str += grid[y][x]
        smol.append(y_str)
    return smol

def get_surrounding_empties(space, grid):
    empties = []
    y, x = space

    directions = [(y-1, x),(y+1, x),(y, x+1),(y, x-1)]

    for direction in directions:
        y,x = direction
        if (y>-1 and x>-1 and x<len(grid[0]) and y<len(grid)):
            if (grid[y][x] == "."): empties.append(direction)
    return empties

def find_all_empty_spaces(known_empties, new_spaces, large_area_grid):
    spaces = []
    for space in new_spaces:
        spaces.extend(get_surrounding_empties(space, large_area_grid))
    new_spaces = list(set(spaces) - set(known_empties))

    if (len(new_spaces)!=0):
        known_empties.extend(new_spaces)
        find_all_empty_spaces(known_empties, new_spaces, large_area_grid)
    return known_empties

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

    area_grid = []
    for y in range(0,len(grid)):
        grid_x = []
        for x in range(0,len(grid[0])):
            if ((y, x) in values):
                grid_x.append(grid[y][x])
            else:
                grid_x.append(".")
        area_grid.append(grid_x)

    for grid_l in area_grid:
        str = ""
        print (str.join(grid_l))

    large_area_grid = print_larger_grid(area_grid)

    for grid_l in large_area_grid:
        # str = ""
        # print (str.join(grid_l))
        print (grid_l)

    final_grid = remove_edges(large_area_grid)

    count = 0
    for row in final_grid:
        count += row.count('.')

    print(count)

if __name__ == '__main__':
    main()
