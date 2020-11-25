from Student import Student

student1 = Student("Anamitra Dey", "ECE", 3.1, True)
student2 = Student("Sagarika Paul", "MCA", 3.5, False)

print(student1.is_on_probation)

student1.to_string()

print(student1.on_honor_role())
