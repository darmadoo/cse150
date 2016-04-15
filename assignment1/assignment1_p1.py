__author__ = 'mdarmadi@ucsd.edu, A11410141, hdharmaw@ucsd.edu, A91413023, vcchandr@ucsd.edu, A12496582'
import sys
import time

closedList = {} # closedList is going to be a dictionary showing the parent of number
frontier = [] # list of nodes (number) ready to be explored

def isPrime(n):
    if n == 0 or n == 1:
         return False
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

            # check if new integer is prime and not in closedList already
            if (isPrime(newInt)):
                if (not newInt in closedList):
                    listOfPrimes.append(newInt)

            currentList[i] = curChar # return currentList to original char

    return listOfPrimes


def getPath(startingPrime, finalPrime):
    possibleAction = (getPossibleActions(startingPrime))
    frontier = possibleAction

    # if it takes only one digit to change from starting --> final prime
    if (finalPrime in frontier):
        outputString = str(startingPrime) + " " + str(finalPrime)

        file = open('output.txt', 'w')
        print >> file, outputString
        print outputString
        file.close()
        return

    for i in range(0, len(frontier)): # indicate who the parent is
        closedList[frontier[i]] = startingPrime

    while (frontier): # until no discoverable nodes
        currentNode = frontier[0]
        childOfNode = getPossibleActions(currentNode)

        if (finalPrime in childOfNode): # if we can find the final prime
            outputString = str(finalPrime)
            while currentNode != startingPrime:
                outputString = str(currentNode) + " " + outputString
                currentNode = closedList[currentNode]
            outputString = str(startingPrime) + " " + outputString
            file = open('output.txt', 'w')
            print >> file, outputString
            print outputString
            file.close()
            return

        for i in range(0, len(childOfNode)): # indicate who the parent is
            closedList[childOfNode[i]] = currentNode

        frontier.remove(currentNode)

        additionalNodes = childOfNode
        for i in range(0, len(childOfNode)):
            if (childOfNode[i] in frontier):
                additionalNodes.remove(childOfNode[i])

        for i in range(0, len(additionalNodes)):
            frontier.append(additionalNodes[i])

    file = open('output.txt', 'w')
    print >> file, 'UNSOLVABLE'
    print "UNSOLVABLE"
    file.close()

    return getPath

def main():
    primes = str(sys.stdin.readline()).split()
    first = list(primes[0])
    second = list(primes[1])
    if len(first) - len(second) == 0:
        t0 = time.time()
        getPath(int(primes[0]), int(primes[1]))
    else:
        outputString = 'UNSOLVABLE'
        ofile = open('output.txt', 'w')
        print >> ofile, outputString
        print outputString
        ofile.close()
    t1 = time.time()
    print t1 - t0

if __name__ == '__main__':
    main()
