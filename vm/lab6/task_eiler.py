def f(x: float, y: float) -> float:
    return x / (y * y)


def _eiler_runge(x: float, y: float, h: float, eps: float) -> float:
    hstart = h
    y1: float = y + h * f(x, y)
    div: int = 2
    h = hstart / div
    yp: float = y + h * f(x, y)
    y2: float = yp + h * f(x + h, yp)
    # y1 = 2 y2 = 2.4 nastoyashee4 
    while abs(y1 - y2) / (div - 1) >= eps:
        print("y1-y2: ", abs(y1 - y2))
        y1 = y2
        div *= 2
        h = hstart / div
        xh = x
        yp = y
        for i in range(div - 1):
            yp = yp + h * f(xh, yp)
            xh += h
        y2 = yp + h * f(xh, yp)
    return y2


def eiler_runge(x0: float, y0: float, x_dest: float, h: float, eps: float) -> list[list[float]]:
    table: list[list[float]] = [[x0], [y0]]

    i = 0
    while (table[0][i] <= x_dest):
        table[0].append(table[0][i] + h)
        table[1].append(_eiler_runge(table[0][i], table[1][i], h, eps))
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
        print(f"y({table[0][i]}) = {table[1][i]}")



if "__main__" == __name__:
    table: list[list[float]] = eiler_runge(x0 = 3 / 2, y0 = 3 / 2, x_dest = 10, h = 1, eps = 0.00000000000001)
    check(table)
