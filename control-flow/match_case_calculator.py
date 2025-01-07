# Prompt the user for input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose the operation: +, -, *, /: ")

# Initialize result
result = None

# Perform the operation using match-case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation.")

# Print the result if it's valid
if result is not None:
    print(f"Result: {result}")
        
