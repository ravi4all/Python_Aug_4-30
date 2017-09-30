try:
    file = open("file.txt")
    print(file.read())
    # print("Hello world")

except:
    print("Error")

else:
    print("I will execute...")
