N = 5


def func(x):
    return x**2 - 4


def get_min_sampling(eps, a, b):
    left = a
    right = b

    x = left
    h = (right - left) / N
    iter_amount = 0

    while h >= eps:
        while func(x) > func(x + h):
            x += h
            iter_amount += 1
        left = x
        right = x + h
        h = (right - left) / N
        iter_amount += 1

    return x, iter_amount


if __name__ == "__main__":
    eps = 0.0005
    a = -3
    b = 3.5

    x, iter_amount = get_min_sampling(eps, a, b)
    print(f"x = {x}")
    print(f"f(x) = {func(x)}")
    print(f"iter_amount = {iter_amount}")
