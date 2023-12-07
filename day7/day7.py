#!/usr/bin/env python3
import re

# INPUT = 'day7/test_input.txt'
INPUT = 'day7/input.txt'

def score_type(hand_str):
    occurrences = []
    hand = list(hand_str)
    hand.sort()
    duplicates = 1
    for i in range (0,4):
        if hand[i] != hand[i+1]:
            occurrences.append(duplicates)
            duplicates = 1
        else:
            duplicates += 1
    occurrences.append(duplicates)
    occurrences.sort(reverse=True)

    if (occurrences[0] == 5): return 7
    if (occurrences[0] == 4): return 6
    if (occurrences[0] == 3):
        if (occurrences[1] == 2): return 5
        if (occurrences[1] == 1): return 4
    if (occurrences[0] == 2):
        if (occurrences[1] == 2): return 3
        if (occurrences[1] == 1): return 2
    if (occurrences[0] == 1): return 1
    return 1

def part1(hands):
    new_hands = []
    for hand in hands:
        new_hands.append((score_type(hand[0]), hand[0], hand[1]))

    new_hands.sort()
    return new_hands


def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    hands = []

    for line in Lines:
        line = line.replace("T", "B")
        line = line.replace("J", "C")
        line = line.replace("Q", "D")
        line = line.replace("K", "E")
        line = line.replace("A", "F")
        line = line.split(" ")
        hands.append([line[0], int(line[1]), 0])

    pt1_score = 0
    pt1_sorted = part1(hands)
    for i in range(0, len(pt1_sorted)):
        pt1_score += pt1_sorted[i][2] * (i+1)

    # Example = 6440
    print (pt1_score)


if __name__ == '__main__':
    main()
