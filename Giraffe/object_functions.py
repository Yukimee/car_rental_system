from student import Student

student1 = Student("Lee", "IT", 4.0, True)
student2 = Student("Jim", "Business", 3.5, False)
student3 = Student("Jim", "Business", 3.4, False)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())
