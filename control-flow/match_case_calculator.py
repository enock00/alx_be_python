num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

#result
match operation:
    case '+':
        print("The result is", num1 + num2)
    case '-':
        print("The result is", num1 - num2)
    case '*':
        print("The result is", num1 * num2)
    case '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")