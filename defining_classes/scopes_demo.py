x = 5


def f(x):
    x = 6

    def f1():
        x = 7
        return x

    print(x)
    x = f1()
    print(x)
    return x


print(x)
x = f(x)
print(x)
