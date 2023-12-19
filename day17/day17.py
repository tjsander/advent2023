#!/usr/bin/env python3
import re

INPUT = 'day17/test_input.txt'
# INPUT = 'day17/input.txt'

def traverse(grid):
    visited = ["0,0"]
    heat = 0
    y = 0
    x = 0
    do_continue = True
    while (do_continue):
        directions = get_valid_directions(visited,grid)

        if (len(directions)==0): return visited

        least_heat = 666
        go_direction = []
        for direction in directions:
            next_heat = int(grid[direction[0]][direction[1]])
            if next_heat < least_heat:
                go_direction = direction
                least_heat = next_heat
        heat += least_heat
        visited.append(str(go_direction[0])+ "," + str(go_direction[1]))
    return visited

def get_valid_directions(visited,grid):
    directions = []
    return_directions = []
    current = visited[-1].split(",")

    y = int(current[0])
    x = int(current[1])

    if x+1 < len(grid[0]):
        directions.append([y,x+1])
    if x-1 >= 0:
        directions.append([y,x-1])
    if y-1 >= 0:
        directions.append([y-1,x])
    if y+1 < len(grid):
        directions.append([y+1,x])
    for direction in directions:
        dir_string = str(direction[0]) + "," + str(direction[1])
        if dir_string not in visited:
            return_directions.append(direction)
    return return_directions

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []
    grid = []

    for line in Lines:
        print(line.strip())
        grid.append(list(line.strip()))

    values = traverse(grid)

    print(len(values))

if __name__ == '__main__':
    main()
