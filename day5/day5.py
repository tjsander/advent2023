#!/usr/bin/env python3
import re
import sys
from operator import itemgetter

# INPUT = 'day5/test_input.txt'
INPUT = 'day5/input.txt'

def get_maps(Lines):
    maps = []
    map_add = []
    for line in Lines[1:]:
        if (line == "\n"):
            map_add.sort(key=lambda x:x[1])
            maps.append(map_add)
            map_add = []
        elif (line[0].isalpha()):
            print(line)
        else:
            line = line.strip().split(" ")
            res = [eval(i) for i in line]
            map_add.append(res)
    map_add.sort(key=lambda x: x[1])
    sorted(map_add, key=itemgetter(1))
    maps.append(map_add)
    return maps

def parse_locations(seeds, maps):
    locations = []
    for seed in seeds:
        location = seed
        for seed_map in maps:
            seed = location
            for line in seed_map:
                # print(line)
                if seed in range(line[1],line[1]+line[2]):
                    location = seed - line[1] + line[0]
            seed = location
        locations.append(location)
    return locations

def location_to_seed(location, maps):
    # seed = location
    for seed_map in reversed(maps):
        l1 = location
        for line in seed_map:
            if l1 in range(line[0],line[0]+line[2]):
                location = location - line[0] + line[1]
    return location

def in_seed_ranges(seed, seed_ranges):
    for seed_range in seed_ranges:
        if (seed >= seed_range[0] and seed < seed_range[0] + seed_range[1]):
            return True
    return False

def find_min_location(seeds, maps, seed_ranges):
    seed_found = []
    min_location = max(seeds)
    for i in range (0, min_location):
        new_seed = location_to_seed(i, maps)
        if in_seed_ranges(new_seed, seed_ranges):
            return i
    return sys.maxsize

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    scores = []
    number = 0

    seeds = Lines[0].split(": ")[1].strip().split(" ")
    seeds = [eval(i) for i in seeds]

    maps = get_maps(Lines[2:])
    locations = parse_locations(seeds, maps)
    print (min(locations))

    seed_ranges = []
    for x in range (0, int(len(seeds)/2)):
        seed_ranges.append([seeds[x*2], seeds[x*2+1]])

    print (find_min_location(seeds, maps, seed_ranges))

if __name__ == '__main__':
    main()
