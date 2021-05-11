from sympy.parsing.mathematica import mathematica
from sympy.printing.latex import latex
from math import sqrt

import numpy as np


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

    a, b = [start_point, start_point + h]

    x = start_point
    x_values = []

    while f0 > f1:
        x = x + h
        h = h * 2

        x_values = [x - h, x, x + h, x + (h / 2)]

        f0 = func(x)
        f1 = func(x + h)

        if func(x_values[0]) > func(x_values[2]):
            a = x_values[1]
            b = x_values[2]
        else:
            a = x_values[0]
            b = x_values[3]

    return [a, b]


def golden_ratio(func, point_a, point_b, number_of_points, acc):
    a = point_a
    b = point_b

    x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
    x2 = a + b - x1

    f1 = func(x1)
    f2 = func(x2)

    config = {
        'start_point': round(a,2),
        'end_point': round(b,2)
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
            'start_point': round((number_of_points - 1) * ((a - point_a) / (point_b - point_a)), 2),
            'end_point': round((number_of_points - 1) * ((b - point_a) / (point_b - point_a)), 2)
        })

    config['iterations'] = iterations
    config['number_of_iterations'] = len(iterations)
    config['result'] = round((a + b) / 2, 2)

    return config


def calculate_function_local_min(function_string, init_point=0, step=0.1, number_of_points=50, acc=0.001):
    formula = Formula(function_string)
    function = np.vectorize(formula.f)

    (a, b) = dsk(function, init_point, step)

    result = golden_ratio(function, a, b, number_of_points, acc)

    x_values = np.round(np.linspace(a, b, num=int(number_of_points)), 2).tolist()
    y_values = np.round(function(x_values), 2).tolist()

    result['formula'] = f'$${latex(formula.get_formula())}$$'

    result['x_values'] = x_values
    result['y_values'] = y_values

    result['number_of_points'] = number_of_points
    result['acc'] = acc

    return result
