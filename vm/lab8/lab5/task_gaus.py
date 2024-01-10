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

def solve_gaus(a_mat: list[list], b_mat: list) -> list[float]:
    n: int = len(a_mat)
    x: list[float] = []
    for i in range(n):
        x.append(0)
    
    a: list[list[float]] = []
    for i in range(5):
        a.append([])
        a[i] = a_mat[i].copy()

    b: list[float] = b_mat.copy()
    
    for k in range(n):
        m: list[float] = []
        for i in range(n):
            m.append(a[i][k] / a[k][k])
        for i in range(k + 1, n):
            b[i] = b[i] - m[i] * b[i]
            for j in range(n):
                a[i][j] = a[i][j] - m[i] * a[k][j]

    print(a)

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    x[n - 2] = b[n - 2] / a[n - 2][n - 2]
    for i in range(n - 3, -1, -1):
        sum: float = 0
        for j in range(n - 1, i, -1):
            sum += a[i][j] * x[j]
        x[i] = (b[i] - sum) / a[i][i]


    return x




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
    a_mat, b_mat = ([[56, 2, 2, 2, 3], [1, 48, 3, 2, 3], [2, 3, 48, 1, 1], [1, 2, 3, 16, 1], [3, 1, 3, 1, 18]], [61, 97, -38, 49, -3])
    print("a:", a_mat)
    print("b:", b_mat)
    # print("det(a) = ", det(a_mat))
    if (det(a_mat)) == 0:
        print("Determinant equals to 0")
        exit()

    X = solve_gaus(a_mat, b_mat)
    print("\nX: ", X)
    check_solution(a_mat, b_mat, X)

    

