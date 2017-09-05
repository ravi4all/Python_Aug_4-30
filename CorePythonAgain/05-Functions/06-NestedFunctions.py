# Closures

def outer(msg):
    message = msg
    def inner():
        # print("Message was",message)
        return message + ' Python'
    return inner
    # print(inner())

# outer("Hello world")

# print(outer("Hello"))

a = outer("Hello")

print(a())
print(type(a))
