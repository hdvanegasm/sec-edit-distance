import collections
import sys


def get_n_black_edges(self, path_colored):
    '''
    Returns the number of black edges in the path.
    '''
    
    return path_colored.count("b")


class Graph:
    '''
    Implementation of a graph to represent the dependencies between positions
    of the matrix in the edit distance computation. This dependencies are given
    by the formulas presented in the Fisher-Wagner algorithm.
    '''
    
    def __init__(self, tau) -> None:
        # Adjacency list.
        self.adj = {}
        self.tau = tau
    
    def add_edge(self, v, w, color) -> None:
        '''
        Adds an edge to the graph from v to w with the given color.
        '''
        self.adj[v].append((w, color))
    
    def add_vertex(self, v) -> None:
        '''
        Adds an edge to the graph. A vertex has the form (i, j).
        '''
        if not v in self.adj:
            self.adj[v] = []
    
    def all_paths(self, v, w):
        '''
        Given two vertices v and w, the method returns all paths between the two
        vertices.
        '''
        pass
    
    def generate_dependency_graph(self):
        '''
        Adds all the vertices and edges to construct the dependency
        graph for a given number of rows and columns in the edit distance 
        problem.
        '''
        
        # Add vertices.
        for i in range(self.tau + 1):
            for j in range(self.tau + 1):
                self.add_vertex(v=(i, j))
                
        # Add edges.
        for i in range(self.tau):
            for j in range(self.tau):
                self.add_edge(v=(i + 1, j + 1), w=(i, j), color="r")
                self.add_edge(v=(i, j + 1), w=(i, j), color="b")
                self.add_edge(v=(i + 1, j), w=(i, j), color="b")
    
    def get_indexes_formulas(self, v_init, v_end):
        '''
        Return all the indexes formulas for a pair of indexes. Here v_init is in
        T or L, and v_end is in R or B.
        '''
        pass
    
    def get_n_red_diff(self, path_ref, path_other):
        '''
        Returns the number of red edges in path_ref but not in path_other.
        '''
        pass
    
    def BFS(self, start, parents):
        '''
        Executes BFS in the graph starting from a node.
        '''
        
        distances = {}
        for vertex in self.adj.keys():
            distances[vertex] = sys.maxsize
        
        deque = collections.deque()
        
        deque.append(start)
        parents[start] = [None]
        distances[start] = 0
        
        while len(deque) > 0:
            u = deque[0]
            deque.popleft()
                        
            for (v, _) in self.adj[u]:
                if distances[v] > distances[u] + 1:
                    distances[v] = distances[u] + 1
                    deque.append(v)
                    parents[v].clear()
                    parents[v].append(u)
                elif distances[v] == distances[u] + 1:
                    parents[v].append(u)
    
    def find_paths(self, paths, path, parents, u):
        '''
        Finds all the paths recursively traversin along the parents.
        '''
        
        if u == None:
            paths.append(path.copy())
            return
        
        for parent in parents[u]:
            path.append(u)
            self.find_paths(paths, path, parents, parent)
            path.pop()
            
    def shortest_paths(self, v, w):
        '''
        Given two vertices v and w, the method returns all the shortest paths
        between the two vertices.
        '''
        
        paths = []
        path = []
        
        parents = {}
        for vertex in self.adj.keys():
            parents[vertex] = []
        
        self.BFS(v, parents)
        
        self.find_paths(paths, path, parents, w)
        result_paths = []
        for p in paths:
            p.reverse()
            result_paths.append(p)
            
        return result_paths
    
    def get_colored_path(self, path):
        colors = []
        for i in range(1, len(path)):
            for (vertex, color) in self.adj[path[i - 1]]:
                if vertex == path[i]:
                    colors.append(color)
        return colors