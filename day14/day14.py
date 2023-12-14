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
        print (line.strip())

    # platform = tilt_platform_north(platform)
    loads = get_rock_loads(platform)
    rock_locations = get_locations(platform,"O")
    room = get_empty_room(platform, rock_locations)

    print(sum(loads))
    print(sum(room))
    print (sum(loads) + sum(room))


if __name__ == '__main__':
    main()
