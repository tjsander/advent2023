#!/usr/bin/env python3
import re

# INPUT = 'day2/test_input.txt'
INPUT = 'day2/input.txt'

# 12 red cubes, 13 green cubes, and 14 blue cubes
RED = 12
GREEN = 13
BLUE = 14

def is_possible(i, color):
    if (color == "red" and i > RED): return False
    if (color == "green" and i > GREEN): return False
    if (color == "blue" and i > BLUE): return False
    return True

def power(pairs, color):
    val = 0
    for pair in pairs:
        if pair[1] == color and int(pair[0]) >= val:
            val = int(pair[0])
    print (color + str(val))
    return val

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    i = 0
    powers = []
    for game in Lines:
        i += 1
        qualified = 0
        pair_arr = []
        game = game.strip().split(': ')[1]
        examples = game.split('; ')
        for example in examples:
            pairs = example.split(", ")
            for pair in pairs:
                pair = pair.split(" ")
                pair_arr.append(pair)
                if not is_possible(int(pair[0]), pair[1]):
                    qualified = 1
                    # print(pair)
        if qualified == 0: values.append(i)

        red     = power(pair_arr, "red")
        green   = power(pair_arr, "green")
        blue    = power(pair_arr, "blue")
        game_power = red*green*blue
        powers.append(game_power)

    print (sum(values))
    print (sum(powers))



if __name__ == '__main__':
    main()
