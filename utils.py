import networkx as nx
import matplotlib.pyplot as plt
import scipy

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

def plot(og_edge_list,edge_list,node_num):
    G = nx.Graph()
    for i in range(node_num):
        G.add_node(i)

    edge_labels = {}
    for edge in og_edge_list:
        G.add_edge(edge[0],edge[1],weight = edge[2])
        edge_tuple = (edge[0],edge[1])
        edge_labels[edge_tuple] = edge[2]
    
    pos = nx.planar_layout(G)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,verticalalignment= "baseline")
    nx.draw(G,pos)

    H = nx.Graph(edge_list)
    nx.draw(H,pos,edge_color="red",with_labels = True)
    plt.show()

def dfs(graph, node, node_num, arr, vis=None):

    if vis is None:
        vis = set()
    vis.add(node)

    arr.append(node)

    for next in graph[node] - vis:
        dfs(graph, next, node_num, arr, vis)
    return arr