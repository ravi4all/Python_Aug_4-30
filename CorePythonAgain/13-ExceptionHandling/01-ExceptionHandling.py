num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

try:
    result = int(num_1) / int(num_2)
    print(result)
except ZeroDivisionError as er:
    print("{} Error Occured".format(er))

