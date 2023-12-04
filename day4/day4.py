#!/usr/bin/env python3
import re

# INPUT = 'day4/test_input.txt'
INPUT = 'day4/input.txt'

def get_score(data):
    score = 0
    game = data.split(" | ")
    winning_nos = list(filter(None, game[0].split(" ")))
    player = list(filter(None, game[1].strip().split(" ")))
    print(winning_nos)
    print(player)
    for number in player:
        if number in winning_nos:
            print ("WINNER=" + number)
            score += 1
    if score <= 1:
        return score
    else:
        return (pow(2, score-1))


def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    score = []

    for game in Lines:
        score.append(get_score(game.split(": ")[1]))

    print(sum(score))

if __name__ == '__main__':
    main()
