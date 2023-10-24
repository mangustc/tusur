import math
import matplotlib.pyplot as plt

def f(x) -> float:
    return math.sqrt(x)

def lagrange(x: float, table_x: list[float], table_y: list[float]) -> float:
    answer: float = 0
    for i in range(len(table_x)):
        numerator: float = table_y[i]
        denominator: float = 1
        for j in range(len(table_x)):
            if j == i:
                continue
            numerator *= (x - table_x[j])
            denominator *= (table_x[i] - table_x[j])
        answer += numerator / denominator

    return answer

if __name__ == "__main__":
    table_x: list[float] = [0, 1, 2, 3, 4]
    table_y: list[float] = [0, 0, 0, 0, 0]
    for i in range(len(table_x)):
        table_y[i] = f(table_x[i])
    print("table_x: ", table_x)
    print("table_y: ", table_y)

    lagrange_x = lagrange(2.5, table_x, table_y)
    function_x = f(2.5)
    print("lagrange: ", lagrange_x)
    print("function: ", function_x)
    print("absolute error: ", abs(lagrange_x - function_x))

    points: int = 1000
    a: float = table_x[0]
    b: float = table_x[len(table_x) - 1]
    f_points_x: list[float] = []
    f_points_y: list[float] = []
    l_points_y: list[float] = []
    x: float = a
    h: float = (b - a) / points
    for i in range(points):
        f_points_x.append(x)
        f_points_y.append(f(x))
        l_points_y.append(lagrange(x, table_x, table_y))
        x += h
    plt.plot(f_points_x, f_points_y, color="blue")
    plt.plot(f_points_x, l_points_y, color="red")
    plt.scatter(table_x, table_y, color="black")
    plt.show()
    plt.savefig("mygraph.png")


