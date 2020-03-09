class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __validate_age(self, age):
        if age < 0 or age > 125:
            raise ValueError('Invalid age value')

    def __set_name(self, name):
        if not name or len(name) < 5:
            raise ValueError('Name is too short')
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__validate_age(age)
        self.__age = age

    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, name):
    #     self.__name = name
    #
    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, age):
    #     self.__validate_age(age)
    #     self.__age = age


person = Person("George", 11)

print(person.name)
