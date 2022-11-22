import numpy as np
from utils import is_cycle,find_parent,connect_subtrees,closest_node,plot

def kruskal(edge_list,node_num):
    '''
    Kruskals Algo
    '''
    result=[]
    i,e=0,0
    parent=[]
    subtree_sizes=[]
    for node in range(node_num):
        parent.append(node)
        subtree_sizes.append(0)
    
    # Important property of MSTs
    # number of egdes in a MST is 
    # equal to (m_num_of_nodes - 1)
    while e < (node_num - 1):
        # Pick an edge with the minimal weight
        node1, node2, weight = edge_list[i]
        i = i + 1

        x = find_parent(parent, node1)
        y = find_parent(parent, node2)

        if x != y:
            e = e + 1
            result.append([node1, node2, weight])
            connect_subtrees(parent, subtree_sizes, x, y)
    
    # Print the resulting MST
    # for node1, node2, weight in result:
    #     print("%d - %d: %d" % (node1, node2, weight))
    new_edge_list = []
    totcost = 0
    for edge in result:
        new_edge_list.append((edge[0],edge[1]))
        totcost += edge[2]
    
    print("Path Cost - Kruskal's Algorithm: ",totcost)
    plot(edge_list,new_edge_list,node_num)
    

def prim(edge_list,node_num,adj_mat,pri = 0):
    '''
    Prim's Algo
    '''
    # Init
    max = edge_list[len(edge_list)-1][2]+1
    cost = [max] * node_num
    prev = [None] * node_num
    tree = [False] * node_num
    totcost = 0
    cost[0] = 0
    prev[0] = -1

    # Add min edges w/o forming cycle
    for i in range(node_num):

        closest = closest_node(cost,tree,node_num,max)
        tree[closest] = True

        for j in range(node_num):
            if (adj_mat[closest][j] > 0)  and (tree[j] == False) and (cost[j] > adj_mat[closest][j]):
                cost[j] = adj_mat[closest][j]
                prev[j] = closest


    # Calculating Cost + Set for Graphing
    new_edge_list = []
    for i in range(len(prev)):
        if prev[i] != -1:
            new_edge_list.append((i,prev[i]))
            totcost += adj_mat[i][prev[i]]
    
    print("Path Cost - Prim's Algorithm: ",totcost)
    if pri == 1:
        plot(edge_list,new_edge_list,node_num)
    

    return edge_list

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
    kruskal(edge_list,node_num)

    # Prim's Algo
    prim(edge_list,node_num,adj_list,1)

def test():
    list = [[1, 2, 2], [2, 4, 2], [2, 3, 3], [3, 5, 3], [4, 5, 3], [0, 1, 4], [0, 2, 4], [2, 5, 4]]
    adj_mat = [[0,4,4,0,0,0],
                [4,0,2,0,0,0],
                [4,2,0,3,2,4],
                [0,0,3,0,0,3],
                [0,0,2,0,0,3],
                [0,0,4,3,3,0]]
    prim(list,6,adj_mat,1)
    kruskal(list,6)

if __name__ == "__main__":
    runner()
    #test()




