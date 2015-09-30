from undirected_graph import Graph

G = Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(6, 3)
G.add_edge(5, 1)
G.add_edge(4, 2)


def dfs(graph, starting_vertex):
    """
    Stack: FIFO
    
    start at starting_vertex
    iterate all verticies adjacent to starting_vertex
    if vertex not in visited
    add vertex to visited
    """
    visited = set()
    stack = graph.adjacent_to(starting_vertex)
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # stack.remove(vertex)
    return visited

def dfs_path(graph, starting_vertex, goal_vertex):
    """
    outputs all possible paths from 
    starting_vertex to goal_vertex
    inside an undirect graph.
    """
    stack = graph.adjacent_to[starting_vertex]
    for vertex in stack:
        