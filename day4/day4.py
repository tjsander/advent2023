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
    return score

def game1(scores):
    total = 0
    for score in scores:
        if score <= 1:
            total += score
        else:
            total += pow(2, score-1)
    return total

def game2(scores, Lines):
    total = 0
    game = 0

    mults = [1] * len(scores)

    for score in scores:
        for y in range (0,mults[game]):
            for x in range (game+1,game+score+1):
                if (x < len(scores)):
                    mults[x] += 1
                else:
                    break
        game += 1
    return sum(mults)

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    scores = []
    number = 0

    for game in Lines:
        scores.append(get_score(game.split(": ")[1]))
        number += 1

    print(game1(scores))
    print(game2(scores, Lines))

if __name__ == '__main__':
    main()
