class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __validate_age(self, age):
        if age < 0 or age > 125:
            raise ValueError('Invalid age value')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__validate_age(age)
        self.__age = age

person = Person("George", 32)
person.__name = 'Pesho'

person2 = Person('Peter', 33)
print(person.__dict__)
print(person2.__dict__)
