from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.parsing.mathematica import mathematica
from math import sqrt

import numpy as np

import json


class Formula:
    def __init__(self, formula):
        self.formula = mathematica(formula)

    def f(self, x):
        return float(self.formula.subs({'x': x}).evalf())

    def get_formula(self):
        return self.formula


def dsk(func, start_point, step):
    h = step

    f0 = func(start_point)
    f1 = func(start_point + h)

    if f0 < f1:
        h = -h

        f0 = func(start_point)
        f1 = func(start_point + h)

    x = [start_point]

    while f0 >= f1:
        h = h * 2

        x.append(x[-1] + h)

        f0 = func(x[-2])
        f1 = func(x[-1])

    h = h / 2

    x.append(x[-1] - h)

    if len(x) < 4:
        return min(x), max(x)

    x = [x[-4], x[-3], x[-1], x[-2]]

    if func(x[0]) > func(x[-1]):
        x = x[1:]
    else:
        x = x[:-1]

    return min(x), max(x)


def golden_ratio(func, point_a, point_b, acc):
    a = point_a
    b = point_b

    x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
    x2 = a + b - x1

    f1 = func(x1)
    f2 = func(x2)

    config = {
        'start_point': a,
        'end_point': b
    }

    iterations = []

    while abs(a - b) >= acc:

        if f1 <= f2:
            a = a
            b = x2
            x2 = x1
            x1 = a + b - x2

        else:
            a = x1
            b = b
            x1 = x2
            x2 = a + b - x1

        f1 = func(x1)
        f2 = func(x2)

        iterations.append({
            'start_point': a,
            'end_point': b
        })

    config['iterations'] = iterations
    config['number_of_iterations'] = len(iterations)
    config['result'] = (a + b) / 2

    return config


def calculate_function_local_min(function_string, init_point=0, step=0.1, number_of_points=50, acc=0.001):
    formula = Formula(function_string)
    function = np.vectorize(formula.f)

    (a, b) = dsk(function, init_point, step)

    result = golden_ratio(function, a, b, acc)

    x_values = np.linspace(a, b, num=number_of_points).tolist()
    y_values = function(x_values).tolist()

    result['x_values'] = x_values
    result['y_values'] = y_values

    result['acc'] = acc

    return result