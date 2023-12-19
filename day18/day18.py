#!/usr/bin/env python3
import re

INPUT = 'day18/test_input.txt'
INPUT = 'day18/input.txt'
MAP_INPUT = 'day18/day18map.txt'
PROCESS_MAP = True

def generate_grid(instructions):
    grid = []
    dimensions = [[0,0]]
    for instruct in instructions:
        dimensions.extend(process_instruct(instruct[0],int(instruct[1]),dimensions))

    x_arr = []
    y_arr = []
    for dimension in dimensions:
        x_arr.append(dimension[1])
        y_arr.append(dimension[0])

    max_x = max(x_arr)
    max_y = max(y_arr)
    min_x = min(x_arr)
    min_y = min(y_arr)

    map_string = ""
    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            if [y,x] in dimensions:
                map_string += "#"
            else:
                map_string += "."
        map_string += "\n"
    print(map_string)
    return dimensions

def process_instruct(direction, length, dimensions):
    current_x = dimensions[-1][1]
    current_y = dimensions[-1][0]

    new_coords = []

    for i in range(0,length):
        match (direction):
            case "U":
                current_y-=1
            case "D":
                current_y+=1
            case "R":
                current_x+=1
            case "L":
                current_x-=1
        new_coords.append([current_y, current_x])
    return new_coords

def find_all_empty_spaces(known_empties, new_spaces, large_area_grid):
    spaces = []
    for space in new_spaces:
        spaces.extend(get_surrounding_empties(space, large_area_grid))
    new_spaces = list(set(spaces) - set(known_empties))

    if (len(new_spaces)!=0):
        known_empties.extend(new_spaces)
        find_all_empty_spaces(known_empties, new_spaces, large_area_grid)
    return known_empties

def get_surrounding_empties(space, grid):
    empties = []
    y, x = space

    directions = [(y-1, x),(y+1, x),(y, x+1),(y, x-1)]

    for direction in directions:
        y,x = direction
        if (y>-1 and x>-1 and x<len(grid[0]) and y<len(grid)):
            if (grid[y][x] == "."): empties.append(direction)
    return empties

def remove_edges(large_area_grid):
    grid = []
    for row in large_area_grid:
        grid.append(list(row))

    empty_spaces = [(0,0)]
    empty_spaces = find_all_empty_spaces(empty_spaces, empty_spaces, large_area_grid)

    for space in empty_spaces:
        grid[space[0]][space[1]] = " "

    return grid

def main():
    if not PROCESS_MAP:
        input_file = open(INPUT, 'r')
        Lines = input_file.readlines()
        count = 0
        values = []

        instructions = []

        for line in Lines:
            # print (line.strip())
            instructions.append(line.strip().split(" "))

        grid = generate_grid(instructions)

    if PROCESS_MAP:
        input_file = open(MAP_INPUT, 'r')
        Lines = input_file.readlines()
        large_area_grid = []
        for line in Lines:
            large_area_grid.append(line.strip())

        final_grid = remove_edges(large_area_grid)

        count = 0
        for row in final_grid:
            count += row.count('.')
            count += row.count('#')
        print(count)
        # 30401 too low

if __name__ == '__main__':
    main()
