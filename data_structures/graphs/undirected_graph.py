class Graph(object):
    
    """
    Implementation of an undirected Graph API.
    Uses an adjacency list representation.
    Verticies can be strings or integers.
    """
    
    def __init__(self):
        self.verticies = []
        self.num_of_verticies = len(self.verticies)
        self.num_of_edges = self.num_of_verticies - 1
        self.adjacency_list = {}
        
    def add_edge(self, vertex_one, vertex_two):
        """
        adds edge with vertex 1 and vertex 2
        """
        if self.adjacency_list.get(vertex_one, 0) != 0:
            self.adjacency_list[vertex_one].append(vertex_two)
        else:
            self.adjacency_list[vertex_one] = [vertex_two]
        if self.adjacency_list.get(vertex_two, 0) != 0:
            self.adjacency_list[vertex_two].append(vertex_one)
        else:
            self.adjacency_list[vertex_two] = [vertex_one]
        
    def adjacent_to(self, vertex):
        """
        returns a list of vertex's adjacent to the given `vertex`
        """
        return self.adjacency_list[vertex]
    
    def to_string(self):
        """
        Displays the Graph to the console
        """
        string = []
        for key_vertex in self.adjacency_list:
            values = self.adjacency_list[key_vertex]
            string.append(key_vertex)
            string.append("-->")
            string.append(values)
        return " ".join(str(v) for v in string)
