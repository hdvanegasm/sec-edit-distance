import itertools

if __name__ == "__main__":
    n = 3
    
    # Computation of minimum elements in terms of T
    for i in range(0, n + 1):
        elements = list(range(1, n + 1))
        iterator = itertools.combinations(elements, n - i)
        output = "D_{0," + str(i) + "}"
        for comb in iterator:
            t_output = ""
            for (idx, mov) in enumerate(comb):
                t_output += " + t_{" + str(mov) + "," + str(i + idx + 1) + "}"
            print(output + " " + t_output + (" + " + str(i) if i != 0 else ""))
        
    # Computation of minimum elements in terms of L
    for i in range(1, n + 1):
        elements = list(range(1, n + 1))
        iterator = itertools.combinations(elements, n - i)
        output = "D_{" + str(i) + "," + "0}"
        for comb in iterator:
            t_output = ""
            for (idx, mov) in enumerate(comb):
                t_output += " + t_{" + str(i + idx + 1)  + "," + str(mov) + "}"
            print(output + " " + t_output + (" + " + str(i) if i != 0 else ""))