#!/usr/bin/env python3
import re
import numpy

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

            elif result == "R":

                if (len(pass_range) > 0):
                    range_set = pass_range
            else:
                if (len(pass_range) > 0):
                    list_ranges.extend(process_ranges(pass_range, result, workflows))

                if (len(fail_range) > 0):
                    range_set = fail_range
        else:
            if flow == "A":
                list_ranges.extend([range_set])
            elif flow != "R":
                list_ranges.extend(process_ranges(range_set, flow, workflows))
    return list_ranges

def parse_eval_range(range_eval, flow):
    split_f =""
    less_than = False
    if flow.find("<") != -1:
        split_f = flow.split(":")[0].split("<")
        less_than = True
    else:
         split_f = flow.split(":")[0].split(">")

    character = split_f[0]
    comparison_int = int(split_f[1])

    top_range    = range_eval.copy()
    bottom_range = range_eval.copy()

    lower_range = top_range[split_f[0]][0]

    if (lower_range > 0):
        comparison_int -= lower_range
    ### PROBLEM HERE: Slicing was not occuring at the number specified,
    # It is happening at that INDEX. ie - 2770 is out of range 1351:4000

    if comparison_int > 0:
        top_range[split_f[0]] = top_range[character][:comparison_int]
        bottom_range[character] = bottom_range[character][comparison_int:]
    else:
        print("ERROR")

    if len(bottom_range[character]) == 0:
        bottom_range = []
    if len(top_range[character]) == 0:
        top_range = []

    if (less_than):
        return (top_range, bottom_range)
    else:
        return (bottom_range, top_range)

def get_overlapping_range_total(ranges_a, ranges_b):
    totals = []
    keys = ["x","m","a","s"]
    # for key in ranges_a.items():
    for key in keys:
        total = len(set(ranges_a[key]) & set(ranges_b[key]))
        totals.append(total)
    return numpy.prod(totals)

def get_unique_overlapping_range_totals(range_sets):
    full_sets = []
    keys = ["x","m","a","s"]

    totals = []
    new_range_sets = []

    for i in range(0,len(range_sets)):

        range_set_copy = range_sets[i].copy()

        for j in range(i+1,len(range_sets)):
            overlaps = []

            for key in keys:
                overlaps.append(len(set(range_sets[i][key]) & set(range_sets[j][key])))
            product = numpy.prod(overlaps)
            # totals.append(product)
            if (product > 0):
                amended = False
                for key in keys:
                    # If overlaps actually exist
                    # if (len(set(range_set_copy[key]) - set(range_sets[j][key]))>0):
                    range_set_copy[key] = set(range_set_copy[key]) - set(range_sets[j][key])
                        # amended = True
                # if not (amended):
                #     for key in keys:
                #         range_set_copy[key] = set(range_set_copy[key]) - set(range_sets[j][key])
                        # range_set_copy[key] = {}
        new_range_sets.append(range_set_copy)

    range_totals = []
    for result in new_range_sets:
        range_total = 1
        for key, value in result.items():
            range_total = range_total * len(value)
        range_totals.append(range_total)

    print(sum(range_totals))
    return new_range_sets

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
    range_results = process_ranges(ranges,"in", workflows)
    print (range_results)

    range_totals = []
    for result in range_results:
        range_total = 1
        for key, value in result.items():
            range_total = range_total * len(value)
        range_totals.append(range_total)

    #NEED TO FIND A WAY TO REMOVE DUPES....
    print(sum(range_totals))

    dupe_totals = get_unique_overlapping_range_totals(range_results)


if __name__ == '__main__':
    main()
