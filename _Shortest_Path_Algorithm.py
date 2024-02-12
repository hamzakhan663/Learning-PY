my_graph = {
    # 'A': [('B', 3), ('D', 1)],
    # 'B': [('A', 3), ('C', 4)],
    # 'C': [('B', 4), ('D', 7)],
    # 'D': [('A', 1), ('C', 7)]
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    unvisited = list(graph)
    #contains numerical values representing the currently known shortest distances from the starting node to each node i.e shortest distance from A to C is 7. distances['C'] would be 7.
    distances = {node: 0 if node == start else float('inf') for node in graph}
    #contains sequence of nodes representing the currently known shortest paths from the starting node to each node i.e shortest path from A to C is A-D-C. paths['C'] would be [A, D, C]
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key = distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    targets_to_print = [target] if target else graph 
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
shortest_path(my_graph, 'A', 'F')