def custom_range(min, max):
    index = min
    while index <= max:
        yield index
        index += 1

it = custom_range(1, 2)
print(next(it))
print(next(it))

print((x for x in range(3)))

even = filter(lambda x: x % 2 == 0, range(10))
for x in even:
    print(x)