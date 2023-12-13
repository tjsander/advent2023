#!/usr/bin/env python3
import re

# INPUT = 'day11/test_input.txt'
INPUT = 'day11/input.txt'

SCALE = 1000000

def expand_galaxy(grid):
    new_galaxy = []
    expand_y, expand_x = expand_galaxy_lists(grid)
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

def expand_galaxy_lists(grid):
    expand_x = list(range(0,len(grid[0])))
    expand_y = list(range(0,len(grid)))

    stars = get_stars(grid)
    for star in stars:
        y, x = star
        if x in expand_x: expand_x.remove(x)
        if y in expand_y: expand_y.remove(y)

    return expand_y, expand_x

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

def get_distances_expanded(stars, expand_y, expand_x):
    distances = []
    for star1 in stars:
        for star2 in stars:
            if star1 != star2:
                distance = 0
                if (star1[0] < star2[0]):
                    for y in range(star1[0], star2[0]):
                        if y in expand_y:
                            distance += SCALE
                        else:
                            distance += 1
                else:
                    for y in range(star2[0], star1[0]):
                        if y in expand_y:
                            distance += SCALE
                        else:
                            distance += 1
                if (star1[1] < star2[1]):
                    for x in range(star1[1], star2[1]):
                        if x in expand_x:
                            distance += SCALE
                        else:
                            distance += 1
                else:
                    for x in range(star2[1], star1[1]):
                        if x in expand_x:
                            distance += SCALE
                        else:
                            distance += 1
                # distance += abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])
                distances.append(distance)
    return distances

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    distances = []

    galaxy = []
    for line in Lines:
        galaxy.append(list(line.strip()))
        print (line.strip())

    expanded_galaxy = expand_galaxy(galaxy)

    stars = get_stars(expanded_galaxy)
    # print (stars)
    distances = get_distances(stars)
    print (distances)
    print (sum(distances)/2)

    # PART 2
    stars = get_stars(galaxy)
    expand_y, expand_x = expand_galaxy_lists(galaxy)
    distances = get_distances_expanded(stars, expand_y, expand_x)
    print (distances)
    print (sum(distances)/2)
    # example x10 = 1030



if __name__ == '__main__':
    main()
