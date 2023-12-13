#!/usr/bin/env python3
import re

INPUT = 'day12/test_input.txt'
# INPUT = 'day12/test_input_2.txt'
INPUT = 'day12/input.txt'

def get_arrangements(springs):
    values = []
    for spring in springs:
        broken_possible = get_broken_possible(spring[0])
        for possibility in broken_possible:
            broken_count = get_broken_count(possibility)
            if (broken_count == spring[1]):
                values.append(possibility)
    return values

def get_broken_possible(spring):
    possible = []
    count = spring.count("?")
    if (count == 0):
        possible.append(spring)
    else:
        newspr1 = spring.replace("?", "#", 1)
        newspr2 = spring.replace("?", ".", 1)
        if (count > 1):
            possible.extend(get_broken_possible(newspr1))
            possible.extend(get_broken_possible(newspr2))
        else:
            possible.append(newspr1)
            possible.append(newspr2)
    return possible

# def build_possibilities(spring, count):
#     possibilities = []


def get_broken_count(spring):
    broken = []
    group = 0
    for i in range(0, len(spring)):
        sp = spring[i]
        if (sp == "#"):
            group += 1
        else:
            if (group > 0):
                broken.append(group)
                group = 0
    if (group > 0):
        broken.append(group)
        group = 0
    return broken

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    springs = []
    values = []

    for line in Lines:
        input_parsed = line.strip().split(" ")
        counts = input_parsed[1].split(",")
        counts = [int(x) for x in counts]
        springs.append([input_parsed[0], counts])

    values = get_arrangements(springs)

    # print (values)
    print (len(values))



if __name__ == '__main__':
    main()
