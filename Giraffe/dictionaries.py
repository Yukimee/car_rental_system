# dictionaries, need to use {}
monthConversions = {
    # "Jan" is key, key need to be unique! "January" is value
    # key can be string or int
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Sep"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Lov", "Not a valid key"))
