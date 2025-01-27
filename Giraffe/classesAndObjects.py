# object is actual student, not template, with actual information

from student import Student

student1 = Student("Lee", "IT", "4.0", True)
student2 = Student("Jim", "Business", "3.8", False)

print(student1.gpa)
print(student2.name)
