# # function
def f1():
    return 'This is the function `f1`'

#

# ll = [f1, 1]
# [print(x.__str__()) for x in ll]

class Food:
    def __init__(self, type):
        self.type = type

# print(Food('banana').__str__())

#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def eat(self):
#         banana = Food('banana')
#         print(f'{self.name} eats {banana.type}')
#
#     # method
#     def __str__(self):
#         return f'I am {self.name} and I am a {self.species}'
#
#
# a1 = Animal('Gosho', 'dog')
# a2 = Animal('Ivan', 'cat')
#
# a1.eat()
# a2.eat()
#
# print(a1)
# print(a2)


class Laptop:
    def __init__(self, model, brand, ram=None):
        self.model = model
        self.brand = brand
        self.ram = ram

    def set_ram(self, ram):
        self.ram = ram

    def __str__(self):
        return f'{self.model}; {self.brand}; {self.ram}'

#
#
# asus = Laptop('rog', 'Asus')
# asus_set_ram = asus.set_ram
# asus_set_ram(7)
# print(f1)
# print(asus_set_ram)
# print(asus)

#
# print(asus)
#
# asus.set_ram(17)
# print(asus)


def print_param(p):
    print(p)


def handle_func(func):
    func(1)

asus = Laptop('rog', 'Asus')
handle_func(print_param)
handle_func(asus.set_ram)
print(asus)