import itertools

if __name__ == "__main__":
    n = 5
    k = 3
    elements = list(range(1, n + 1))
    for comb in itertools.combinations(elements, n - k):
        print(comb)
        
