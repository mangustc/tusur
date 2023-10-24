import math
import matplotlib.pyplot as plt

def f(x) -> float:
    return x ** 2

def spline(p, x, y):
    n = len(x)
    index = 0

    for i in range(0, n):
        if p < x[i]:
            index = i - 1
            break

    h = []
    for i in range(0, n - 1):
        hi = x[i + 1] - x[i]
        h.append(hi)
    print(h)

    a = []
    for i in range(0, n):
        a.append(y[i])
    print(a)

    z = []
    for i in range(0, n - 1):
        zi = 2 * (y[i + 1] - y[i]) / h[i]
        z.append(zi)
    print(z)

    b = [0]
    for i in range(0, n-1):
        bi = z[i] - b[i]
        b.append(bi)
    print(b)

    c = []
    for i in range(0, n-1):
        ci = (b[i + 1] - b[i]) / (2 * h[i])
        c.append(ci)
    print(c)

    s = a[index] + b[index] * (p - x[index]) + c[index] * ((p - x[index]) ** 2)
    return s


# def spline(p, x, y):
#     a = x[0]
#     b = x[len(x) - 1]
#     n = len(x)
#     l: list[float] = [0]
#     h = (b - a) / n
#
#     for i in range(1, n - 1):
#         li = -1 / (l[i - 1] + 4)
#         l.append(li)
#
#     c = []
#     for i in range(0, n - 1):
#         ci = 3 * (y[i + 1] - y[i - 1]) / h
#         c.append(ci)
#
#     m_big = [0]
#     m: list[float] = [0] * n
#
#     for i in range(1, n - 1):
#         mi_big = l[i] * (m_big[i - 1] - c[i])
#         m_big.append(mi_big)
#
#     print(l)
#     print(m_big)
#     print(m)
#
#     for i in range(n - 2, -1, -1):
#         mi = l[i] * m[i + 1] + m_big[i]
#         m[i] = mi
#
#     print(m)
#
#     index = 228
#     for i in range(0, n):
#         if p < x[i]:
#             index = i - 1
#             break
#
#     s1 = y[index - 1] * (p - x[index]) ** 2 * (2 * (p - x[index - 1]) + h) / h ** 3
#     s2 = y[index] * (p - x[index - 1]) ** 2 * (2 * (x[index] - p) + h) / h ** 3
#     s3 = m[index - 1] * (p - x[index]) ** 2 * (p - x[index - 1]) / h ** 2
#     s4 = m[index] * (p - x[index - 1]) ** 2 * (p - x[index]) / h ** 2
#     return s1 + s2 + s3 + s4


# def spline(x_interp, x, y):
#     a = x[0]
#     b = y[len(x) - 1]
#     n = len(x)
#     h= (b-a)/n
#
#     c= [0]
#     m= [0] * n
#     M= []
#     L= []
#     m[0] = 0
#     m[n-1] = 0
#     M.append(m[0])
#     L.append(0)
#
#     for i in range(1, n-1):
#         c.append(3*(y[i+1] - y[i-1]) / h)
#     for i in range(1, n-1):
#         L.append(-1 / (L[i-1] + 4))
#     for i in range(1, n-1):
#         M.append(L[i]*(M[i-1] - c[i]))
#     for i in range(n-2, 0, -1):
#         m[i] = L[i]*m[i+1] + M[i]
#
#     k= 0
#     for i in range(n):
#         if x_interp < x[i]:
#             # k = i - 1
#             break
#         k = i - 1
#
#     S= (y[k-1]*((x_interp - x[k])**2 * (2*(x_interp - x[k-1]) + h)) / h**3 +
#          y[k]*((x_interp - x[k-1])**2 * (2*(x[k] - x_interp) + h)) / h**3 +
#          m[k-1]*((x_interp - x[k])**2 * (x_interp - x[k-1])) / h**2 +
#          m[k]*((x_interp - x[k-1])**2 * (x_interp - x[k])) / h**2)
#
#     return S


# def spline(x: float, table_x: list[float], table_y: list[float]) -> float:
#     index: int = 0
#     for index in range(len(table_x)):
#         if x < table_x[index]:
#             index -= 1
#             break
#
#     a: float = table_x[0]
#     b: float = table_x[len(table_x) - 1]
#     n: int = len(table_x)
#     h: float = (b - a) / n
#     
#     c: list[float] = [0]
#     for i in range(1, n - 1):
#         c.append(3 * (table_y[i + 1] - table_y[i - 1]) / h)
#
#     L: list[float] = [0]
#     for i in range(1, n - 1):
#         L.append(-1 / (L[i - 1] + 4))
#
#     M: list[float] = [0]
#     for i in range(1, n - 1):
#         M.append(L[i] * (M[i - 1] - c[i]))
#
#     m: list[float] = [0] * n
#     m[0] = 0
#     m[n - 1] = 0
#     # m[0] = 2 * table_x[0]
#     # m[n-1] = 2 * table_x[n - 1]
#
#     for i in range(n - 2, 1, -1):
#         m[i] = L[i] * m[i + 1] + M[i]
#
#     answer: float = (table_y[index - 1] * (((x - table_x[index]) ** 2) * (2 * (x - table_x[index - 1]) + h)) / (h ** 3) + \
#              table_y[index] * (((x - table_x[index - 1]) ** 2) * (2 * (table_x[index] - x) + h)) / (h ** 3) + \
#              m[index - 1] * (((x - table_x[index]) ** 2) * (x - table_x[index - 1])) / (h ** 2) + \
#              m[index] * (((x - table_x[index - 1]) ** 2) * (x - table_x[index])) / (h ** 2))
#
#     return answer

if __name__ == "__main__":
    n: int = 2
    a: float = 0
    b: float = 10
    h: float = (b - a) / n
    table_x: list[float] = []
    for i in range(n):
        table_x.append(a)
        a += h

    table_y: list[float] = []
    for i in range(len(table_x)):
        table_y.append(f(table_x[i]))
    print("table_x: ", table_x)
    print("table_y: ", table_y)

    x: float = 2.5
    spline_x: float = spline(x, table_x, table_y)
    function_x: float = f(x)
    print("spline: ", spline_x)
    print("function: ", function_x)
    print("absolute error: ", abs(spline_x - function_x))

    points: int = 10000
    a: float = table_x[0]
    b: float = table_x[len(table_x) - 1]
    f_points_x: list[float] = []
    f_points_y: list[float] = []
    s_points_y: list[float] = []
    x: float = a
    h: float = (b - a) / points
    for i in range(points):
        f_points_x.append(x)
        f_points_y.append(f(x))
        s_points_y.append(spline(x, table_x, table_y))
        x += h
    plt.plot(f_points_x, s_points_y, color="red")
    plt.plot(f_points_x, f_points_y, color="blue")
    plt.scatter(table_x, table_y, color="black")
    plt.show()
    plt.savefig("mygraph.png")


