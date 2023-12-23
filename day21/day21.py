#!/usr/bin/env python3
import re

INPUT = 'day21/test_input.txt'
INPUT = 'day21/input.txt'

def step(grid, steps):
    new_steps = set({})
    for y in range (0, len(grid)):
        for x in range (0, len(grid[0])):
            if str(y)+","+str(x) in steps:
                new_step= next_steps(grid,(y,x))
                new_steps.update(new_step)
    return new_steps

def next_steps(grid, step):
    possible_steps = []
    return_steps = set({})
    # step_arr = list(step.split(","))
    y = step[0]
    x = step[1]
    if (y+1 < len(grid)):
        possible_steps.append((y+1,x))
    if (y-1 >= 0):
        possible_steps.append((y-1,x))
    if (x+1 < len(grid[0])):
        possible_steps.append((y,x+1))
    if (x-1 >= 0):
        possible_steps.append((y,x-1))
    for step in possible_steps:
        if grid[step[0]][step[1]] != "#":
            return_steps.add(str(step[0]) + "," + str(step[1]))
    return return_steps


def print_grid(grid, steps):
    line_str = ""
    for y in range(0,len(grid)):
        for x in range(0,len(grid[0])):
            if str(y)+","+str(x) in steps:
                line_str += "O"
            else:
                line_str += grid[y][x]
        line_str += "\n"
    return line_str

def find_start(grid):

    for y in range(0,len(grid)):
        for x in range(0,len(grid[0])):
            if grid[y][x] == "S":
                return [str(y)+","+str(x)]

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    steps = []

    grid = []
    for line in Lines:
        print (line.strip())
        grid.append(list(line.strip()))

    steps = find_start(grid)
    for i in range (0,64):
        steps = step(grid, steps)

    print (steps)
    print (len(steps))
    grid_str = print_grid(grid, steps)
    print (grid_str)
    print (grid_str.count("O"))

    # 1255 too low

if __name__ == '__main__':
    main()
