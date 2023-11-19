def f(x: float, y: float) -> float:
    return x / (y * y)


def _runge_kutte(x: float, y: float, h: float, eps: float) -> float:
    hstart: float = h
    # y1: float = y + h * f(x, y)
    k1: float = h * f(x, y)
    k2: float = h * f(x + h / 2, y + k1 / 2)
    k3: float = h * f(x + h / 2, y + k2 / 2)
    k4: float = h * f(x + h, y + k3)
    y1: float = y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    div: int = 2
    h = hstart / div
    # yp: float = y + h * f(x, y)
    k1: float = h * f(x, y)
    k2: float = h * f(x + h / 2, y + k1 / 2)
    k3: float = h * f(x + h / 2, y + k2 / 2)
    k4: float = h * f(x + h, y + k3)
    yp: float = y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    # y2: float = yp + h * f(x + h, yp)
    k1: float = h * f(x + h, yp)
    k2: float = h * f(x + 3 * h / 2, yp + k1 / 2)
    k3: float = h * f(x + 3 * h / 2, yp + k2 / 2)
    k4: float = h * f(x + 2 * h, yp + k3)
    y2: float = yp + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    while abs(y1 - y2) / (pow(div, 4) - 1) >= eps:
        y1 = y2
        div *= 2
        h = hstart / div
        xh = x
        yp = y
        for i in range(div - 1):
            # yp = yp + h * f(xh, yp)
            k1: float = h * f(xh, yp)
            k2: float = h * f(xh + h / 2, yp + k1 / 2)
            k3: float = h * f(xh + h / 2, yp + k2 / 2)
            k4: float = h * f(xh + h, yp + k3)
            yp: float = yp + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            xh += h
        # y2 = yp + h * f(xh, yp)
        k1: float = h * f(xh, yp)
        k2: float = h * f(xh + h / 2, yp + k1 / 2)
        k3: float = h * f(xh + h / 2, yp + k2 / 2)
        k4: float = h * f(xh + h, yp + k3)
        y2: float = yp + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y2


def runge_kutte(x0: float, y0: float, x_dest: float, h: float, eps: float) -> list[list[float]]:
    table: list[list[float]] = [[x0], [y0]]

    i: int = 0
    while (table[0][i] <= x_dest):
        table[0].append(table[0][i] + h)
        table[1].append(_runge_kutte(table[0][i], table[1][i], h, eps))
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
    table: list[list[float]] = runge_kutte(x0 = 3 / 2, y0 = 3 / 2, x_dest = 10, h = 1, eps = 0.00000000000001)
    check(table)
