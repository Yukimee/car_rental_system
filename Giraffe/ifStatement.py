# make decision, response depends on the data given

# I wake up
# If I'm hungry || condition
# I eat breakfast

# I leave my house
# If its cloudy
# I bring an umbrella
# otherwise
# I bring sunglasses

# I'm at a restaurant
# if I want meant
# I order a steak
# otherwise if I want pasta
# I order spaghetti & meatballs
# otherwise
# I order a salad

is_male = True
is_tall = False

# for "or", if either one got True == True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male or tall")
# print You are a male or tall or both

# for "and", if either one got False == False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You either not male or not tall or both")
# print You either not male or not tall or both

# for "and", if either one got False == False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but tall")
else:
    print("You are not male and not tall")
# print You are a short male
