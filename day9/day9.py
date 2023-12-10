#!/usr/bin/env python3
import re
import numpy

# INPUT = 'day9/test_input.txt'
INPUT = 'day9/input.txt'

def get_diffs(history):
    new_hist = []
    for i in range (0, len(history) - 1):
        new_hist.append(history[i+1] - history[i])
        i+=1
    return new_hist

def get_next_sequence(new_history):
    sum = 0
    for history in new_history:
        sum += history[-1]
    return sum

def get_first_sequence(new_history):
    # values = []
    value = 0
    for i in reversed(range(0,len(new_history))):
        value = (new_history[i][0] - value)
        # values.append(new_history[i-1][0] - new_history[i][0])
    return value

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []
    histories = []

    for line in Lines:
        history = line.strip().split(" ")
        history = [int(i) for i in history]
        histories.append(history)
        print(history)

    new_histories = []
    for history in histories:
        current_history = history
        new_history = []
        new_history.append(current_history)
        while len(set(current_history)) != 1:
            current_history = get_diffs(current_history)
            new_history.append(current_history)

        new_histories.append(new_history)
        # print (new_histories)

    i = 0
    for new_history in new_histories:
        i+=get_next_sequence(new_history)
    print(i)

    i = 0
    for new_history in new_histories:
        i+=get_first_sequence(new_history)
    print(i)


if __name__ == '__main__':
    main()
