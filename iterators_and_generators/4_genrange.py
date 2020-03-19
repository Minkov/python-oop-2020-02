def genrange(min, max):
    for x in range(min, max + 1):
        yield x

print(list(genrange(1, 10)))
