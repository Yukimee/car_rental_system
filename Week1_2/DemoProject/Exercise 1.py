print("Please enter your score for the tests below:")
test1 = input("Test 1:")
test2 = input("Test 2:")
test3 = input("Test 3:")

# to convert str to int using int(test1)
# collect all 3 tests and divide it to 3
average_score = ((float(test1)+float(test2)+float(test3))/3)

# to print the average score from the input
print("Average score for the test", round(average_score, 2))


# from lecturer
