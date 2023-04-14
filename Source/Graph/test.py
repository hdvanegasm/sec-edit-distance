import graph

if __name__ == "__main__":
    G = graph.Graph(tau=4)
    G.generate_dependency_graph()
    
    s_paths = G.shortest_paths(v=(2, 2), w=(0, 0))
    all_paths = G.all_paths(v=(2, 2), w=(0, 0))
    relevant_forms = G.get_relevant_formulas(v_init=(2, 2), v_end=(0, 0))
    
    print("# Shortest paths =", len(s_paths))
    print("Shortest paths =", s_paths)
    
    print("--")
        
    print("# All paths =", len(all_paths))
    print("All paths =", all_paths)
    
    print("--")
    
    print("# Relevant formulas =", len(relevant_forms))
    for relevant_form in relevant_forms:
        print(relevant_form)
        
    print("\n===========[TEST]===========")
    
    end = (0, 0)
    tau = 5 
    
    G = graph.Graph(tau)
    G.generate_dependency_graph()
    
    formulas = G.get_block_formulas_from_endpoint(end)
    
    print("==> Formulas for D[i-{}, j-{}]".format(end[0], end[1]))
    
    for f in formulas:
        print(graph.format_formula(f))
        
    print("Number of formulas:", len(formulas))
