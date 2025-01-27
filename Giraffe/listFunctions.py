lucky_numbers = [4, 8, 9, 3, 6, 23, 465, 12]
friends = ["Jay", "Lee", "Mai", "Poppy", "Jess", "Yuri", "Poppy"]

print(friends)

# copy the list
friends2 = friends.copy()
print(friends2)

# sort elements in ascending list
friends.sort()
print(friends)

# sort number from smaller to biggest
lucky_numbers.sort()
print(lucky_numbers)

# sort number from biggest to smaller
lucky_numbers.reverse()
print(lucky_numbers)

# extend function, take 1 list append the other list
friends.extend(lucky_numbers)
print(friends)

# always add after the last value
friends.append("Cred")
print(friends)

# insert value before the number, push to the right
friends.insert(2, "Mandy")
print(friends)

# remove element
friends.remove("Mandy")
print(friends)

# check specific element
print(friends.index("Poppy"))

# count specific element
print(friends.count("Poppy"))

# remove the last element in the list
friends.pop()
print(friends)

# remove all elements
friends.clear()
print(friends)



