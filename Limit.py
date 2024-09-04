import sympy as sp

def calculate_limit():
    # Get user input
    func_input = input("Enter the function (in terms of x): ")
    point_input = input("Enter the point at which to evaluate the limit: ")
    
    # Define the symbol
    x = sp.symbols('x')
    
    # Parse the function input
    func = sp.sympify(func_input)
    
    # Convert point to a number
    try:
        point = float(point_input)
    except ValueError:
        print("Invalid point input. Please enter a numeric value.")
        return
    
    # Compute the limit
    limit_result = sp.limit(func, x, point)
    
    # Display the result
    print(f"The limit of {func_input} as x approaches {point_input} is {limit_result}")

if __name__ == "__main__":
    calculate_limit()
