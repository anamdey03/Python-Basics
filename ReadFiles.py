
employee_file = open("employees.txt", "r")

print(employee_file.readable())  # Checks whether the file is readable or not

for employee in employee_file.readlines():
    print(employee)

# print(employee_file.readline())  # Prints the first line
# print(employee_file.readline())  # Prints the second line
#
# print(employee_file.readlines()[1])  # Prints all the lines by storing it in an array

employee_file.close()

