#!/usr/bin/env python3
import re
import networkx as nx

INPUT = 'day25/test_input.txt'
INPUT = 'day25/input.txt'


def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()
    count = 0
    edges = []

    for line in Lines:
        print (line.strip())
        split_line = line.strip().split(": ")
        node1 = split_line[0]
        nodes_connected = split_line[1].split(" ")
        for node2 in nodes_connected:
            edges.append((node1, node2))

    G = nx.Graph()
    G.add_edges_from(edges)

    print (G)

    # njx-pbx
    # pzr-sss
    # zvk-ncm
    del_edges = [("njx","pbx"),("pzr","sss"),("zvk","sxx")]
    G.remove_edges_from(del_edges)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=False)
    print(G.number_of_nodes())

    subgraph_g = (G.subgraph(c) for c in nx.connected_components(G))
    subgraph_count = len([G.nodes for G in subgraph_g][0])
    print(subgraph_count)

    print((G.number_of_nodes()-subgraph_count) * subgraph_count)


if __name__ == '__main__':
    main()
