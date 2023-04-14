import collections
import sys


def format_formula(formula):
    D = formula[0]
    t_list = formula[1]
    b = formula[2]
    
    final_str = "D[i-{}, j-{}]".format(D[0], D[1])
    
    for t in t_list:
        final_str += " + t[i-{}, j-{}]".format(t[0], t[1])
        
    final_str += " + {}".format(b)
    return final_str

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
            
    def get_n_black_edges(self, path):
        '''
        Returns the number of black edges in the path.
        '''
    
        return self.get_colored_path(path).count("b")
            
    def DFS(self, v, w, visited, path, result):
        '''
        This method performs DFS over the graph to print all the paths between
        two vertices.
        '''
        if v == w:
            result.append(path.copy())
            return
        
        visited[v] = True
    
        for (vertex, _) in self.adj[v]:
            if not visited[vertex]:
                path.append(vertex)
                self.DFS(vertex, w, visited, path, result)
                path.remove(vertex)
                
        visited[v] = False
    
    def all_paths(self, v, w):
        '''
        Given two vertices v and w, the method returns all paths between the two
        vertices.
        '''
        visited = {}
        for vertex in self.adj.keys():
            visited[vertex] = False
        
        path = [v]
        result = []
        
        self.DFS(v, w, visited, path, result)
        
        return result
    
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
    
    def get_relevant_paths(self, v_init, v_end):
        '''
        Return all the paths induced by relevant formulas for a pair of indexes. 
        Here v_init is in T or L, and v_end is in R or B.
        '''
        
        shortest_paths = self.shortest_paths(v_init, v_end)
        all_paths = self.all_paths(v_init, v_end)
        relevant_paths = shortest_paths.copy()
        for path in all_paths:
            is_relevant = True
            for shortest_path in shortest_paths:
                red_diff = self.get_n_red_diff(shortest_path, path)
                n_black_path = self.get_n_black_edges(path)
                n_black_shortest = self.get_n_black_edges(shortest_path)
                
                if red_diff + n_black_shortest <= n_black_path:
                    is_relevant = False
            
            if is_relevant:
                relevant_paths.append(path)
                
        for path_r in relevant_paths:
            print("relevance =", self.is_completely_relevant(path_r))
                
        return relevant_paths
    
    def get_relevant_paths_all_to_all(self, v_init, v_end):
        '''
        Get all relevant paths by comparing all-to-all with respect to
        the set of paths.
        '''

        all_paths = self.all_paths(v_init, v_end)
        relevant_paths = []
        for i in range(len(all_paths)):
            current_path = all_paths[i]
            is_relevant = True
            for j in range(len(all_paths)):
                if i == j:
                    continue
                other_path = all_paths[j]
                red_diff = self.get_n_red_diff(other_path, current_path)
                b_current = self.get_n_black_edges(current_path)
                b_other = self.get_n_black_edges(other_path)
                
                if red_diff + b_other <= b_current:
                    is_relevant = False
            
            if is_relevant:
                relevant_paths.append(current_path)
                
        return relevant_paths
    
    def is_completely_relevant(self, path):
        '''
        Check if a path is inamovible from the result list.
        '''
        
        v_init = path[0]
        v_end = path[len(path) - 1]
        all_paths = self.all_paths(v_init, v_end)
        relevance = True
        for test_path in all_paths:
            if test_path == path:
                continue
            b_test_path = self.get_n_black_edges(path)
            b_path = self.get_n_black_edges(path)
            red_diff = self.get_n_red_diff(path, test_path)
            if not b_test_path > red_diff + b_path:
                relevance = False
                
        return relevance
                
    def get_relevant_formulas(self, v_init, v_end):
        '''
        This method returns all the relevant formulas given the initial and
        final vertices.
        '''
        
        # This code is for obtain the relevant paths comparing only with the set
        # of shortest paths:
        # ===========================================================
        # relevant_paths = self.get_relevant_paths(v_init, v_end)
        # ===========================================================
        relevant_paths = self.get_relevant_paths_all_to_all(v_init, v_end)
        # ===========================================================
        relevant_forms = []
        for path in relevant_paths:
            relevant_forms.append(self.get_formula_from_path(path))
        
        return relevant_forms
                    
    def get_formula_from_path(self, path):
        '''
        This method returns a formula associated with the given path.
        A formula will be represented as a list of tuple of t indexes plus the 
        number of black edges. For example: 
            ([(1, 2), (2, 0)], 4)
        represents the formula with the following form
           D_{end} = D_{init} + t_{i-1, j-2} + t_{i-2, j} + 4
        '''
        
        t_indexes = []
        colored_path = self.get_colored_path(path)
        for i in range(1, len(path)):
            if colored_path[i - 1] == "r":
                t_indexes.append(path[i])
        
        n_black = self.get_n_black_edges(path)
        
        return (path[0], t_indexes, n_black)
        
    def get_n_red_diff(self, path_ref, path_other):
        '''
        Returns the number of red edges in path_ref but not in path_other.
        Note: given the structure of the graph, the paths does not repeat
        vertices. For this reason, the tail will appear only once in the list
        as well as the head.
        '''
        
        count = 0 
        
        path_ref_colors = self.get_colored_path(path_ref)
        
        for i in range(1, len(path_ref)):
            tail_ref = path_ref[i - 1]
            head_ref = path_ref[i]
            
            if path_ref_colors[i - 1] == "r":            
                if tail_ref in path_other and head_ref in path_other:
                    index_tail_other = path_other.index(tail_ref)
                    if index_tail_other < len(path_other) - 1 and \
                            head_ref != path_other[index_tail_other + 1]:
                        count += 1
                    elif index_tail_other == len(path_other) - 1:
                        count += 1
                else:
                    count += 1
                
        return count          
    
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
        '''
        Given a path, this method returns the color of the edges of such path.
        '''
        
        colors = []
        for i in range(1, len(path)):
            for (vertex, color) in self.adj[path[i - 1]]:
                if vertex == path[i]:
                    colors.append(color)
        return colors
    
    def get_block_formulas_from_endpoint(self, end):
        '''
        This method returns all the formulas given an endpoint.
        '''
        
        # We must query for endpoints in L and B.
        assert(end[0] == 0 or end[1] == 0)
        
        # The endpoint must be inside the block
        assert((0 <= end[0] <= self.tau) and (0 <= end[1] <= self.tau))
        
        formulas = []
    
        # Top formulas.
        for j in range(end[1], self.tau + 1):
            init = (self.tau, j)
            relevant_forms = self.get_relevant_formulas(v_init=init, v_end=end)
            formulas = formulas + relevant_forms
            
        # Left formulas.
        for i in range(end[0], self.tau):
            init = (i, self.tau)
            relevant_forms = self.get_relevant_formulas(v_init=init, v_end=end)
            formulas = formulas + relevant_forms
            
        return formulas