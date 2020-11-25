
def fibonacci(num):
    result = []
    a, b = 0, 1
    while a < num:
        result.append(a)
        a, b = b, a + b
    return result


num = input("Enter the number: ")
print(fibonacci(int(num)))
