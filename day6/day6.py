#!/usr/bin/env python3
import re
import math

# INPUT = 'day6/test_input.txt'
# INPUT = 'day6/input.txt'
# INPUT = 'day6/test_input_2.txt'
INPUT = 'day6/input_2.txt'

def part_1(time, distance):
    wins = 0
    for i in range (1,time):
        if (i * (time-i) > distance):
            wins += 1
    return wins

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    values = []


    times = Lines[0].strip().split(": ")[1].split(" ")
    distances = Lines[1].strip().split(": ")[1].split(" ")

    times       = list(filter(None, times))
    distances   = list(filter(None, distances))

    for x in range(0,len(times)):
        values.append(part_1(int(times[x]), int(distances[x])))

    print (values)
    # Example: 288 (4 * 8 * 9)
    print (math.prod(values))


if __name__ == '__main__':
    main()
