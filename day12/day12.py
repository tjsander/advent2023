#!/usr/bin/env python3
import re

INPUT = 'day12/test_input.txt'
# INPUT = 'day12/test_input_2.txt'
INPUT = 'day12/input.txt'
DEBUG = False
PART1 = True

def get_arrangements(springs):
    values = []
    for spring in springs:
        if DEBUG: print ("Getting possible for " + spring[0])
        # values.extend(get_broken_possible(spring[0], spring[1]))
        broken_possible = get_broken_possible(spring[0], spring[1])
        if DEBUG: print ("Beginning verification for " + spring[0])
        for possibility in broken_possible:
            broken_count = get_broken_count(possibility)
            if (broken_count == spring[1]):
                values.append(possibility)
        if DEBUG: print (len(values))
    return values

def get_broken_possible(spring, goal):
    possible = []
    question_count = spring.count("?")
    if (question_count == 0):
        possible.append(spring)
    else:
        newspr1 = spring.replace("?", "#", 1)
        newspr2 = spring.replace("?", ".", 1)
        if (question_count > 1):
            if not_already_broken(newspr1, goal):
                possible.extend(get_broken_possible(newspr1, goal))
            if not_already_broken(newspr2, goal):
                possible.extend(get_broken_possible(newspr2, goal))
        else:
            if not_already_broken(newspr1, goal):
                possible.append(newspr1)
            if not_already_broken(newspr2, goal):
                possible.append(newspr2)
    return possible

def not_already_broken(spring, count):
    new_spr = spring.split("?")[0]
    new_count = get_broken_count(new_spr)
    if (len(new_count) > len(count)):
        return False
    for i in range (0, len(new_count)):
        if (new_count[i] > count[i]):
            return False
    return True

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

    if PART1:
        for line in Lines:
            input_parsed = line.strip().split(" ")
            counts = input_parsed[1].split(",")
            counts = [int(x) for x in counts]
            springs.append([input_parsed[0].strip(), counts])
        values = get_arrangements(springs)

    if not PART1:
        springs = []
        for line in Lines:
            count_arr = []
            input_str = ""
            input_parsed = line.strip().split(" ")
            instr = input_parsed[0].strip()
            counts = input_parsed[1].split(",")
            counts = [int(x) for x in counts]

            input_str = instr
            for i in range (0,4):
                count_arr.extend(counts)
                input_str += "?"
                input_str += instr
            springs.append([input_str, count_arr])
        values = get_arrangements(springs)

    print (len(values))



if __name__ == '__main__':
    main()
