class Graph:
    '''
    Implementation of a graph to represent the dependencies between positions
    of the matrix in the edit distance computation. This dependencies are given
    by the formulas presented in the Fisher-Wagner algorithm.
    '''
    
    def __init__(self) -> None:
        # Adjacency list.
        self.adj = {}
    
    def add_edge(self, v, w) -> None:
        '''
        Add an edge to the graph.
        '''
        self.adj[v].append(w)
    
    def add_vertex(self, v) -> None:
        '''
        Add an edge to the graph.
        '''
        if not v in self.adj:
            self.adj[v] = []
        
    def shortest_paths(self, v, w):
        '''
        Given two vertices v and w, the method returns all the shortest paths
        between the two vertices.
        '''
        pass
    
    def all_paths(self, v, w):
        '''
        Given two vertices v and w, the method returns all paths between the two
        vertices.
        '''
        pass
    
    def generate_dependency_graph(self, n, m):
        '''
        The method add all the vertices and edges to construct the dependency
        graph for a given number of rows and columns in the edit distance 
        problem.
        '''
        pass
    
    def get_indexes_formulas(self, v_init, v_end):
        '''
        Return all the indexes formulas for a pair of indexes. Here v_init is in
        T or L, and v_end is in R or B.
        '''
        pass
    
    def get_red_diff(self, path_ref, path_other):
        '''
        Returns the number of red edges in path_ref but not in path_other.
        '''
        pass
    
    def get_black_edges(self, path):
        '''
        Returns the number of black edges in the path.
        '''
        pass
    