# def add(x,y):
#     return x+y
#
# def sub(x,y):
#     return x-y
#
# def div(x,y):
#     return x/y
#
# def mul(x,y):
#     return x*y

# print(add(2,5))
# print(sub(5,2))
# print(div(4,8))
# print(mul(11,5))

def calc(x,y):
    return x+y, x-y, x*y, x/y

# print(calc(12,5))

# calculator = calc(12,5)
# print(calculator)

add,sub,mul,div = calc(12,5)
print(add, sub, div, mul)
