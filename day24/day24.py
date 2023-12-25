#!/usr/bin/env python3
import re

INPUT = 'day24/test_input.txt'
INPUT = 'day24/input.txt'

def calculate_collisions(hailstones, velocities):
    collisions = []
    for a in range(0,len(hailstones)):
        for b in range (a+1,len(hailstones)):
            if stones_collide_in_range(hailstones, velocities, a, b):
                collisions.append(str(a) + "***" + str(b))
    return collisions

def stones_collide_in_range(hailstones, velocities, a, b):
    range_low = 200000000000000
    range_high = 400000000000000
    if INPUT == 'day24/test_input.txt':
        range_low = 7
        range_high = 27
    stone_a = hailstones[a]
    stone_b = hailstones[b]
    velocity_a = velocities[a]
    velocity_b = velocities[b]

    slope_a = velocity_a[1] / velocity_a[0]
    f_x_a = -1*((stone_a[0] * slope_a) - stone_a[1])

    slope_b = velocity_b[1] / velocity_b[0]
    f_x_b = -1* ((stone_b[0] * slope_b) - stone_b[1])

    # Parallel
    if slope_a - slope_b == 0:
        return False

    x_intercept  =  (f_x_b-f_x_a) / (slope_a - slope_b)
    y_intercept  = x_intercept * slope_a + f_x_a

    if (x_intercept >= range_low and x_intercept <= range_high \
        and y_intercept >= range_low and y_intercept <= range_high):
        if in_the_future(stone_a[0], stone_a[1], x_intercept, y_intercept, velocity_a[0], velocity_a[1]):
            return in_the_future(stone_b[0], stone_b[1], x_intercept, y_intercept, velocity_b[0], velocity_b[1])
        else:
            return False
    else:
        return False

def in_the_future(x1, y1, x2, y2, x_vel, y_vel):
    if y_vel > 0:
        return y2 > y1
    else:
        return y2 < y1

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()

    hailstones = []
    velocities = []

    for line in Lines:
        stone_line = line.strip().split(" @ ")
        hailstones.append([int(x) for x in stone_line[0].split(", ")])
        velocities.append([int(x) for x in stone_line[1].split(", ")])
    print (hailstones)
    print (velocities)

    print (len(calculate_collisions(hailstones, velocities)))




if __name__ == '__main__':
    main()
