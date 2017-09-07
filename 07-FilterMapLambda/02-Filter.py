a = [x for x in range(50)]

def even(e):
    return e%2 == 0

num = list(filter(even, a))

print(num)
