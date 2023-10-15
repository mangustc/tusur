import numpy as np

DIVIDE_NUM: float = 10


# def f(x: list[float]) -> float:
#     sum: float = 0
#     for k in range(len(x)):
#         sum += x[k] ** 2
#     return sum


def f(x: list[float]) -> float:
    return (
        (x[0] ** 3) * (x[1] ** 2)
        + (x[1] ** 3) * (x[2] ** 2)
        + (x[2] ** 3) * (x[3] ** 2)
    )


def f_part_der2(x: list[float], x_num: int, eps: float) -> float:
    dx: float = 0.1
    fx: float = f(x)
    x_changed1 = x.copy()
    x_changed2 = x.copy()

    x_changed1[x_num] += dx
    x_changed2[x_num] -= dx
    f_d1 = (f(x_changed1) - 2 * fx + f(x_changed2)) / dx**2
    x_changed1[x_num] -= dx
    x_changed2[x_num] += dx

    dx /= DIVIDE_NUM

    x_changed1[x_num] += dx
    x_changed2[x_num] -= dx
    f_d2 = (f(x_changed1) - 2 * fx + f(x_changed2)) / dx**2
    x_changed1[x_num] -= dx
    x_changed2[x_num] += dx

    now_diff = abs(f_d1 - f_d2)
    while now_diff > eps:
        prev_diff = now_diff
        f_d1 = f_d2

        dx /= DIVIDE_NUM
        x_changed1[x_num] += dx
        x_changed2[x_num] -= dx
        f_d2 = (f(x_changed1) - 2 * fx + f(x_changed2)) / dx**2
        x_changed1[x_num] -= dx
        x_changed2[x_num] += dx

        now_diff = abs(f_d1 - f_d2)
        if prev_diff < now_diff:
            print("Ошибка! Заданная точность не может быть достигнута")
            break

    return f_d2


if __name__ == "__main__":
    eps = 0.005
    x = list(np.arange(1.2, 1.5, 0.1))
    x = [1.0, 1.0, 1.0, 1.0]
    for k in range(len(x)):
        part_der2x = f_part_der2(x, k, eps)
        print(f"partial2 {k} der1 {x[k]}: {part_der2x}")
