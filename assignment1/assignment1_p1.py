__author__ = 'mdarmadi@ucsd.edu, A11410141, '
import sys

#allPrime is going to be a dictionary showing whether a number is prime
allPrime = []

#closedList is going to e a dictionary showing whether a prime number has been visited or not 
closedList = {}	

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
	
	length = 0
	listOfPrimes = []
	
	currentStr = str(currentPrime)
	currentList = list(currentStr)
	length = len(currentList)   #this is the length of the number
	
	#check every possible combination
	for i in range(0, length):
		curChar = currentList[i]
		for j in range(0,10):
			j = str(j)
			if(j == curChar):
				continue
			currentList[i] = j
			newStr = ''.join(currentList)
			newInt = int(newStr)            #might not need to convert to int if dictionary uses str for key
			
			#see if curInt is a prime
# 			if(allPrime[newInt] and not closedList[newInt]):
# 				listOfPrimes.append(newInt)
			print(newStr)
						
			# return currentList to original char
			currentList[i] = curChar
	
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
			allPrime['key'] = value
	primes = str(sys.stdin.readline()).split()
	getPossibleActions(113)


if __name__ == '__main__':
	main()
