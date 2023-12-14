#!/usr/bin/env python3
import re

INPUT = 'day14/test_input.txt'
INPUT = 'day14/input.txt'

def tilt_platform_north(platform):
    new_platform = []
    for x in range(0,len(platform[0])):
        for y in range (0,len(platform)):
            if platform[y][x] == "O":
                print("found one")
    return new_platform

def get_rock_loads(grid):
    loads = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if (grid[y][x] == "O"):
                loads.append(len(grid)-y)
    return loads

def get_empty_room(grid, rock_locations):
    room = []
    for location in rock_locations:
        space = 0
        for y in reversed(range(0,location[0])):
            character = grid[y][location[1]]
            if character == ".":
                space +=1
            if character == "#":
                break
        if (space > 0):
            room.append(space)
    return room

def new_coords(rock_locations, solid_rock_locations, direction, max_y, max_x):
    new_locations = []
    for rock in rock_locations:
        run_range = []
        space = 0
        new_location = []
        if direction == "east":
            run_range = range(rock[1], max_x)
        if direction == "west":
            run_range = reversed(range(0,rock[1]))
        if direction == "south":
            run_range = range(rock[0], max_y)
        if direction == "north":
            run_range = reversed(range(0,rock[0]))
        for xy in run_range:
            compare_location = []
            if direction == "north" or direction == "south":
                compare_location.append(xy)
                compare_location.append(rock[1])
            if direction == "east" or direction == "west":
                compare_location.append(rock[0])
                compare_location.append(xy)
            if compare_location in solid_rock_locations:
                break
            if compare_location not in rock_locations:
                space += 1
        if direction == "east":
            new_location = [rock[0],rock[1]+space]
        if direction == "west":
            new_location = [rock[0],rock[1]-space]
        if direction == "south":
            new_location = [rock[0]+space,rock[1]]
        if direction == "north":
            new_location = [rock[0]-space,rock[1]]
        new_locations.append(new_location)
    return new_locations

def spin(rock_locations, solid_rock_locations, max_y, max_x):
    dirs = ["north", "west", "south", "east"]
    for direction in dirs:
        rock_locations = new_coords(rock_locations, solid_rock_locations, direction, max_y, max_x)
    return rock_locations

def print_grid(rock_locations, solid_rock_locations, max_y, max_x):
    for y in range (0,max_y):
        x_str = ""
        for x in range (0,max_x):
            location = [y,x]
            if (location in rock_locations):
                x_str+="O"
            elif (location in solid_rock_locations):
                x_str+="#"
            else:
                x_str+="."
        print (x_str)
    print("\n")

def get_locations(grid, character):
    locations = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if (grid[y][x] == character):
                locations.append([y, x])
    return locations

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    distances = []

    platform = []
    for line in Lines:
        platform.append(list(line.strip()))

    loads = get_rock_loads(platform)
    rock_locations = get_locations(platform,"O")
    room = get_empty_room(platform, rock_locations)
    print(sum(loads))
    print(sum(room))
    print (sum(loads) + sum(room))

    rock_locations = get_locations(platform,"O")
    solid_rock_locations = get_locations(platform,"#")
    print_grid(rock_locations, solid_rock_locations, len(platform), len(platform[0]))

    # for i in range(0,1000000000):
    for i in range(0,1000):
        rock_locations = spin(rock_locations, solid_rock_locations, len(platform), len(platform[0]))
    print_grid(rock_locations, solid_rock_locations, len(platform), len(platform[0]))
    # rock_locations = spin(rock_locations, solid_rock_locations, len(platform), len(platform[0]))
    # print_grid(rock_locations, solid_rock_locations, len(platform), len(platform[0]))
    # rock_locations = spin(rock_locations, solid_rock_locations, len(platform), len(platform[0]))
    # print_grid(rock_locations, solid_rock_locations, len(platform), len(platform[0]))

    total = 0
    for rock in rock_locations:
        total += (len(platform) - rock[0])
    print(total)



if __name__ == '__main__':
    main()
