import numpy as np
from part1 import prim
from utils import dfs,plot

def approxHamil(edge_list,node_num,adj_mat):
    '''
    Approximate Hamiltonian's Cycle Algo
    '''
    
    tree_edge = prim(edge_list,node_num,adj_mat)

    neighbours = {}
    for i in range(node_num):
        neighbours[i] = set()
    for edge in tree_edge:
        neighbours[edge[0]].add(edge[1])
        neighbours[edge[1]].add(edge[0])
    
    path = dfs(neighbours,0,node_num)
    order = []
    for vertex in path:
        order.append(vertex)
    
    new_edge_list = []
    totcost = 0
    for i in range(node_num-1):
        new_edge_list.append((order[i],order[i+1]))
        totcost += adj_mat[order[i]][order[i+1]]
    new_edge_list.append((order[0],order[node_num-1]))
    totcost += adj_mat[order[0]][order[node_num-1]]
    
    print("Path Cost - Hamiltomian's Algorithm: ",totcost)
    plot(edge_list,new_edge_list,node_num)



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
    adj_mat = np.zeros((node_num,node_num),"int8")

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

        # Add edge to adj_mat
        adj_mat[start][end] = edge_wght
        adj_mat[end][start] = edge_wght

    # Sorting edge_list in ascending order based on weight
    edge_list = sorted(edge_list, key = lambda x: x[2])

    # Approx Hamiltonian's Cycle Algo
    approxHamil(edge_list,node_num,adj_mat)


def test():
    list = [[1, 2, 2], [0, 3, 3], [1, 3, 3], [0, 1, 4], [2, 3, 4], [0, 2, 5]]
    adj_mat = [[0,4,5,3],
                [4,0,2,3],
                [5,2,0,4],
                [3,3,4,0]]
    approxHamil(list,4,adj_mat)
    
def test1():
    list = [[0, 2, 2], [0, 3, 2], [1, 3, 2], [1, 4, 2], [2, 4, 2], [0, 1, 3], [0, 4, 3], [1, 2, 3], [2, 3, 3], [3, 4, 3]]
    adj_mat = [[0,3,2,2,3],
                [3,0,3,2,2],
                [2,3,0,3,2],
                [2,2,3,0,3],
                [3,2,2,3,0]]
    approxHamil(list,5,adj_mat)

if __name__ == "__main__":
    runner()
    # test()
    # test1()






