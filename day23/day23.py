#!/usr/bin/env python3
import re

INPUT = 'day23/test_input.txt'
# INPUT = 'day23/input.txt'

# Longest path problem

def traverse(Grid, positions):
    start = positions[-1]
    end = (len(Grid)-1 , len(Grid[0])-2)

    position = start
    while position != end:
        next_step_set = next_steps(Grid, position)
        branch = 0
        for step in next_step_set:
            if step not in positions:
                branch +=1
                # if branch > 1:
                #     print("branch")
                    # positions[-1][-1] = step
                    # positions.append(traverse(Grid,positions))
                # else:
                position = step
                positions.append(position)
                break
    return positions

def print_grid(grid, steps):
    line_str = ""
    for y in range(0,len(grid)):
        for x in range(0,len(grid[0])):
            if (y,x) in steps:
                line_str += "O"
            else:
                line_str += grid[y][x]
        line_str += "\n"
    return line_str

def next_steps(grid, step):
    possible_steps = []
    # step_arr = list(step.split(","))
    # y = int(step_arr[0])
    # x = int(step_arr[1])
    y = step[0]
    x = step[1]
    if (y+1 < len(grid)):
        step = (y+1,x)
        space = grid[step[0]][step[1]]
        if space != "^" and space != "#":
            possible_steps.append(step)
    if (y-1 >= 0):
        step = (y-1,x)
        space = grid[step[0]][step[1]]
        if space != "v" and space != "#":
            possible_steps.append(step)
    if (x+1 < len(grid[0])):
        step = (y,x+1)
        space = grid[step[0]][step[1]]
        if space != "<" and space != "#":
            possible_steps.append(step)
    if (x-1 >= 0):
        step = (y,x-1)
        space = grid[step[0]][step[1]]
        if space != ">" and space != "#":
            possible_steps.append(step)
    return possible_steps

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    grid = []
    values = []

    for line in Lines:
        grid.append(list(line.strip()))

    positions = [(0,1)]
    values = traverse(grid, positions)

    print (print_grid(grid,positions))


if __name__ == '__main__':
    main()
