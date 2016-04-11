__author__ = 'mdarmadi@ucsd.edu, A11410141, '
import sys

allPrime = []

def isprime(n):
    # if n < 2:
    #     return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def getPossibleActions(currentPrime):
	# This method would return the list of prime
	# numbers reachable from current prime .
	# Note - this should not include the prime numbers
	# which have already been processed, either in the
	# frontier or in the closedlist.
	return listOfPrimes


def getPath(startingPrime, finalPrime):
	# your code here
	return getPath

def main():
	allNum = []
	for x in range(2, 1000001):
		allNum.append(x)

	for i in allNum:
		if isprime(i):
			allPrime.append(i)

	primes = str(sys.stdin.readline()).split()
	print(getPath(primes[0], primes[1]))


if __name__ == '__main__':
	main()
