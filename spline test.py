import numpy as np
import sympy
import matplotlib.pyplot as plt
import math

def get_a(h_):
    a = np.array([round(hi/6, 3) for hi in h_])
    return a

def get_b(h_):
    b = np.zeros(n)
    for i in range(1, len(h_)):
        b[i] = -2 * h_[i] / 3
    return b

def get_c(h_):
    c = np.append(np.array([h_[i + 1] / 6 for i in range(len(h_) - 1)]), 0.)
    return c

def get_d(h_, y):
    d = np.zeros(len(h_))
    for i in range(1, len(h_)-1):
        d[i] = (y[i - 1] / h_[i]) - y[i] * (1 / h_[i] + 1 / h_[i + 1]) + (y[i + 1] / h_[i + 1])
    return d

def get_alpha(t, a, b, c):
    alpha = np.zeros(t)
    alpha[0] = 0
    for i in range(1, t):
        alpha[i] = c[i] / (b[i] - a[i] * alpha[i - 1])
    return alpha

def get_gamma(t, a, b, d, alpha):
    gamma = np.zeros(t)
    gamma[0] = 0
    for i in range(1, n - 2):
        gamma[i] = (a[i] * gamma[i - 1] - d[i]) / (b[i] - a[i] * alpha[i - 1])
    return gamma

def get_m(n, a, b, d, alpha, gamma):
    m = np.zeros(n+1)
    m[-1] = 0
    m[-2] = float((a[-1] * gamma[-1] - d[-1]) / (b[-1] - a[-1] * alpha[-1]))
    for i in range(len(m)-2):
        m[i] = float(alpha[i] * m[i + 1] + gamma[i])

    return m

def build_spline(h_, y, m):
    x = sympy.symbols("x")
    functions = []
    for i in range(1, len(m)):
        first = round(m[i - 1] / (6 * h_), 7)
        second = round(m[i] / (6 * h_), 7)
        third = round((y[i] - (m[i] * (h_ ** 2)) / 6) / h_, 7)
        fourth = round((y[i - 1] - (m[i - 1] * (h_ ** 2)) / 6) / h_, 7)
        main_expression = (first*(x_[i]-x)**3 + second*(x-x_[i-1])**3 + third*(x-x_[i-1]) + fourth*(x_[i] - x)).expand()
        functions.append(main_expression)
    return functions

def draw(x_, y, g):
    x = sympy.symbols("x")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(x_, y, c="r")

    plt.plot(x_, y, 'o', c="b")
    x_values = []
    for i in range(0, 10):
        x_values.append(np.linspace(x_[i], x_[i + 1], 20))
    function_values = []
    for i in range(10):
        f_arr = [float(g[i].subs(x, val)) for val in x_values[i]]
        function_values.append(np.array(f_arr))
    for i in range(0, 10):
        plt.plot(x_values[i], function_values[i], c="b")

    plt.legend(['f(x)', 'cubic', 'node'])
    plt.show()




if __name__ == '__main__':
    # дані інтервалу
    start = -5
    end = 0.5
    n = 11
    h = (end-start)/(n-1)
    print(h)

    h_ = np.array([round(h, 2) for i in range(n-1)])
    x_ = np.linspace(start, end, n)
    y = []
    for xi in x_:
        exp = 2 * xi + 1
        y.append(math.pow(0.5, exp))

    print("x: ", x_)
    print("h: ", h_)
    print("y: ", y)

    a = get_a(h_)
    print("a: ", a)
    b = get_b(h_)
    print("b: ", b)
    c = get_c(h_)
    print("c: ", c)
    d = get_d(h_, y)
    print("d: ", d)

    t = len(h_)
    alpha = get_alpha(t-1, a, b, c)
    print(" alpha", alpha)

    gamma = get_gamma(t-1, a, b, d, alpha)
    print(" gamma", gamma)

    m = get_m(t, a, b, d, alpha, gamma)
    print(" m", m)

    g = build_spline(h, y, m)
    for i in range(0, len(g)):
        print(f"g_{i + 1}(x) = {g[i]}.")

    draw(x_, y, g)


