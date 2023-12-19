#!/usr/bin/env python3
import re

INPUT = 'day19/test_input.txt'
# INPUT = 'day19/input.txt'

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

def process_ranges(range_set, work_id, workflows):
    list_ranges = []
    flows = workflows[work_id]
    for flow in flows:
        if (flow.find(":") != -1):
            # Return two range sets if(
            pass_range, fail_range = parse_eval_range(range_set, flow)
            result = flow.split(":")[1]
            if result == "A":
                list_ranges.extend([pass_range])
                return list_ranges
            if result == "R":
                return list_ranges
            if (len(pass_range) > 0):
                list_ranges.extend(process_ranges(pass_range, result, workflows))
                return list_ranges
        else:
            if flow == "A":
                list_ranges.extend(range_set)
                return list_ranges
            if flow == "R":
                return list_ranges
            list_ranges.extend(process_ranges(range_set, flow, workflows))
            return list_ranges
    return list_ranges

def parse_eval_range(range_eval, flow):
    split_f =""
    less_than = False
    if flow.find("<") != -1:
        split_f = flow.split(":")[0].split("<")
        less_than = True
    else:
         split_f = flow.split(":")[0].split(">")

    comparison_int = int(split_f[1])

    top_range    = range_eval.copy()
    top_range[split_f[0]] = top_range[split_f[0]][:comparison_int]

    bottom_range = range_eval.copy()
    bottom_range[split_f[0]] = bottom_range[split_f[0]][comparison_int:]

    if len(bottom_range[split_f[0]]) == 0:
        bottom_range = []
    if len(top_range[split_f[0]]) == 0:
        top_range = []

    if (less_than):
        return (top_range, bottom_range)
    else:
        return (bottom_range, top_range)


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

    ranges = {"x":range(0,4000),"m":range(0,4000),"a":range(0,4000),"s":range(0,4000)}
    range_results = []
    # range_1 = ranges["x"][2000:]
    # range_2 = ranges["x"][:2000]
    # ranges["x"] = range_2
    # range_2 = range_2[:50]
    range_results = process_ranges(ranges,"in", workflows)
    print (range_results)

    range_totals = []
    for result in range_results:
        range_total = 1
        for key, value in result.items():
            range_total = range_total * len(value)
        range_totals.append(range_total)
    print(sum(range_totals))


if __name__ == '__main__':
    main()
