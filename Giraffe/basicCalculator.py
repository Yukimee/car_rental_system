# for input, python always convert int to string
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2

# result will be 38.3 which is wrong
print(result)

# only for whole number, not for decimal number
# result = int(num1) + int(num2)
# print(result)

# to print out float number
result = float(num1) + float(num2)
print(result)


