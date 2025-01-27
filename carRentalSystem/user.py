class User:
    def __init__(self, user_id, name, email, role):
        self.__user_id = user_id  # Encapsulation
        self.__name = name
        self.__email = email
        self.__role = role  # 'customer' or 'admin'

    # Getters and setters
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_role(self):
        return self.__role

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def display_info(self):
        print(f"User: {self.__name}, Email: {self.__email}, Role: {self.__role}")


