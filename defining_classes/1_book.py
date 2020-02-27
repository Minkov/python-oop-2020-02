class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

class Person:
    def __init__(self, first_name, last_name):
        self.full_name = f'{first_name} {last_name}'

    def get_max_age(self):
        return 101

print(Book('xxxx', 'yyyyy', 3).__dict__)
