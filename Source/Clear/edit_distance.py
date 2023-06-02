'''
This source code is an implementation of the edit-distance algorithm
using dynamic programming.
'''

import numpy as np


def edit_distance(A, B):
    D = np.zeros(shape=(len(A) + 1, len(B) + 1))

    # Fill base cases
    for i in range(len(A) + 1):
        D[i][0] = i
    for j in range(len(B) + 1):
        D[0][j] = j

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                t = 0
            else:
                t = 1

            D[i][j] = min(
                    D[i - 1][j] + 1,
                    D[i][j - 1] + 1,
                    D[i - 1][j - 1] + t
                    )

    print(D)

    return D[len(A)][len(B)]


if __name__ == "__main__":
    file_chain_A = open("Inputs/arithmetic/Input-P0-0")
    file_chain_B = open("Inputs/arithmetic/Input-P1-0")

    A = file_chain_A.read().replace("\n", "")
    B = file_chain_B.read().replace("\n", "")

    file_chain_A.close()
    file_chain_B.close()

    print("Distance =", edit_distance(A, B))
