import os
import math

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Displays the calculator menu."""
    print("=" * 40)
    print("       ✨ PYTHON INTERACTIVE CALCULATOR ✨       ")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. Modulo (%)")
    print("8. View Calculation History")
    print("9. Exit")
    print("=" * 40)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return x / y

def exponent(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Error: Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def modulo(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Modulo by zero is not allowed.")
    return x % y

def main():
    history = []
    
    while True:
        clear_screen()
        show_menu()
        
        choice = input("Select an operation (1-9): ").strip()
        
        if choice == '9':
            print("\nThank you for using the Python Interactive Calculator! Goodbye! 👋")
            break
            
        if choice == '8':
            print("\n--- 📜 Calculation History ---")
            if not history:
                print("No calculations performed yet.")
            else:
                for idx, record in enumerate(history, 1):
                    print(f"{idx}. {record}")
            input("\nPress Enter to return to the menu...")
            continue

        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("\n❌ Invalid choice! Please select a valid option.")
            input("\nPress Enter to continue...")
            continue

        try:
            if choice == '6':
                num = float(input("\nEnter the number: "))
                result = square_root(num)
                operation_str = f"√({num}) = {result}"
                print(f"\n✅ Result: {operation_str}")
                history.append(operation_str)
            else:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    op = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    op = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    op = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    op = "/"
                elif choice == '5':
                    result = exponent(num1, num2)
                    op = "^"
                elif choice == '7':
                    result = modulo(num1, num2)
                    op = "%"
                
                operation_str = f"{num1} {op} {num2} = {result}"
                print(f"\n✅ Result: {operation_str}")
                history.append(operation_str)
                
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("\n❌ Error: Please enter valid numeric values.")
            else:
                print(f"\n❌ {e}")
        except ZeroDivisionError as e:
            print(f"\n❌ {e}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
