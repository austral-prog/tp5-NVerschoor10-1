def max_of_two(x, y):
    """Dado x e y, retorna el mayor de los dos."""
    if x > y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    """Dado x, y y z, retorna el mayor de los tres."""
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z
