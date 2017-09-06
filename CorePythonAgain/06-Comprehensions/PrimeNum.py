import time

start = time.time()

noprimes = [j for i in range(2,8) for j in range(i*2, 15000, i)]

primes = [x for x in range(2,15000) if x not in noprimes]

end = time.time()

print(primes)
print("Total time",end - start)
