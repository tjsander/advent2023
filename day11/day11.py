#!/usr/bin/env python3
import re

# INPUT = 'day11/test_input.txt'
INPUT = 'day11/input.txt'



def expand_galaxy(grid):
    expand_x = list(range(0,len(grid[0])))
    expand_y = list(range(0,len(grid)))
    new_galaxy = []

    stars = get_stars(grid)
    for star in stars:
        y, x = star
        if x in expand_x: expand_x.remove(x)
        if y in expand_y: expand_y.remove(y)

    for y in range(0,len(grid)):
        x_str = ""
        for x in range(0,len(grid[0])):
            if (x in expand_x):
                x_str += grid[y][x]
            x_str += grid[y][x]
        new_galaxy.append(x_str)
        if (y in expand_y):
            new_galaxy.append(x_str)
    return new_galaxy

def get_stars(grid):
    stars = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if (grid[y][x] == "#"):
                stars.append((y,x))
    return stars

def get_distances(stars):
    distances = []
    for star1 in stars:
        for star2 in stars:
            if star1 != star2:
                distance = abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])
                distances.append(distance)
    return distances

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    distances = []

    grid = []
    for line in Lines:
        grid.append(list(line.strip()))
        print (line.strip())

    grid = expand_galaxy(grid)

    stars = get_stars(grid)
    print (stars)
    distances = get_distances(stars)
    print (distances)
    print (sum(distances)/2)



if __name__ == '__main__':
    main()
