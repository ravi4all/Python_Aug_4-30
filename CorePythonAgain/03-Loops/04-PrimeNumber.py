import time
# num = int(input("Enter a number : "))

minRange = int(input("Enter starting range : "))
maxRange = int(input("Enter end range : "))

start = time.time()
print("Starting time",start)
for num in range(minRange, maxRange):

    for i in range(2,num):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            break
    else:
        print("{} is a prime number".format(num))

end = time.time()
print("End time", end)
print("Total time was",end-start)
