#!/usr/bin/env python3
import re

INPUT = 'day15/test_input.txt'
INPUT = 'day15/input.txt'

def get_hash_values(problems):
    values = []
    for problem in problems:
        current_val = 0
        for char in problem:
            current_val += ord(char)
            current_val = current_val * 17
            current_val = current_val % 256
        values.append(current_val)
    return values

def get_label_hash_values(problems):
    boxes = []
    for x in range (256):
        boxes.append([])
    for problem in problems:
        current_val = 0
        c_string = ""
        for char in problem:
            if char == "=":
                found = False
                for box in boxes[current_val]:
                    if c_string == box[0]:
                        box[1] = problem.split("=")[1]
                        found = True
                        break
                if not found:
                    boxes[current_val].append(problem.split("="))
                break
            if char == "-":
                for box in boxes[current_val]:
                    if c_string == box[0]:
                        boxes[current_val].remove(box)
                        break
                break
            c_string += char
            current_val += ord(char)
            current_val = current_val * 17
            current_val = current_val % 256
    return boxes

# rn: 1 (box 0) * 1 (first slot) * 1 (focal length) = 1
# cm: 1 (box 0) * 2 (second slot) * 2 (focal length) = 4
# ot: 4 (box 3) * 1 (first slot) * 7 (focal length) = 28
# ab: 4 (box 3) * 2 (second slot) * 5 (focal length) = 40
# pc: 4 (box 3) * 3 (third slot) * 6 (focal length) = 72
def calc_box_values(boxes):
    values = []
    box_no = 1
    for box in boxes:
        slot_no = 1
        for slot in box:
            focal_length = int(slot[1])
            value = box_no * slot_no * focal_length
            slot_no+=1
            values.append(value)
        box_no+=1
    return values

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []
    boxes = []

    problems = []

    for line in Lines:
        problems = list(line.strip().split(","))
        print(line)

    boxes = get_label_hash_values(problems)

    values = calc_box_values(boxes)

    print(sum(values))



if __name__ == '__main__':
    main()
