import csv
import sys
# import numpy
from Node import Node
import json

nodes_index_origem = []
nodes_index_dest = []
all_nodes = []


def printNodes(all_nodes):
    print(len(all_nodes))
    # for No in Nos:
    #     print(" Coord x:" + str(No.getX()) + " Coord y:" + str(No.getY()) + "\n")

def add_nodes(lat, lon, nodes_index, id):
    global all_nodes

    lat_lon = lat + lon
    if lat_lon not in nodes_index:
        nodes_index.append(lat_lon)
        new_node = Node(int(lat), int(lon))
        all_nodes.append(new_node)
        new_node.add_frequentadores(id)
    # else:
    #     new_node.add_frequentadores(id)


if __name__ == '__main__':

    with open(r"OD_2017.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader, None)
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count > 5: break

            add_nodes(row[84], row[85], nodes_index_origem, row[43])
            add_nodes(row[88], row[89], nodes_index_dest, row[43])

    printNodes(all_nodes)