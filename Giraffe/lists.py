
friends = ["Jay", "Lee", "Mai", "Poppy", "Jess", "Yuri"]

# print specific index, negative value start from -1 counted from last index
# Lee
print(friends[-3])

# print index of value + after
# ['Lee', 'Mai', 'Poppy']
print(friends[1:])

# print elements of the first value and index before last value
# ['Lee', 'Mai', 'Poppy']
print(friends[1:4])

# update value of the selected index
# ['Jay', 'Lee', 'Mike', 'Poppy', 'Jess', 'Yuri']
friends[2] = "Mike"
print(friends)
