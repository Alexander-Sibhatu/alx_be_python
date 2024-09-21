num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")
result = None

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("division by zero is not valid")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation")

if result is not None:
    print(f"The result is {result}")