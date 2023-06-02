from concrete import fhe
import numpy as np


def edit_distance(A, B):
    D = np.zeros(shape=(A.shape[0] + 1, B.shape[0] + 1))
    for i in range(A.shape[0] + 1):
        D[i][0] = i
    for j in range(B.shape[0] + 1):
        D[0][j] = j

    for i in range(1, A.shape[0] + 1):
        for j in range(1, B.shape[0] + 1):
            first_comp = D[i - 1][j] + 1 <= D[i][j - 1] + 1
            first_min = first_comp * (D[i - 1][j] + 1) + \
                (1 - first_comp) * (D[i][j - 1] + 1)

            second_comp = first_min <= D[i][j - 1] + (A[i - 1] != B[j - 1])
            final_min = second_comp * first_min + \
                (1 - second_comp) * (D[i][j - 1] + (A[i - 1] != B[j - 1]))

            print(D)
            print((A[i - 1] != B[j - 1]))
            D[i][j] = final_min

    return D[A.shape[0]][B.shape[0]]


if __name__ == "__main__":
    #    compiler = fhe.Compiler(edit_distance, {"A": "encrypted",
    #                                        "B": "encrypted"})
    input_set = [
            (np.array([0, 1, 3, 2, 1]), np.array([0, 1, 3, 2, 1])),
            (np.array([0, 1, 2, 1]), np.array([0, 1, 2, 1])),
            (np.array([0, 1, 3, 3, 2, 1]), np.array([0, 2, 1, 3, 2, 1])),
    ]

    # circuit = compiler.compile(input_set)
    print(edit_distance(input_set[0][0], input_set[0][1]))
