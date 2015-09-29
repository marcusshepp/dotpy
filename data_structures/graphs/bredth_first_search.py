class BFS(object):
    
    """
    Performs a Bredth-first search on an undirected Graph.
    Queue FIFO
    """
    
    def __init__(self, graph, starting_vertex):
        self.graph = graph
        self.starting_vertex = starting_vertex
        
    def marked(self, vertex):
        """
        is this vertex marked?
        """
        pass

    def count(self):
        """
        how may verticies are connected to the starting vertex?
        """
        pass