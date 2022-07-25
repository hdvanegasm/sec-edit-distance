'''
This source code is an implementation of the edit-distance algorithm
using dynamic programming and a reduction of the min calculation.
At this moment this is valid only for len(A) and len(B) being even.
'''

import numpy as np


def t(i, j, A, B):
    return int(not A[i - 1] == B[j - 1])


def edit_distance(A, B):
    D = np.zeros(shape=(len(A) + 1, len(B) + 1))
    
    # Fill base cases
    for i in range(len(A) + 1):
        D[i][0] = i
    for j in range(len(B) + 1):
        D[0][j] = j

    for i in range(2, len(A) + 1, 2):
        for j in range(2, len(B) + 1, 2):
            D[i][j] = min(
                D[i - 2][j - 2] + t(i - 1, j - 1, A, B) + t(i, j, A, B),
                D[i - 2][j - 1] + t(i - 1, j, A, B) + 1,
                D[i - 2][j - 1] + t(i, j, A, B) + 1,
                D[i - 2][j] + 2,
                D[i - 1][j - 2] + t(i, j, A, B) + 1,
                D[i - 1][j - 2] + t(i, j - 1, A, B) + 1,
                D[i][j - 2] + 2
            )
            
            D[i - 1][j] = min(
                D[i - 1][j - 2] + 2,
                D[i - 2][j - 2] + t(i - 1, j - 1, A, B) + 1,
                D[i - 2][j] + 1,
                D[i - 2][j - 1] + t(i - 1, j, A, B)
            )
            
            D[i][j - 1] = min(
                D[i - 2][j - 1] + 2,
                D[i - 2][j - 2] + t(i - 1, j - 1, A, B) + 1,
                D[i][j - 2] + 1,
                D[i - 1][j - 2] + t(i, j - 1, A, B)
            )
    
    return D[len(A)][len(B)]

if __name__ == "__main__":
    file_chain_A = open("Inputs/arithmetic/Input-P0-0")
    file_chain_B = open("Inputs/arithmetic/Input-P1-0")
    
    A = file_chain_A.read().replace("\n", "")
    B = file_chain_B.read().replace("\n", "")   
    
    file_chain_A.close()
    file_chain_B.close()

    print("Distance =", edit_distance(A, B))