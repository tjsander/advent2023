#!/usr/bin/env python3
import re
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
                    # print (str(seed) + " in " + str(line[1]) + ":" + str(line[2]))
                    location = seed - line[1] + line[0]
            seed = location
        locations.append(location)
    return locations

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

if __name__ == '__main__':
    main()
