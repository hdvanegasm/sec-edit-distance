import graph

if __name__ == "__main__":
    G = graph.Graph(tau=3)
    G.generate_dependency_graph()
    
    s_paths = G.shortest_paths(v=(3, 1), w=(1, 0))
    all_paths = G.all_paths(v=(3, 1), w=(1, 0))
    relevant_forms = G.get_relevant_formulas(v_init=(3, 1), v_end=(1, 0))
    
    print("# Shortest paths =", len(s_paths))
    print("Shortest paths =", s_paths)
    
    print("--")
        
    print("# All paths =", len(all_paths))
    print("All paths =", all_paths)
    
    print("--")
    
    print("# Relevant formulas =", len(relevant_forms))
    for relevant_form in relevant_forms:
        print(relevant_form)