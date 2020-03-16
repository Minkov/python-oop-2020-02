def execute(func, *args):
    return func(*args)

execute(print, 1, 2, 3)

print(list(execute(map, lambda x: x + 1, [1, 2, 3, 4, 5])))

def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

execute(say_hello, "Peter", "George") # Hello, Peter, I am George
execute(say_bye, "Peter")