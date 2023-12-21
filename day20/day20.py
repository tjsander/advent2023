#!/usr/bin/env python3
import re

INPUT = 'day20/test_input.txt'
INPUT = 'day20/input.txt'
DEBUG = False


def send_pulse(nodes):
    values = []
    return values

class Node:
    # class attribute
    name = ""
    node_list = []
    node_type = ""

    def process_signal(self, signal_type, sender_name):
        return self.node_list, self.signal_type

    # Instance attribute
    def __init__(self, name, node_type, list_input):
        self.name = name
        self.node_type = node_type
        self.node_list = list_input

# Flip-flop modules (prefix %) are either on or off; they are initially off.
# If a flip-flop module receives a high pulse, it is ignored and nothing happens.
# However, if a flip-flop module receives a low pulse, it flips between on and off.
# If it was off, it turns on and sends a high pulse. If it was on, it turns off
# and sends a low pulse.
class FlipFlop(Node):
    is_on = False

    def process_signal(self, signal_type, sender_name):
        if signal_type == "high":
            return [], ""
        elif signal_type == "low":
            return_pulse = "high"
            if self.is_on:
                return_pulse = "low"
            self.is_on = not self.is_on
            return self.node_list, return_pulse
        else:
            assert False, "this should never happen"
    pass

# Conjunction modules (prefix &) remember the type of the most recent pulse received
# from each of their connected input modules; they initially default to remembering a
# low pulse for each input. When a pulse is received, the conjunction module first
# updates its memory for that input. Then, if it remembers high pulses for all inputs,
# it sends a low pulse; otherwise, it sends a high pulse.
class Conjunction(Node):

    def process_signal(self, signal_type, sender_node):
        if sender_node not in self.input_memory:
            assert False, "Conjunction node received unknown input"

        self.input_memory[sender_node] = signal_type
        for key,value in self.input_memory.items():
            if value != "high":
                return self.node_list, "high"
        return self.node_list, "low"

    def __init__(self, name, node_type, list_input, input_nodes):
        self.name = name
        self.node_type = node_type
        self.node_list = list_input
        self.input_memory = {}
        for node in input_nodes:
            self.input_memory[node] = "low"

    pass

# There is a single broadcast module (named broadcaster). When it receives a pulse,
# it sends the same pulse to all of its destination modules.
class Broadcast(Node):
    def process_signal(self, signal_type, sender_node):
        return self.node_list, signal_type
    pass

class Module:
    nodes   = {}
    high    = 0
    low     = 0

    signals = []

    def push_button(self, no_pressed):
        assert len(self.signals) == 0, "button error, should not be signals on stack"
        if DEBUG:
            print ("\n===BUTTON=== ", no_pressed+1)
        self.signals.insert(0,["broadcaster","low","BUTTON"])
        while len(self.signals) > 0:
            button_signal = self.signals.pop(0)
            self.send_signal(button_signal[0],button_signal[1],button_signal[2])
            if DEBUG:
                print("%s =%s> %s" % (button_signal[2],button_signal[1],button_signal[0]))
        return True

    def send_signal(self, node_name, signal_type, sender_name):
        if signal_type == "low":
            self.low +=1
        elif signal_type == "high":
            self.high +=1
        else:
            print ("ERROR")

        if node_name not in self.nodes:
            return False
            #PART 2: RX HERE

        Node_obj = self.nodes[node_name]

        signal_nodes, n_signal_type = Node_obj.process_signal(signal_type, sender_name)

        for next_node in signal_nodes:
            self.signals.append([next_node,n_signal_type,node_name])

        return True

    def __str__(self):
        return "Module high=%s, low=%s, prod=%s" % (self.low, self.high, self.low*self.high)

    def init_nodes(self, nodes):
        for key, value in nodes.items():
            node_type = value[0]
            if node_type == "&":
                source_node_arr = []
                for new_k, new_v in nodes.items():
                    if key in new_v[1]:
                        source_node_arr.append(new_k)
                self.nodes[key] = Conjunction(key,node_type,value[1],source_node_arr)
            elif node_type == "%":
                self.nodes[key] = FlipFlop(key,node_type,value[1])
            else:
                self.nodes[key] = Broadcast(key,node_type,value[1])
        return True

    # Instance attribute
    def __init__(self, nodes):
        self.init_nodes(nodes)
        print("Initialized")

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    values = []
    nodes = {}

    for line in Lines:
        print (line.strip())
        value = line.strip().split(" -> ")
        # values.append(value)
        node_type = ">"
        node_name = value[0]
        if node_name[0] == "&":
            node_name = value[0][1:]
            node_type = "&"
        elif node_name[0] == "%":
            node_name = value[0][1:]
            node_type = "%"
        nodes[node_name] = [str(value[1]).split(", ")]
        nodes[node_name].insert(0,node_type)
    print (nodes)

    ModulePart1 = Module(nodes)
    for i in range(0,1000000000000):
        ModulePart1.push_button(i)

    print(ModulePart1)


if __name__ == '__main__':
    main()
