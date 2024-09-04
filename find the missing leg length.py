import math

def find_missing_leg(hypotenuse, known_leg):
    """
    Calculate the length of the missing leg of a right triangle
    given the length of the hypotenuse and the length of one leg.
    
    Arguments:
    hypotenuse -- Length of the hypotenuse
    known_leg -- Length of the leg whose length is known
    
    Returns:
    Length of the missing leg
    """
    return math.sqrt(hypotenuse**2 - known_leg**2)

def main():
    print("Missing Leg Length Calculator")
    print("-----------------------------")
    hypotenuse = float(input("Enter the length of the hypotenuse: "))
    known_leg = float(input("Enter the length of the known leg: "))
    
    if hypotenuse <= known_leg:
        print("Error: The length of the hypotenuse must be greater than the length of the known leg.")
    else:
        missing_leg = find_missing_leg(hypotenuse, known_leg)
        print("The length of the missing leg is:", missing_leg)

if __name__ == "__main__":
    main()
