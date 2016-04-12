__author__ = 'mdarmadi@ucsd.edu, A11410141, '
import sys


allPrime = {} #allPrime is going to be a dictionary showing whether a number is prime
closedList = {} # closedList is going to be a dictionary showing the parent of number
frontier = [] # list of nodes (number) ready to be explored

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

            # check if new integer is prime and not in closedList already
            if (isPrime(newInt)):
                if (not newInt in closedList):
                    listOfPrimes.append(newInt)

            currentList[i] = curChar # return currentList to original char

    print("possible actions for " + str(currentPrime) + " is: " + str(listOfPrimes))
    return listOfPrimes


def getPath(startingPrime, finalPrime):

    possibleAction = (getPossibleActions(startingPrime))
    frontier = possibleAction

    for i in range(0, len(frontier)): # indicate who the parent is
        closedList[frontier[i]] = startingPrime

    print("frontier: " + str(frontier))
    print("closed list: " + str(closedList))

    while (frontier): # until no discoverable nodes
        currentNode = frontier[0]
        childOfNode = getPossibleActions(currentNode)

        print("child of node " + str(currentNode) + " is: " + str(childOfNode))

        if (finalPrime in childOfNode): # if we can find the final prime
            outputString = str(finalPrime)
            while currentNode != startingPrime:
                outputString = str(currentNode) + " " + outputString
                currentNode = closedList[currentNode]
            outputString = str(startingPrime) + " " + outputString

            file = open('output.txt', 'w')
            print >> file, outputString
            file.close()

            return








    file = open('output.txt', 'w')
    print >> file, 'UNSOLVABLE'
    file.close()


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
    getPath(89, 11)


if __name__ == '__main__':
    main()
