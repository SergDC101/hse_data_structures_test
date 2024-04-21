import math


def f_me(x):
    if isinstance(x, (int, float)):
        if not math.isinf(x):
            return (25 * x) + 10
    return None
