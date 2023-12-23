#!/usr/bin/env python3
import re

INPUT = 'day22/test_input.txt'
INPUT = 'day22/input.txt'
DEBUG = False

class Brick():
    z_floor = 1
    height = 1
    length = 1
    width = 1
    xyz0 = []
    xyz1 = []
    x_range = []
    y_range = []
    z_range = []

    def drop(self):
        self.z_floor -= 1
        self.z_range = range(self.z_floor,self.z_floor+self.height)
        if self.z_floor < 2:
            return True
        return False

    def get_z(self):
        return 1

    def __str__(self):
        str_grid = ""
        for y in range(0,10):
            for x in range(0,10):
                if x in range(self.xyz0[1],self.xyz1[1] + 1) \
                    and y in range(self.xyz0[0],self.xyz1[0] +1):
                    str_grid += "#"
                else:
                    str_grid += "."
            str_grid += "\n"
        if DEBUG:
            return "brick_" + str(self.z_floor) + "_h" + str(self.height) + "\n" + str_grid
        return "brick_" + str(self.z_floor) + "_h" + str(self.height)

    def __init__(self, brick_line):
        split_line = brick_line.strip().split("~")
        xyz0 = split_line[0].split(",")
        xyz1 = split_line[1].split(",")

        self.xyz0 = res = [eval(i) for i in xyz0]
        self.xyz1 = res = [eval(i) for i in xyz1]
        self.z_floor = int(xyz0[2])
        self.height = abs(self.xyz0[2] - self.xyz1[2]) +1
        self.width = abs(self.xyz0[1] - self.xyz1[1]) +1
        self.length = abs(self.xyz0[0] - self.xyz1[0]) +1

        self.x_range = range(self.xyz0[0],self.xyz1[0]+1)
        self.y_range = range(self.xyz0[1],self.xyz1[1]+1)
        self.z_range = range(self.xyz0[2],self.xyz1[2]+1)
        return
    pass

def brick_rests_on_brick(Brick, Brick_comp):
    if Brick.z_range[0] == Brick_comp.z_range[-1]+1:
        for x in Brick.x_range:
            if x in Brick_comp.x_range:
                for y in Brick.y_range:
                    if y in Brick_comp.y_range:
                        if DEBUG: print (str(Brick) + " rests on " + str(Brick_comp))
                        return True
    return False

def drop_all_bricks(Bricks):
    for brick1 in Bricks:
        if brick1.z_floor > 1:
            drop_brick(brick1, Bricks)
    return Bricks

def drop_brick(brick1, Bricks):
    stopped = False
    while not stopped:
        if brick1.z_floor <= 1: return True
        for brick2 in Bricks:
            if (brick1 != brick2) and brick_rests_on_brick(brick1, brick2):
                return True
        if DEBUG: print(str(brick1) + " dropping1")
        brick1.drop()
    return True

def can_drop_brick(brick1, Bricks):
    for brick2 in Bricks:
        if (brick1 != brick2):
            if brick1.z_floor == 1:
                return False
            if brick_rests_on_brick(brick1, brick2):
                return False
        # return False
    return True

def bricks_can_drop(Bricks):
    for brick in Bricks:
        if (can_drop_brick(brick, Bricks)):
            return True
    return False

def break_bricks(Bricks):
    breakable = []
    for brick in Bricks:
        new_bricks = Bricks.copy()
        new_bricks.remove(brick)
        if (not bricks_can_drop(new_bricks)):
            breakable.append(brick)
    return breakable


def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    bricks = []

    for line in Lines:
        bricks.append(Brick(line))

    z_max = 0
    for brick in bricks:
        brick_z = brick.get_z()
        if brick_z > z_max:
            z_max = brick_z

    # bricks.append(Brick("0,0,0~9,9,0"))

    # print (bricks)
    # for brick in bricks:
    #     print (brick)
    new_list = sorted(bricks, key=lambda x: x.z_floor)
    print("sorted")
    new_list = drop_all_bricks(new_list)
    print("dropped")
    # for brick in new_list:
    #     print (brick)

    breakable_bricks = break_bricks(new_list)
    print("broken")
    print (len(breakable_bricks))


if __name__ == '__main__':
    main()
