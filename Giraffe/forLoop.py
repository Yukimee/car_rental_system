# letter is string
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kelvin"]

# friend is string
for friend in friends:
    print(friend)

# name is string
for name in friends:
    print(name)

# index is integer
for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

len(friends)  # friends is name of the array
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
