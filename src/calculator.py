import numpy as np

def square_root(x: float):
    """Compute the square root of a non-negative number."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return np.sqrt(x)

def factorial(x: float):
    """Compute the factorial of a non-negative integer."""
    if x < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    
    if not x.is_integer():
        raise ValueError("Factorial is only defined for integers.")
    
    x = int(x)
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

def natural_logarithm(x: float):
    """Compute the natural logarithm of a positive number."""
    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return np.log(x)

def power(x: float, b: float):
    """Raise x to the power of b."""
    return x ** b

if __name__ == '__main__':
    
