import numpy as np

def square_root():
    """
    Compute the square root of a non-negative number.
    """
    x = float(input("Enter x: "))

    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    return np.sqrt(x)

def factorial():
    """
    Compute the factorial of a non-negative integer.
    """
    x = float(input("Enter x: "))

    if x < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    
    if not x.is_integer():
        raise ValueError("Factorial is only defined for integers.")
    
    x = int(x)
    res = 1
    for i in range(1, x + 1):
        res *= i

    return res

def natural_logarithm():
    """
    Compute the natural logarithm of a positive number.
    """
    x = float(input("Enter x: "))

    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    
    return np.log(x)

def power():
    """
    Raise x to the power of b.
    """
    x = float(input("Enter x: "))
    b = float(input("Enter b: "))

    return x ** b

def show_calculator_options(options: dict):
    """Display available operations."""
    for option, operation in options.items():
        print(f"To {operation[0]}, enter {option}")

def print_line(n : int):
    print("=" * n)

options_dict = {
    0: ["EXIT", None],
    1: ["COMPUTE SQUARE ROOT", square_root],
    2: ["COMPUTE FACTORIAL", factorial],
    3: ["COMPUTE NATURAL LOGARITHM", natural_logarithm],
    4: ["COMPUTE POWER", power]
}

LINE_SIZE = 40

if __name__ == '__main__':
    
    while True:
        print_line(LINE_SIZE)
        show_calculator_options(options_dict)
        selected_option = -1
        try:
            selected_option = int(input("\nSelect one of the above: "))
        except ValueError as e:
            print(f"Invalid option!!!")

        if selected_option == 0:
            print("Exiting calculator.")
            print_line(LINE_SIZE)
            break
        
        if selected_option in options_dict:
            try:
                result = options_dict[selected_option][1]()
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
                continue
        else:
            print(f"Invalid option!!!")
