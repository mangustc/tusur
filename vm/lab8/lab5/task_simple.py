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
        for i in range(rows):
            sum: float = 0
            for j in range(rows):
                if i != j:
                    sum += abs(a_mat[i][j])
            if abs(a_mat[i][i]) <= sum:
                is_wrong = True
                break


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
        for i in range(rows):
            sum: float = 0
            for j in range(rows):
                if i != j:
                    sum += abs(a_mat[i][j])
            if abs(a_mat[i][i]) <= sum:
                is_wrong = True
                break

    return a_mat, b_mat

def solve_simple(a_mat, b_mat, eps: float) -> tuple[list[float], int]:
    n: int = len(a_mat)

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
    print("C: ", C)
    print("B: ", B)

    X: list[list[float]] = [B.copy(), []]
    # X: list[list[float]] = []
    # X.append([])
    # for j in range(n):
    #     X[0].append(0.0)
    # X.append([])

    for i in range(n):
        sum: float = 0
        for j in range(n):
            sum += C[i][j] * X[0][j]
        X[1].append(B[i] + sum)
    print(X)

    is_end: bool = False
    for i in range(n):
        if abs(X[0][i] - X[1][i]) <= eps:
            is_end = True
            break
    
    iterations: int = 1

    while not is_end:
        iterations += 1
        X[0] = X[1].copy()
        X[1] = []
        print(X[0])

        for i in range(n):
            sum: float = 0
            for j in range(n):
                sum += C[i][j] * X[0][j]
            X[1].append(B[i] + sum)


        for i in range(n):
            if abs(X[0][i] - X[1][i]) <= eps:
                is_end = True
                break

    return X[1], iterations

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

    X, iterations = solve_simple(a_mat, b_mat, 0.000001)
    print("\nX: ", X)
    print("iterations: ", iterations)
    check_solution(a_mat, b_mat, X)

    

