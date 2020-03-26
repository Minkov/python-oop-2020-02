class Student:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Name cannot be None')

        self.__name = value

    def get_info(self):
        return f'Hello, I am {self.name}'


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students_info(self):
        return [s.get_info() for s in self.students]


class Database:
    def add(self, obj):
        pass


class SchoolDatabase:
    def __init__(self, db):
        self.db = db

class MockDatabase:
    def add(self, obj):
        pass

# production
sdb = SchoolDatabase(Database())

# testing
sdb = SchoolDatabase(MockDatabase())
