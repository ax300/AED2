#!/usr/bin/env python
# -- coding: utf-8 --

import csv
import sys
from Node import Node
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


nodes_index = []
all_nodes = []
nodes_freq = []
# def printNodes(all_nodes):
#     print(all_nodes)
    # for No in Nos:
    #     print(" Coord x:" + str(No.getX()) + " Coord y:" + str(No.getY()) + "\n")

# def print_freq():
#     global all_nodes

#     for node in all_nodes:
#         print (str(node.x) +  ' ' + str(node.y) + ' ' + str(node.frequentadores))

def get_node(id): # devolve no com Id procurado
    global all_nodes

    for node in all_nodes:
        if(node.id == id):
            return node

def add_nodes(lat, lon, id_frequentador):
    global all_nodes
    global nodes_index

    lat_lon = lat + lon

    if lat_lon != '00':
        if lat_lon not in nodes_index: # Insere se não tiver nenhum nó repetido (pode ser origem ou destino)
            nodes_index.append(lat_lon)
            new_node = Node(int(lat), int(lon), lat_lon)
            new_node.add_frequentadores(id_frequentador)
            all_nodes.append(new_node)
        else: # caso seja um no jah inserido
            repeated_node = get_node(lat_lon)
            repeated_node.add_frequentadores(id_frequentador)

def count_freq(): # conta quantidade de frequentadores por no
    global all_nodes
    global nodes_freq

    for node in all_nodes:
       nodes_freq.append(len(node.frequentadores))

def plot_hist():
    global nodes_index
    global nodes_freq

    plt.bar(nodes_index, nodes_freq)
    plt.ylabel('Nº Frequentadores')
    plt.xlabel('Nós')
    plt.xticks(rotation='vertical')
    plt.show()

if __name__ == '__main__':

    start = datetime.now()

    with open(r"OD_2017.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader, None) # Pula a primeira linha

        line_count = 0

        for row in csv_reader:
            # line_count += 1
            # if line_count > 50: break

            add_nodes(row[84], row[85], row[43]) # Adiciona os nós origem
            add_nodes(row[88], row[89], row[43]) # Adiciona os nós destino
    
    count_freq()
    # printNodes(all_nodes)
    # print_freq()
    end = datetime.now()
    diff = end-start
    print(diff)
    print("Plotando grafico...")
    plot_hist()