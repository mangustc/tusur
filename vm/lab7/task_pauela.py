import math


# def f(x: list):
#     return 2 * (x[0] ** 3) + 4 * x[0] * (x[1] ** 3) - 10 * x[0] * x[1] + x[1] ** 2


def f(x: list):
    return (x[0] + 1) ** 2 + (x[1] - 12) ** 2 + (x[2] + 3) ** 2 + (x[3] - 7) ** 2 + 7


def xl(x: list, s: list, l: float) -> list:
    xl_vec: list = x.copy()
    for i in range(len(xl_vec)):
        xl_vec[i] += l * s[i]

    return xl_vec


def x_new(x: list, s: list, eps: float) -> list:
    l: float = 0.1
    h: float = 0.1
    if f(xl(x, s, l)) > f(xl(x, s, -l)):
        l *= -1
        h *= -1

    last: float = f(xl(x, s, l))
    while abs(h) > eps:
        l += h
        cur: float = f(xl(x, s, l))
        if cur < last:
            # print(last)
            last = cur
        else:
            l -= h
            h /= 10

    # print(last)

    return xl(x, s, l)


def s_new(x_last: list, x_first: list):
    vec: list = x_last.copy()
    n: int = len(vec)
    for i in range(n):
        vec[i] -= x_first[i]
    # print(x_last, "-", x_first, "=", vec)

    length: float = 0
    for i in range(n):
        length += vec[i] ** 2
    length = math.sqrt(length)
    for i in range(n):
        vec[i] /= length
    # print(vec)

    return vec
    

def pauela(x_st: list, eps: float) -> list:
    n: int = len(x_st)

    s: list[list] = []
    for i in range(n):
        s.append([])
        for j in range(n):
            s[i].append(0)
        s[i][i] = 1

    # x: list[list] = []
    # x_first: list = x_new(x_st, s[n - 1], eps)
    # x.append(x_new(x_st, s[n - 1], eps))
    # for i in range(n):
    #     print()
    #     x.append(x_new(x[i], s[i], eps))
    # for i in range(n - 1):
    #     s[i] = s[i + 1].copy()
    # s[n - 1] = s_new(x[len(x) - 1], x[0])
    # x.append(x_new(x[len(x) - 1], s[n - 1], eps))
    #
    # for i in range(len(x)):
    #     print(x[i], ":", f(x[i]))

    x_first: list = x_new(x_st, s[n - 1], eps)
    last: float = f(x_first)
    x_last: list = x_first.copy()
    for i in range(n):
        x_last = x_new(x_last, s[i], eps)
    for i in range(n - 1):
        s[i] = s[i + 1].copy()
    s[n - 1] = s_new(x_last, x_first)
    x_last = x_new(x_last, s[n - 1], eps)

    cur: float = f(x_last)

    print(last, cur)

    while abs(last - cur) > eps:
        x_first = x_last.copy()
        last = cur
        x_last = x_first.copy()
        for i in range(n):
            x_last = x_new(x_last, s[i], eps)
        for i in range(n - 1):
            s[i] = s[i + 1].copy()
        s[n - 1] = s_new(x_last, x_first)
        x_last = x_new(x_last, s[n - 1], eps)
        cur = f(x_last)
        print(last, cur)


    return x_last


if __name__ == "__main__":
    # x_vec: list = pauela(x_st = [5, 2], eps = 0.000001)
    x_vec: list = pauela(x_st = [0, 0, 0, 0], eps = 0.0000001)
    # out: str = ""
    # out += "Found x: ["
    # for i in range(len(x_vec)):
    #     out += f"{x_vec[i]:.4f}"
    #     out +=
    print(f"Found x: {x_vec}, with f({x_vec}) = {f(x_vec)}")
