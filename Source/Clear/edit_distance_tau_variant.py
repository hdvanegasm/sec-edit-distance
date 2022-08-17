'''
This source code is an implementation of the edit-distance algorithm
using dynamic programming and a reduction of the min calculation.
At this moment this is valid only for len(A) and len(B) being even.
'''

import numpy as np


def t(i, j, A, B):
    return int(not A[i - 1] == B[j - 1])


def edit_distance(A, B, tau):
    D = np.zeros(shape=(len(A) + 1, len(B) + 1))
    
    # Fill base cases
    for i in range(len(A) + 1):
        D[i][0] = i
    for j in range(len(B) + 1):
        D[0][j] = j

    for i in range(tau, len(A) + 1, tau):
        for j in range(tau, len(B) + 1, tau):
            # TODO Implement with multiple tao
            pass
            
    
    return D[len(A)][len(B)]

if __name__ == "__main__":
    file_chain_A = open("Inputs/arithmetic/Input-P0-0")
    file_chain_B = open("Inputs/arithmetic/Input-P1-0")
    
    A = file_chain_A.read().replace("\n", "")
    B = file_chain_B.read().replace("\n", "")   
    
    file_chain_A.close()
    file_chain_B.close()

    print("Distance =", edit_distance(A, B))