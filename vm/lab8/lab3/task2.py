def f(x: float) -> float:
    return 2 * (x**2)


def f_integral(a: float, b: float, eps: float) -> float:
    n: float = 10

    h = (b - a) / n
    integral1: float = 0
    x = a + h
    for k in range(n):
        integral1 += h * f(x)
        x += h

    n *= 2
    h = (b - a) / n
    integral2: float = 0
    x = a + h
    for k in range(n):
        integral2 += h * f(x)
        x += h

    now_diff = abs(integral1 - integral2)
    while now_diff > eps:
        prev_diff = now_diff
        integral1 = integral2

        n *= 2
        h = (b - a) / n
        integral2: float = 0
        x = a + h
        for k in range(n):
            integral2 += h * f(x)
            x += h

        now_diff = abs(integral1 - integral2)
        if prev_diff < now_diff:
            print("Ошибка! Заданная точность не может быть достигнута")
            break

    return integral2


if __name__ == "__main__":
    a: float = 0.0
    b: float = 1.0
    eps: float = 0.0000005
    integral = f_integral(a, b, eps)
    print(f"integral [{a}, {b}], eps {eps}: {integral}")

    print()
