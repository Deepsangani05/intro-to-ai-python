# ==============================================================================
# Variables and Data Types in Python
# ==============================================================================
# This program demonstrates Python's fundamental data types, dynamic typing,
# variable assignments, and basic mathematical operations.
# ==============================================================================

def main():
    print("--- 1. Variable Assignment & Dynamic Typing ---")
    
    # Python is dynamically typed; you don't need to declare types explicitly.
    name = "Deep"            # String (str)
    age = 21                 # Integer (int)
    learning_rate = 0.001    # Floating point number (float)
    is_interested_in_ai = True  # Boolean (bool)
    
    # We can inspect the types using the type() function
    print(f"Name: {name} (Type: {type(name)})")
    print(f"Age: {age} (Type: {type(age)})")
    print(f"Learning Rate: {learning_rate} (Type: {type(learning_rate)})")
    print(f"Interested in AI: {is_interested_in_ai} (Type: {type(is_interested_in_ai)})")
    print()

    print("--- 2. Basic Arithmetic Operations ---")
    # Let's perform basic calculations
    a = 15
    b = 4
    
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b          # Standard division returns a float
    integer_division = a // b  # Floor division returns an integer (trims decimal)
    modulus = a % b           # Remainder of the division
    exponent = a ** b         # Power (a raised to b)
    
    print(f"Addition: {a} + {b} = {addition}")
    print(f"Subtraction: {a} - {b} = {subtraction}")
    print(f"Multiplication: {a} * {b} = {multiplication}")
    print(f"Division: {a} / {b} = {division}")
    print(f"Integer Division: {a} // {b} = {integer_division}")
    print(f"Modulus: {a} % {b} = {modulus}")
    print(f"Exponentiation: {a} ** {b} = {exponent}")
    print()

    print("--- 3. Type Conversion (Casting) ---")
    # Convert an integer to a float
    float_age = float(age)
    print(f"Converted integer {age} to float: {float_age}")
    
    # Convert a float to an integer (truncates towards zero)
    int_rate = int(5.99)
    print(f"Converted float 5.99 to integer: {int_rate}")
    
    # Convert a number to a string
    str_val = str(3.14159)
    print(f"Converted float to string: '{str_val}' (Type: {type(str_val)})")
    print()

    print("--- 4. Interactive User Inputs ---")
    # Taking user inputs is done via the input() function.
    # Note: input() always returns a string, so we must cast it if we need numbers.
    print("Let's calculate your birth year!")
    user_age_str = input("Enter your age: ")
    
    try:
        user_age = int(user_age_str)
        current_year = 2026
        birth_year = current_year - user_age
        print(f"Since you are {user_age} years old in {current_year}, you were born around {birth_year}!")
    except ValueError:
        print(f"Oops! '{user_age_str}' is not a valid number. We skipped the math calculation.")

if __name__ == "__main__":
    main()
