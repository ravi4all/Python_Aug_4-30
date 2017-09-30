try:
    file = open("file.txt")
    print(file.read())
    # print("Hello world")

except:
    print("Error")

finally:
    file.close()
    print("I will execute...")
