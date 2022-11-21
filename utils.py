import networkx as nx
import matplotlib.pyplot as plt

def find_parent(parent,node):
    if node != parent[node]:
        parent[node] = find_parent(parent,parent[node])
    return parent[node]

def connect_subtrees(parent, subtree_sizes, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)
    if subtree_sizes[xroot] < subtree_sizes[yroot]:
        parent[xroot] = yroot
    elif subtree_sizes[xroot] > subtree_sizes[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        subtree_sizes[xroot] += 1


def is_cycle(edge_list,node_num):
    '''
    Checking for Cycle
    '''
    parent = [i for i in range(node_num)]
    rank = [0]*node_num

    for edge in edge_list:
        node_begin = edge[0]
        node_end = edge[1]

        group_begin = find_parent(parent,node_begin)
        group_end = find_parent(parent,node_end)

        if group_begin == group_end:
            return True
        else:
            if group_begin == group_end:
                pass

            elif rank[group_begin] > rank[group_end]:
                parent[group_end] = group_begin
            
            else:
                parent[group_begin] = group_end
                if rank[group_begin] == rank[group_end]:
                    rank[group_end]+=1
    return False

def closest_node(cost,tree,node_num,max):

    min = max

    for i in range(node_num):
        if cost[i] < min and tree[i] == False:
            min = cost[i]
            index_min = i

    return index_min

