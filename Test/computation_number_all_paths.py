import math

def delanoy(m, n):
    sumat = 0
    for k in range(min(m, n) + 1):
        sumat += math.comb(m, k) * math.comb(n, k) * (2 ** k)
    return sumat
    
def compute_n_paths(tau):
    sumat = 0
    for k in range(1, tau + 1):
        sumat += delanoy(tau, tau - k) + delanoy(tau - k, tau)
    return sumat + delanoy(tau, tau)
    
if __name__ == "__main__":
    tau = 300
    n_paths = compute_n_paths(tau)
    print("The number of paths for tau={} is {:e}".format(tau, n_paths))
    print("The bound in O notation is {:e}".format(2 ** (3 * tau)))
    print("The number of optimized rounds is bounded by", math.log2(n_paths))
    print("The bound for the number of optimized rounds is bounded by", math.log2(n_paths))
    print("The number of traditional rounds has order", tau ** 2)
    
    