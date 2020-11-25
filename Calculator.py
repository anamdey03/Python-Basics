
def calculator(num1, num2, op):
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(abs(num1 - num2))
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid operator")


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

calculator(num1, num2, op)



