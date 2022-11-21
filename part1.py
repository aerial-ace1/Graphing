import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from utils import is_cycle 

def kruskal():
    '''
    Implement Kruskal's Algo
    '''
    
    

def prim(edge_list,node_num):
    '''
    Implement Prim's Algo
    '''

def runner():
    '''
    Function to run the algorithms
    '''
    node_num = int(input("Enter Number of Nodes:"))
    edge_num = int(input("Enter Number of Edges:"))

    # Check for validity of edges
    if(edge_num>(node_num*(node_num-1)/2)):
        print("Too many Nodes!!")
        exit(1)

    # Generating edgelist and adjacency matrix
    edge_list = []
    adj_list = np.zeros((node_num,node_num),"int8")

    for i in range(edge_num):

        # edge_prop --> [start,end.weight]
        edge_prop = []

        start = int(input("Starting Node of Edge:"))
        end = int(input("Ending Node of Edge:"))

        if start < node_num and end < node_num:
            if start > end :
                edge_prop.append(end)
                edge_prop.append(start)
            else:
                edge_prop.append(start)
                edge_prop.append(end)
        else:
            print("Nodes not in Index")
            exit(2)

        # Weight of node
        edge_wght = int(input("Weight of Edge:"))
        
        # Add edge to edge_list
        edge_prop.append(edge_wght)
        edge_list.append(edge_prop)

        # Add edge to adj_list
        adj_list[start][end] = edge_wght
        adj_list[end][start] = edge_wght
    
    # Sorting edge_list in ascending order based on weight
    edge_list = sorted(edge_list, key = lambda x: x[2])

    # Kruskal's Algo
    kruskal()

    # Prim's Algo
    prim(edge_list,node_num)

    # Networkx Graphing
    # TODO

    print(edge_list)
    print(adj_list)

# runner()
# [[1, 2, 2], [2, 4, 2], [2, 3, 3], [3, 5, 3], [4, 5, 3], [0, 1, 4], [0, 2, 4], [2, 5, 4]]
# list = [[1, 2, 2], [2, 4, 2], [2, 3, 3], [3, 5, 3]]
# print(is_cycle(list,6))


