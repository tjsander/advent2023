#!/usr/bin/env python3
import re

INPUT = 'day19/test_input.txt'
INPUT = 'day19/input.txt'

def custom_sum(parts):
    values = []
    for part in parts:
        total = 0
        for key, value in part.items():
            total+=value
        values.append(total)
    return values

def process_parts(parts, workflows):
    values = []
    for part in parts:
        if(process_rules(part, "in", workflows)):
            values.append(part)
    return values

def process_rules(part, work_id, workflows):
    flows = workflows[work_id]
    for flow in flows:
        if (flow.find(":") != -1):
            if(parse_eval(part, flow)):
                result = flow.split(":")[1]
                if result == "A": return True
                if result == "R": return False
                return process_rules(part, result, workflows)
            # Else do nothing and let next flow happen
        else:
            if flow == "A": return True
            if flow == "R": return False
            return process_rules(part, flow, workflows)
    return False

def parse_eval(part, flow):
    split_f =""
    less_than = False
    if flow.find("<") != -1:
        split_f = flow.split(":")[0].split("<")
        less_than = True
    else:
         split_f = flow.split(":")[0].split(">")
    if (less_than):
        return (part[split_f[0]] < int(split_f[1]))
    else:
        return (part[split_f[0]] > int(split_f[1]))


def process_ranges(ranges, workflows):
    compiled_ranges = []
    # compiled_ranges.extend()
    return compiled_ranges

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []

    workflows = {}
    parts = []

    workflow_bool = True
    for line in Lines:
        if not (workflow_bool):
            part = {}
            part_disc = line.strip()[1:-1].split(",")
            for disc in part_disc:
                split = disc.split("=")
                part[split[0]] = int(split[1])
            parts.append(part)
        if line == "\n":
            workflow_bool = False
        if (workflow_bool):
            split = line.strip().split("{")
            workflows[split[0]] = split[1][:-1].split(",")
            # workflows.append(line.strip())


    values = process_parts(parts, workflows)

    print (values)
    print (sum(custom_sum(values)))

    ranges = {"x":[0,4000],"m":[0,4000],"a":[0,4000],"s":[0,4000]}
    range_results = []
    range_results = process_ranges(ranges, workflows)
    print (range_results)


if __name__ == '__main__':
    main()
