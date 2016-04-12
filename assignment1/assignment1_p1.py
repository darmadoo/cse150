__author__ = 'mdarmadi@ucsd.edu, A11410141, '
import sys


allPrime = {} #allPrime is going to be a dictionary showing whether a number is prime
closedList = {} #closedList is going to e a dictionary showing whether a prime number has been visited or not

def isPrime(n):
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

# This method would return the list of prime
# numbers reachable from current prime .
# Note - this should not include the prime numbers
# which have already been processed, either in the
# frontier or in the closedlist.

def getPossibleActions(currentPrime):
    listOfPrimes = []

    currentStr = str(currentPrime)
    currentList = list(currentStr)
    length = len(currentList)   # this is the digit of the number

    # check every possible combination
    for i in range(0, length):
        curChar = currentList[i]
        for j in range(0,10): # possible digit replacement
            j = str(j)

            if(j == curChar): # to avoid repetition
                continue

            if (j == '0' and i == 0):    # to avoid producing leading 0
                continue

            currentList[i] = j          # replace the digit
            newStr = ''.join(currentList)
            newInt = int(newStr)            # might not need to convert to int if dictionary uses str for key

            #see if curInt is a prime
# 			if(allPrime[newInt] and not closedList[newInt]):
# 				listOfPrimes.append(newInt)
            if (isPrime(newInt)):
                listOfPrimes.append(newInt)

            currentList[i] = curChar # return currentList to original char

    print("possible actions: ")
    print(listOfPrimes)

    return listOfPrimes


def getPath(startingPrime, finalPrime):
    # your code here
    return getPath

def main():
    allNum = []
    for x in range(2, 1000001):
        allNum.append(x)

    for i in allNum:
        if isPrime(i):
            allPrime[i] = True
        else:
            allPrime[i] = False

    # Replacing number in int ex. from 103 -> 203
    j = 103
    numj = str(j)
    listj = list(numj)
    listj[0] = '2'
    numj = ''.join(listj)


    primes = str(sys.stdin.readline()).split()
    getPossibleActions(89)


if __name__ == '__main__':
    main()
