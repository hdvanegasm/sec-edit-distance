import graph

if __name__ == "__main__":
    G = graph.Graph(tau=10)
    G.generate_dependency_graph()
    
    s_paths = G.shortest_paths(v=(10, 1), w=(0, 0))
    
    for path in s_paths:
        print(path)
        print(G.get_colored_path(path))
        print("---")