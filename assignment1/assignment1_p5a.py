__author__ = 'mdarmadi@ucsd.edu, A11410141, '
import sys
import operator

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
    # Initialized queue with the starting prime and the starting total cost
    # cost so far + distance to reach = 0 + heuristic
    # also track the cost so far (index 2)
    queue = [(startingPrime, heuristic(startingPrime, finalPrime) , 0)]

    # While the queue is not empty
    while queue:
        # Set the head of the queue to be the current node
        current = queue[0]

        # if the current node is the final prime we are looking for, return
        if current[0] == finalPrime:
            print "SUCCESS"
            print current[0]
            break

        # Else, we store the possible actions of the current number
        childOfNode = getPossibleActions(current[0])
        # Set the parent for each child
        for i in range(0, len(childOfNode)):
            closedList[str(childOfNode[i])] = current[0]

        print "Current is " + str(current)

        # Remove the current number
        queue.remove(current)

        # Add in the children of the removed prime
        for i in range(0, len(childOfNode)):
            # Calculate the distance to reach for each child
            heu = heuristic(childOfNode[i], finalPrime)
            # calculate the path length so far
            path = current[2] + 1
            # Append it to the queue with the updated cost
            queue.append((childOfNode[i], path + heu , path))
            # Sort the queue so it is like a priority queue
            # Sorts it by the second value, which is the cost
            queue.sort(key=operator.itemgetter(1))

        #print queue
        
        
    outputString = ""
    print "This is"
    print current[0]
    #if finalPrime is not found
    if current[0] != finalPrime :
        outputString =  'UNSOLVABLE'
    else: # print the found path
        curPrime = finalPrime
        outputString = str(curPrime) + ' ' +  outputString
        while(curPrime != startingPrime):
            curPrime = closedList[str(curPrime)]
            outputString = str(curPrime) + ' ' + outputString
		
    file = open('output.txt', 'w')
    print >> file, outputString
    print outputString
    file.close()

    return getPath

# Hamming distance heuristic
def heuristic(start, end):
    curList = list(str(start))
    finalList = list(str(end))

    # If the number entered are of different length. E.g 109 and 1999
    if (len(curList) - len(finalList)) != 0:
        return -1

    # Counter for hamming distance
    count = 0
    for i in range(0, len(curList)):
        if curList[i] != finalList[i]:
            count += 1

    return count

def main():
    # Replacing number in int ex. from 103 -> 203
    j = 103
    numj = str(j)
    listj = list(numj)
    listj[0] = '2'
    numj = ''.join(listj)

    path = getPossibleActions(109)
    heuList = {}
    # print(path)
    for i in range (0, len(path)):
        heuList[path[i]] = heuristic(path[i], 309)
    # print(heuList)

    primes = str(sys.stdin.readline()).split()
    getPath(int(primes[0]), int(primes[1]))

if __name__ == '__main__':
    main()
