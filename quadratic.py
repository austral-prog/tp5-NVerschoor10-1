def roots(a, b, c):
    """Devuelve las raíces reales de la ecuación cuadrática ax² + bx + c = 0."""
    
    discriminante = b * b - 4 * a * c  

    if discriminante > 0:
        raiz = discriminante ** 0.5
        r1 = (-b + raiz) / (2 * a)
        r2 = (-b - raiz) / (2 * a)
        return "(" + str(r1) + ", " + str(r2) + ")"
    elif discriminante == 0:
        r = -b / (2 * a)
        return "(" + str(r) + ")"
    else:
        return "( )"  



def value_y(a, b, c, x):
    return a * x**2 + b * x + c



def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {c}"



def derivation(a, b, c):
    coef_a = 2 * a
    coef_b = b

    if coef_a != 0 and coef_b != 0:
        return f"f'(x) = {coef_a} * X + {coef_b}"
    elif coef_a != 0 and coef_b == 0:
        return f"f'(x) = {coef_a} * X"
    elif coef_a == 0 and coef_b != 0:
        return f"f'(x) = {coef_b}"
    else:
        return "f'(x) = 0"

