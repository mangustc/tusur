from numpy.random import random, randint
# from numpy.linalg import det
import numpy as np

def det(a_mat: list[list]) -> float:
    sum: float = 0

    if len(a_mat) == 2 and len(a_mat[0]) == 2:
        return a_mat[0][0] * a_mat[1][1] - a_mat[1][0] * a_mat[0][1]

    for column in range(len(a_mat)):
        minor_mat: list[list] = a_mat.copy()[1:]
        for i in range(len(minor_mat)):
            minor_mat[i] = minor_mat[i][0:column] + minor_mat[i][(column + 1):]
        sum += (-1) ** (column % 2) * a_mat[0][column] * det(minor_mat)

    return sum

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
        # if det(a_mat) == 0:
        #     is_wrong = True


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
        # if det(a_mat) == 0:
        #     is_wrong = True

    return a_mat, b_mat

def solve_inverse(a_mat: list[list]) -> list[list[float]]:
    n: int = len(a_mat)
    eps: float = 0.000000000001
    if det(a_mat) == 0 or n != len(a_mat[0]):
        print("Обратной матрицы не существует")
        return []

    inv_mat: list[list[float]] = []

    for i in range(n):
        b_mat: list[int] = []
        for j in range(n):
            b_mat.append(0)
        b_mat[i] = 1

        B: list[float] = []
        C: list[list[float]] = []
        for i in range(n):
            B.append(b_mat[i] / a_mat[i][i])
            C.append([])
            for j in range(n):
                if i == j:
                    C[i].append(0)
                else:
                    C[i].append(- (a_mat[i][j] / a_mat[i][i]))

        X: list[list[float]] = [B.copy(), []]

        for i in range(n):
            sum: float = 0
            for j in range(n):
                sum += C[i][j] * X[0][j]
            X[1].append(B[i] + sum)

        is_end: bool = True
        for i in range(n):
            if abs(X[0][i] - X[1][i]) > eps:
                is_end = False
                break

        iterations = 1
        while not is_end:
            iterations += 1
            X[0] = X[1].copy()
            X[1] = []

            for i in range(n):
                sum: float = 0
                for j in range(n):
                    sum += C[i][j] * X[0][j]
                X[1].append(B[i] + sum)


            is_end = True
            for i in range(n):
                if abs(X[0][i] - X[1][i]) > eps:
                    is_end = False
                    break
        inv_mat.append(X[1].copy())
        print("iterations: ", iterations)

    tr_inv_mat: list[list[float]] = []

    for row in range(n):
        tr_inv_mat.append([])
        for col in range(n):
            tr_inv_mat[row].append(inv_mat[col][row])

    # print("inv_Mat: ")
    # for i in range(n):
    #     print("\t", inv_mat[i])

    print("tr_inv_Mat: ")
    for i in range(n):
        print("\t", tr_inv_mat[i])

    return tr_inv_mat




def check_solution(a_mat: list[list], inv_mat: list[list]) -> None:
    n: int = len(a_mat)
    e_mat: list[list] = []
    for i in range(n):
        e_mat.append([])
        for j in range(n):
            e_mat[i].append(0)

    for row in range(n):
        for col in range(n):
            for k in range(n):
                e_mat[row][col] += a_mat[row][k] * inv_mat[k][col]
    
    print("A * A**(-1): ")
    for i in range(n):
        print("\t", e_mat[i])

    e_mat: list[list] = []
    for i in range(n):
        e_mat.append([])
        for j in range(n):
            e_mat[i].append(0)

    for row in range(n):
        for col in range(n):
            for k in range(n):
                e_mat[row][col] += inv_mat[row][k] * a_mat[k][col]

    print("A**(-1) * A: ")
    for i in range(n):
        print("\t", e_mat[i])


if __name__ == "__main__":
    # a_mat, b_mat = get_rand_float_mat(100)
    # a_mat, b_mat = get_rand_int_mat(5)
    # a_mat, b_mat = ([[9.2, 2.5, -3.7], [0.9, 9.0, 0.2], [4.5, -1.6, -10.3]], [-17.5, 4.4, -22.1])
    a_mat = [[24, 2, 3, 3, 2], [3, 56, 1, 2, 2], [2, 1,32,2,2],[3,2,2,16,2],[1,2,3,3,8]]
    print("a:", a_mat)
    # print("b:", b_mat)
    # print("det(a) = ", det(a_mat))

    inv_mat: list[list[float]] = solve_inverse(a_mat)
    # print("\ninv_mat: ", inv_mat)
    check_solution(a_mat, inv_mat)
