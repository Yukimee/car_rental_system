def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":  # or letter.lower() "aeiou"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
