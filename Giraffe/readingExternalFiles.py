# read = r, write = r, append = a, read and write = r+
employee_file = open("employees.txt", "r")

# loop, to read each single line from lines
for employee in employee_file.readlines():
    print(employee)

'''
# read each single line
print(employee_file.readline())
print(employee_file.readline())

# read specific line from lines
print(employee_file.readlines()[0])

# read all lines
print(employee_file.readlines())

# read all information in the txt file
print(employee_file.read())

# return boolean true/false
print(employee_file.readable())

'''

# close file
employee_file.close()
