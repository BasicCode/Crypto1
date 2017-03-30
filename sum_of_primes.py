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

#Find the longest sum of primes possible
def sumOfPrimes(isPrime):
	#Turn the array of indexes in to an array of numbers
	primes = []
	for i in range(2, len(isPrime)):
		if(isPrime[i]):
			primes.append(i)
	
	numPrimes = len(primes)
	
	#test each sequence of primes up to half the total number of primes
	sums = []
	highest_prime = 0
	for i in range(0, math.ceil(numPrimes / 2)):
		testSum = 0
		sumSequence = []
		#sum a sequence of primes
		j = i
		while testSum < primes[-1] - highest_prime:
			testSum = testSum + primes[j]
			sumSequence.append(primes[j])
			#if the sum is TRUE in the array then it is a prime
			if(isPrime[testSum]):
				print(sumSequence)
				print(testSum)
				sums.append(sumSequence)
				highest_prime = sumSequence[-1]
			j = j + 1
		
	return sums

#Print out the primes
print("Finding primes...")
start = time.time()
isPrime = primesUpToN(1000)
stop = time.time()

print("Finding sum of primes...")
sums = sumOfPrimes(isPrime)

print("Found " + str(len(primes)) + " in " + str(stop - start) + " seconds")
print(sums)