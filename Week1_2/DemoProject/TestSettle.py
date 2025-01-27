class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def set_name(self, name):  # Setter
        if name:  # Validate that name is not empty
            self.__name = name

        print(f"Hi, I am", self.__name)

p = Person("Alice")
p.set_name("Bob")

