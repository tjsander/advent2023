#!/usr/bin/env python3
import re

INPUT = 'day7/test_input.txt'
INPUT = 'day7/input.txt'

def score_type_joker(hand_str):

    # With Stringsub hax jokers are now 1
    occurrences = []
    hand = list(hand_str)
    hand.sort()

    wildcards = hand.count('1')
    if (wildcards > 0):
        for i in range (0,wildcards):
            hand.remove('1')
    duplicates = 1
    for i in range (0,len(hand)-1):
        if hand[i] != hand[i+1]:
            occurrences.append(duplicates)
            duplicates = 1
        else:
            duplicates += 1
    occurrences.append(duplicates)
    occurrences.sort(reverse=True)
    occurrences[0] += wildcards

    if (occurrences[0] >= 5): return 7
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
        new_hands.append((score_type_joker(hand[0]), hand[0], hand[1]))

    new_hands.sort()
    return new_hands


def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    hands = []
    pt2 = True

    for line in Lines:
        line = line.replace("T", "B")
        if (pt2):
            line = line.replace("J", "1")
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
    # Example pt2 = 5905

    print (pt1_score)


if __name__ == '__main__':
    main()
