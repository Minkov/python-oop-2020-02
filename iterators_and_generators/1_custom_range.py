class custom_range_iterator:
    def __init__(self, first, last):
        self.index = first
        self.last = last

    def __next__(self):
        if self.index > self.last:
            raise StopIteration
        index = self.index
        self.index += 1
        return index


class custom_range:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        # return iter(range(self.first, self.last + 1))
        return custom_range_iterator(self.first, self.last)

cr = custom_range(1, 4)

it1 = iter(cr)
print(next(it1)) # 1
it2 = iter(cr)
print(next(it1)) # 2
print(next(it2)) # 1

print(''.join(str(x) for x in cr))
print(''.join(str(x) for x in cr))