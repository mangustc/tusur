import matplotlib.pyplot as plt

def f(x: float, y: float) -> float:
    # return x / (y * y)
    return y


def y(x: float) -> float:
    return pow((3 / 2) * x * x, 1 / 3)


def milna(x0: float, y0: float, x_dest: float, n: int) -> list[list[float]]:
    table: list[list[float]] = [[x0], [y0]]
    h: float = (x_dest - x0) / n

    end: int = 3
    if n < 3:
        end = n
    for j in range(end):
        k1: float = h * f(table[0][j], table[1][j])
        k2: float = h * f(table[0][j] + h / 2, table[1][j] + k1 / 2)
        k3: float = h * f(table[0][j] + h / 2, table[1][j] + k2 / 2)
        k4: float = h * f(table[0][j] + h, table[1][j] + k3)
        table[0].append(table[0][j] + h)
        table[1].append(table[1][j] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4))

    i = end
    while (table[0][i] <= x_dest - h):
        table[0].append(table[0][i] + h)
        ty = table[1][i - 3] + (4 / 3) * h * (2 * f(table[0][i], table[1][i]) - \
            f(table[0][i - 1], table[1][i - 1]) + 2 * f(table[0][i - 2], table[1][i - 2]))
        table[1].append(table[1][i - 1] + (h / 3) * (f(table[0][i + 1], ty) + \
            4 * f(table[0][i], table[1][i]) + f(table[0][i - 1], table[1][i - 1])))
        i += 1

    return table


def check(table: list[list[float]]) -> None:
    if len(table) != 2:
        print("error1")
        return
    elif len(table[0]) != len(table[1]):
        print("error2")
        return

    n: int = len(table[0])
    for i in range(n):
        print(f"y({table[0][i]}) = {table[1][i]}. Real: y({table[0][i]}) = {y(table[0][i])}")


if "__main__" == __name__:
    x0 = 0
    x_dest: float = 10
    table: list[list[float]] = milna(x0 = x0, y0 = 1, x_dest = 4, n = 20)
    check(table)

    points: int = 10000
    h: float = (x_dest - x0) / points
    x: float = x0
    table_real: list[list[float]] = [[], []]
    for i in range(points):
        table_real[0].append(x)
        table_real[1].append(y(x))
        x += h

    # plt.plot(table_real[0], table_real[1], color="blue")
    plt.plot(table[0], table[1], color="red")
    plt.scatter(table[0], table[1], color="black")
    plt.show()
