from math import sqrt
import numpy as np

def cholesky(A):
    n = len(A)
    # Create zero matrix for L and U
    L = np.array([[0.0] * n for i in range(n)])
    U = np.array([[0.0] * n for i in range(n)])
    #diagonal U-matrix:
    for el in range(n):
        U[el][el] = 1
    #1-col of L-matrix:
    for row in range(n):
        L[row][0] = A[row][0]
    #1-row of U-matrix:
    for col in range(n):
        U[0][col] = A[0][col]/L[0][0]
    #2-col of L-matrix:
    L[1][1] = A[1][1] - L[1][0] * U[0][1]
    L[2][1] = A[2][1] - L[2][0] * U[0][1]
    L[3][1] = A[3][1] - L[3][0] * U[0][1]
    #2-row of U-matrix:
    U[1][2] = 1/L[1][1] * (A[1][2] - L[1][0] * U[0][2])
    U[1][3] = 1/L[1][1] * (A[1][3] - L[1][0] * U[0][3])
    #3-col of L-matrix:
    L[2][2] = A[2][2] - (L[2][0] * U[0][2] + L[2][1] * U[1][2])
    L[3][2] = A[3][2] - (L[3][0] * U[0][2] + L[3][1] * U[1][2])
    #3-row of U-matrix:
    U[2][3] = 1/L[2][2] * (A[2][3] - (L[2][0]*U[0][3] + L[2][1]*U[1][3]))
    #4-col of L-matrix:
    L[3][3] = A[3][3] - (L[3][0]*U[0][3] + L[3][1]*U[1][3] + L[3][2]*U[2][3])
    print("L: \n", L)
    print("U: \n", U)
    print("det:", np.linalg.det(L))



if __name__ == '__main__':
    # create A-matrix
    A = np.array(
       [[14.11, 4.45, 6.97, 3.23],
       [6.66, 14.37, 13.23, 4.18],
       [6.43, 12.27, 13.67, 3.88],
       [3.77, 6.22, 2.86, 11.90]])
    print(A)
    cholesky(A)

