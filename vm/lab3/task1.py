DIVIDE_NUM: float = 10


def f(x: float) -> float:
    return x**2


def f_der1(x: float, eps: float) -> float:
    dx: float = 0.1
    fx: float = f(x)
    f_d1 = (f(x + dx) - fx) / dx
    dx /= DIVIDE_NUM
    f_d2 = (f(x + dx) - fx) / dx

    now_diff = abs(f_d1 - f_d2)
    while now_diff > eps:
        prev_diff = now_diff
        f_d1 = f_d2
        dx /= DIVIDE_NUM
        f_d2 = (f(x + dx) - fx) / dx
        now_diff = abs(f_d1 - f_d2)
        if prev_diff < now_diff:
            print("Ошибка! Заданная точность не может быть достигнута")
            break

    return f_d2


if __name__ == "__main__":
    eps = 0.00000000000000000005
    for k in range(11):
        x = 1.2 + 0.1 * k
        derx = f_der1(x, eps)
        print(f"der1 {x}: {derx}")

    print()
