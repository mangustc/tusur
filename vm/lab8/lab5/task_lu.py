from numpy.random import random, randint
from numpy.linalg import det

def get_rand_float_mat(rows: int) -> tuple[list[list[float]], list[float]]:
    is_wrong: bool = True
    a_mat: list[list[float]] = random(size=(rows, rows)).tolist()
    b_mat: list[float] = random(size=rows).tolist()

    while is_wrong:
        a_mat: list[list[float]] = random(size=(rows, rows)).tolist()
        b_mat: list[float] = random(size=rows).tolist()

        for i in range(rows):
            b_mat[i] *= 100
            for j in range(rows):
                a_mat[i][j] *= 100
            a_mat[i][i] *= 1000

        is_wrong = False
        if det(a_mat) == 0:
            is_wrong = True


    return a_mat, b_mat

def get_rand_int_mat(rows: int) -> tuple[list[list[int]], list[int]]:
    is_wrong: bool = True
    a_mat: list[list[int]] = randint(1, 100, size=(rows, rows)).tolist()
    b_mat: list[int] = randint(1, 100, size=rows).tolist()

    while is_wrong:
        a_mat: list[list[int]] = randint(1, 100, size=(rows, rows)).tolist()
        b_mat: list[int] = randint(1, 100, size=rows).tolist()

        for i in range(rows):
            a_mat[i][i] = randint(101 * rows, 200 * rows)


        is_wrong = False
        if det(a_mat) == 0:
            is_wrong = True

    return a_mat, b_mat

def solve_lu(a_mat, b_mat) -> list[float]:
    n: int = len(a_mat)

    U: list[list[float]] = []
    for i in range(n):
        U.append([])
        for j in range(n):
            U[i].append(0)

    L: list[list[float]] = []
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)
    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(n):
            if i <= j:
                sum: float = 0
                for k in range(i):
                    sum += L[i][k] * U[k][j]
                U[i][j] = a_mat[i][j] - sum
            else:
                sum: float = 0
                for k in range(j):
                    sum += L[i][k] * U[k][j]
                L[i][j] = (a_mat[i][j] - sum) / U[j][j]

    Y: list[float] = []
    for i in range(n):
        sum: float = 0
        for k in range(i):
            sum += L[i][k] * Y[k]
        Y.append(b_mat[i] - sum)

    X: list[float] = []
    for i in range(n):
        X.append(0)
    for i in range(n - 1, -1, -1):
        sum: float = 0
        for k in range(i, n):
            sum += U[i][k] * X[k]
        X[i] = (Y[i] - sum) / U[i][i]

    return X


def check_solution(a_mat, b_mat, X: list[float]):
    print("Solution check:")
    n: int = len(a_mat)
    for i in range(n):
        sum: float = 0
        for j in range(n):
            sum += a_mat[i][j] * X[j]
        print(sum, " = ", b_mat[i])

if __name__ == "__main__":
    # a_mat, b_mat = get_rand_float_mat(100)
    a_mat, b_mat = get_rand_int_mat(5)
    # a_mat, b_mat = ([[9.2, 2.5, -3.7], [0.9, 9.0, 0.2], [4.5, -1.6, -10.3]], [-17.5, 4.4, -22.1])
    print("a:", a_mat)
    print("b:", b_mat)
    # print("det(a) = ", det(a_mat))
    if (det(a_mat)) == 0:
        print("Determinant equals to 0")
        exit()

    X = solve_lu(a_mat, b_mat)
    print("\nX: ", X)
    check_solution(a_mat, b_mat, X)
