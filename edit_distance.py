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
    
    return D[len(A)][len(B)]

if __name__ == "__main__":
    A = "0332122211212213333200311021123031331003221211222101023212230103032112130222312020200111030203110023"
    B = "2232121113203122113323010123023122331231323103130021312020121113130001302131230013301022013210201131"

    print("Distance =", edit_distance(A, B))