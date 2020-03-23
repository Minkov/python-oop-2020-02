#
# def my_sum(*args):
#     return sum(args)
#
# def sum_of_even(*args):
#     return my_sum(*get_even(args))
#
# def sum_of_even(*args):
#     return my_sum(args)
#
# def get_even(*args):
#     return list(filter(lambda x: x % 2 == 0, args))
#
# print(my_sum(*get_even(1, 2, 3)))
from time import time


def uppercase(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper


@uppercase
def say_hi():
    return 'Hello'

@uppercase
def log():
    return f'Error'

print(log())
print(say_hi())

# def exception_logger(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as ex:
#             with open('decorators.log', 'a') as file:
#                 file.write(f'{ex} thrown from {func.__name__}\n')
#             raise ex
#     return wrapper

def measure_performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end = time()
            print(f'{func.__name__} executed for {end-start} seconds')

    return wrapper

def exception_logger(file='logs.log'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as ex:
                # with open(file, 'a') as log_file:
                #     log_file.write(f'{ex} thrown from {func.__name__}\n')
                print(f'{ex} thrown from {func.__name__}')
                raise ex
        return wrapper
    return decorator

@exception_logger(file='./decorators.log')
@measure_performance
def my_multiply(x, y):
    # return 2 * 3
    return x * y

@exception_logger()
def throws():
    raise ValueError

# throws()
print(my_multiply(2, 3))
print(my_multiply('Pesho', 'Gosho'))
