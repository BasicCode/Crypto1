#sum of primes finder
#Finds the longest run of consecutive primes which add together to equal another prime.
import math
import time

#Find primes up to a give value
#Sieve of Eratosthenes
def primesUpToN(n):
	isPrime = [True] * n
	for i in range(2, math.ceil(math.sqrt(n))):
		if(isPrime[i]):
			p = i
			for j in range(2, math.ceil((n / i))):
				p = p + i
				isPrime[p] = False
	return isPrime

#Print out the primes
start = time.time()
isPrime = primesUpToN(1000000)
stop = time.time()

counter = 0
for i in range(2, len(isPrime)):
	if(isPrime[i]):
		#print(i)
		counter = counter + 1

print("Found " + str(counter) + " in " + str(stop - start) + " seconds")