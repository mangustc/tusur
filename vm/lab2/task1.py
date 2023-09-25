import math

def func(x):
    return 4 * x + math.exp(x)

def func_der1(x):
    return 4 + math.exp(x)

def func_der2(x):
    return math.exp(x)


def get_x_newton(eps, a, b):
    if func_der1(a) * func_der2(a) > 0:
        x = a
    elif func_der1(b) * func_der2(b) > 0:
        x = b
    else:
        raise RuntimeError("Not possible to find x0")
    print(f"x ---- {x}")

    func_div = func(x) / func_der1(x)
    iter_amount = 1
    while abs(func_div) >= eps:
        x -= func_div
        print(f"x ---- {x}")
        func_div = func(x) / func_der1(x)
        iter_amount += 1

    return x, iter_amount


if __name__ == '__main__':
    eps = 0.00000000005
    a = -1
    b = 1

    x, iter_amount = get_x_newton(eps, a, b)
    print(f"x = {x}")
    print(f"f(x) = {func(x)}")
    print(f"iter_amount = {iter_amount}")
