'''
    r - Reading from a file
    w - Writing to a file
    r+ - Reading and writing to a file
    a - Appending content to the end of the file
'''


# employee_file = open("employees.txt", "a")
#
# employee_file.writable()
# employee_file.write("\nAnamitra - Software Developer")
#
# employee_file.close()

# student_file = open("students.txt", "w")
#
# student_file.write("Anamitra Dey - ECE\n")
# student_file.write("Sagarika Paul - MCA\n")
#
# student_file.close()

web_page = open("index.html", "w")

web_page.write("<p>This is HTML</p>")

web_page.close()