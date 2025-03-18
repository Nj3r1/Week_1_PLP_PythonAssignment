
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

result = None


if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please choose +, -, *, or /.")


if result is not None:

    def format_num(n):
        return int(n) if n.is_integer() else n


    formatted_num1 = format_num(num1)
    formatted_num2 = format_num(num2)
    formatted_result = format_num(result)

    print(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")