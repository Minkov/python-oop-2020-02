# def f1():
#     print(1)
#
#
# def execute_operation(func):
#     print(f'Started execution of {func.__name__}')
#     func()
#     print(f'Execution of {func.__name__} ended')
#
#
# execute_operation(f1)
# execute_operation(lambda: print(2))


def sum2(x):
    def sum_internal(y):
        return x + y + z

    return sum_internal


sum3 = sum2(3)
sum4 = sum2(4)
print(sum3(2))
print(sum4(2))
