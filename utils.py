def find_parent(parent,node):
    if node != parent[node]:
        parent[node] = find_parent(parent,parent[node])
    return parent[node]

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