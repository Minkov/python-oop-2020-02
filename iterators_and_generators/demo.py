ll = [1, 2, 3, 4]

# for x in ll:
#     print(x)
#
# [print(x) for x in ll]

it = iter(ll)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

print(list(map(str, [1, 2, 3, 4])))
