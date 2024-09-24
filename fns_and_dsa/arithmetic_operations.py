def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 == 0:
                print("invalid division")
                return None
            elif num2 != 0:
                result = num1 / num2
        case _:
            print("invalid input")
            return None


    return result