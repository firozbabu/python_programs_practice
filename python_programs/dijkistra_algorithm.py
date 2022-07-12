def dijkistra(nodes,edges,source_index='A'):
    path_lengths = {v:float('inf') for v in nodes}
    path_lengths[source_index]=0


    adjacent_nodes = {v:{} for v in nodes}
    for (u,v),w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv
        adjacent_nodes[v][u] = w_uv

    print(adjacent_nodes)


    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes)>0:
        upper_bounds = {v:path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds,key=upper_bounds.get)

        temporary_nodes.remove(u)

        for v,w_uv in adjacent_nodes[u].items():
            path_lengths[v] = min(path_lengths[v],path_lengths[u]+w_uv)

    return path_lengths

print(dijkistra(['A','B','C','D','E','F'],{('A','B'):2,('A','D'):8,('B','D'):5,('B','E'):6,('D','E'):3,('D','F'):2,('E','C'):9,('F','C'):3}))


