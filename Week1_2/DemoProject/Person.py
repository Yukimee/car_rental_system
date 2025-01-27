class Person:

    def __init__(self, name, address, age):
        self.__name = name
        self.address = address
        self.age = age

    def greet(self):
        print(f"My name is", self.__name)



class Student(Person):

    def __init__(self, name, address, age, s_id):
        Person.__init__(self, name, address, age)
        self._name = None
        self.s_id = s_id

    def do_homework(self):
        print(f"I'm doing my homework")

    def greet(self):
        print(f"I am", self.name, "and I'm a student")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_setter(self, value):
        self.__name = value


student = Student("Lee", "Atata", 33, "BI1111")
student.name_setter = "Yoyo"
student.greet()
