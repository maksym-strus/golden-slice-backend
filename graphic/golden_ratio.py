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

    try:
        f0 = func(start_point)
        f1 = func(start_point + h)
    except:
        raise Exception("Can't calculate function while finding a segment with minimum. Please, use another entry "
                        "data.")

    if f0 < f1:
        h = -h

        try:
            f0 = func(start_point)
            f1 = func(start_point + h)
        except:
            raise Exception("Can't calculate function while finding a segment with minimum. Please, use another entry "
                            "data.")

    x = start_point

    x_values = [start_point, start_point + h]

    k = 0

    while f0 > f1:
        k += 1
        x = x + h
        h = h * 2

        x_values = [x - h, x, x + h, x + (h / 2)]

        try:
            f0 = func(x)
            f1 = func(x + h)
        except:
            raise Exception("Can't calculate function while finding a segment with minimum. Please, use another entry "
                            "data.")

        if k == 50:
            raise Exception("Can't find a local segment with a minimum point. Please, use another entry data.")

    return [min(x_values), max(x_values)]


def golden_ratio(func, point_a, point_b, number_of_points, acc):
    a = point_a
    b = point_b

    x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
    x2 = a + b - x1

    try:
        f1 = func(x1)
        f2 = func(x2)
    except:
        raise Exception("Can't calculate function while finding a minimum. Please, use another entry "
                        "data.")

    config = {
        'start_point': round(a, 4),
        'end_point': round(b, 4),
    }

    iterations = []

    k = 0

    while abs(a - b) >= acc:
        iterations.append({
            'start_point': round((number_of_points - 1) * ((a - point_a) / (point_b - point_a)), 4),
            'end_point': round((number_of_points - 1) * ((b - point_a) / (point_b - point_a)), 4),
            'start_point_value': round(a, 4),
            'end_point_value': round(b, 4),
            'y_value': round(x1, 4),
            'f_y_value': np.round(f1, 4),
            'z_value': round(x2, 4),
            'f_z_value': np.round(f2, 4),
            'is_left_slice': bool(f1 <= f2),
            'is_right_slice': bool(f1 > f2),
            'iteration': k,
        })

        k += 1

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

        try:
            f1 = func(x1)
            f2 = func(x2)
        except:
            raise Exception("Can't calculate function while finding a minimum. Please, use another entry "
                            "data.")
        if k == 50:
            raise Exception("Can't find a minimum point. Please, use another entry data.")

    config['iterations'] = iterations
    config['number_of_iterations'] = len(iterations)
    config['result'] = round((a + b) / 2, 4)

    return config


def calculate_function_local_min(function_string, init_point=0, step=0.1, number_of_points=50, acc=0.001):
    try:
        formula = Formula(function_string)

        function = np.vectorize(formula.f)
    except:
        raise Exception("Can't read an input function. Please, read 'About' section for getting more information how "
                        "to write functions using Mathematica symbols")

    if (function(init_point + abs(step)) > function(init_point)) and (
            function(init_point - abs(step)) > function(init_point)) and abs(step) < acc:
        return {
            'result': init_point,
            'formula': f'${latex(formula.get_formula())}$',
            'acc': acc,
        }

    (a, b) = dsk(function, init_point, step)

    result = golden_ratio(function, a, b, number_of_points, acc)

    x_values = np.round(np.linspace(a, b, num=int(number_of_points)), 4).tolist()
    y_values = np.round(function(x_values), 4).tolist()

    result['formula'] = f'${latex(formula.get_formula())}$'

    result['x_values'] = x_values
    result['y_values'] = y_values

    result['number_of_points'] = number_of_points
    result['acc'] = acc

    return result
