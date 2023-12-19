#!/usr/bin/env python3
import re
import time

INPUT = 'day16/test_input.txt'
INPUT = 'day16/input.txt'

def generate_grid(Lines):
    grid = []
    for line in Lines:
        grid.append(list(line.strip()))
    return grid

def ray_traverse_grid(grid, y, x, direction, reflected_values):
    values = set({})
    # if depth > 50: return values
    max_x = len(grid[0])
    max_y = len(grid)
    while y>=0 and x>=0 and y<max_y and x<max_x:
        current_location = grid[y][x]
        str_value = str(y)+ "," + str(x)
        values.add(str_value)

        if current_location != ".":
            if (current_location == "/" or current_location == "\\"):
                direction = new_direction(current_location, direction)
            if (current_location == "|" and (direction == "left" or direction == "right")):
                if str_value not in reflected_values:
                    reflected_values.add(str_value)
                    if (y-1>-1):
                        values.update(ray_traverse_grid(grid,y-1,x,"up",reflected_values))
                    if (y+1<max_y):
                        values.update(ray_traverse_grid(grid,y+1,x,"down",reflected_values))
                return values
            elif (current_location == "-" and (direction == "up" or direction == "down")):
                if str_value not in reflected_values:
                    reflected_values.add(str_value)
                    if (x-1 >=0):
                        values.update(ray_traverse_grid(grid,y,x-1,"left",reflected_values))
                    if (x+1 <max_x):
                        values.update(ray_traverse_grid(grid,y,x+1,"right",reflected_values))
                return values

        y,x = move_direction(grid,y,x,direction)
    return values

def new_direction(char_location, direction):
    new_direction = ""
    match char_location:
        case "/":
            match direction:
                case "up":
                    return "right"
                case "down":
                    return "left"
                case "right":
                    return "up"
                case "left":
                    return "down"
        case "\\":
            match direction:
                case "up":
                    return "left"
                case "down":
                    return "right"
                case "right":
                    return "down"
                case "left":
                    return "up"
    return "ERROR"

def move_direction(grid,y,x,direction):
    new_y = y
    new_x = x
    match direction:
        case "up":
            new_y-=1
        case "down":
            new_y+=1
        case "right":
            new_x+=1
        case "left":
            new_x-=1
        case _:
            print ("ERROR")
    return (new_y,new_x)

def print_grid(maxy,maxx,values):
    for y in range(maxy):
        linestr = ""
        for x in range(maxx):
            str_value = str(y)+ "," + str(x)
            if (str_value in values):
                linestr += "#"
            else:
                linestr += "."
        print (linestr)

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    for line in Lines:
        print(line.strip())

    grid = generate_grid(Lines)

    reflected_values = set({})
    values = ray_traverse_grid(grid,0,0,"right",reflected_values)

    for value in reflected_values:
        if value not in values:
            print ("WHAT THE WHAT")

    print_grid(len(grid), len(grid[0]),values)
    print(len(values))
    # 10654 too high

if __name__ == '__main__':
    main()
