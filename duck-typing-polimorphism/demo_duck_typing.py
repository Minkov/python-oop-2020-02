def f(a):
    print(a.size)


class C1:
    size = 1


class C2:
    def __init__(self, size):
        self.size = size

class MyClass:
    def __init__(self, size):
        self.size = size
    def __len__(self):
        return self.size

def f(obj):
    if "__len__" not in dir(obj):
        raise TypeError
    # do the work

f(MyClass(3))
print(len("peter")) # 5
print(len([10, 20, 30])) # 3
print(len(MyClass(4))) # 4
print(len(MyClass(3))) # 3
