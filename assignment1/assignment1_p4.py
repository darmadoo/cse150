__author__ = 'mdarmadi@ucsd.edu, A11410141, hdharmaw@ucsd.edu, A91413023, vcchandr@ucsd.edu, A12496582'
import sys
import time

closedList = {} # closedList is going to be a dictionary showing the parent of number
closedList2 = {} # closedList from the final prime

frontier = [] # list of nodes (number) ready to be explored
frontier2 = [] # list of nodes ready to be explored from the final prime

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
def getPossibleActions(currentPrime, isStarting):
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
                if (isStarting):
                    if (not newInt in closedList):
                        listOfPrimes.append(newInt)

                else:
                    if (not newInt in closedList2):
                        listOfPrimes.append(newInt)

            currentList[i] = curChar # return currentList to original char

    return listOfPrimes


def getPath(startingPrime, finalPrime):
    possibleAction = (getPossibleActions(startingPrime, True))
    frontier = possibleAction

#     print("starting number: " + str(startingPrime))
#     print("frontier 1: " + str(frontier))

    # if it takes only one digit to change from starting --> final prime
    if (finalPrime in frontier):
        outputString = str(startingPrime) + " " + str(finalPrime) + "\n" + str(finalPrime)

#         file = open('output.txt', 'w')
#         file.write(outputString)
#         file.close()
        sys.stdout.write(outputString)
        return

    for i in range(0, len(frontier)): # indicate who the parent is
        closedList[frontier[i]] = startingPrime
    closedList[startingPrime] = startingPrime



    frontier2 = getPossibleActions(finalPrime, False)
    #print("frontier 2: " + str(frontier2))

    for i in range(0, len(frontier2)):  # indicate who the parent is
        closedList2[frontier2[i]] = finalPrime
    closedList2[finalPrime] = finalPrime

    while (frontier or frontier2): # until no discoverable nodes from both sides
        # STARTING FROM THE BACK
        if frontier2: # if final prime still has descendants
            currentNode = frontier2[0]
            childOfNode = getPossibleActions(currentNode, False) # indicate that it is from the back

#             print("currentNode: " + str(currentNode))
#             print("child of nodes HERE: " + str(childOfNode))

            for i in range(0, len(childOfNode)):
                if (childOfNode[i] in closedList):
                    #print("found child of node: " + str(childOfNode[i]))
                    copyCurrent = currentNode # for backtracking until finish prime
                    currentNode = childOfNode[i]
                    line1 = ""
                    line2 = str(childOfNode[i])
                    while currentNode != startingPrime: # backtrack starting prime
                        line1 = str(currentNode) + " " + line1
                        currentNode = closedList[currentNode]
                    line1 = str(startingPrime) + " " + line1
                    #print("get here 1")
                    while copyCurrent != finalPrime: # backtrack final prime
                        line2 = str(copyCurrent) + " " + line2
                        copyCurrent = closedList2[copyCurrent]
                    line2 = str(finalPrime) + " " + line2
                    #print("get here 2")

#                     file = open('output.txt', 'w')
#                     print >> file, line1 + "\n" + line2
#                     file.close()
                    sys.stdout.write(line1 + "\n" + line2)
                    return

            for i in range(0, len(childOfNode)):  # indicate who the parent is
                closedList2[childOfNode[i]] = currentNode

            frontier2.remove(currentNode)

            additionalNodes = childOfNode[:]
#             print("")
#             print("child of nodes: " + str(childOfNode))
#             print("additional nodes: " + str(additionalNodes))
            for k in range(0, len(childOfNode)):
                if (childOfNode[k] in frontier2):
                    additionalNodes.remove(childOfNode[k])

            for i in range(0, len(additionalNodes)):
                frontier2.append(additionalNodes[i])

            #print("frontier 2: " + str(frontier2))

        if frontier:
            # CHECK FROM FRONT
            currentNode = frontier[0]
            childOfNode = getPossibleActions(currentNode, True)

#             print("current Node: " + str(currentNode))
#             print("child Of Nodeee: " + str(childOfNode))

            for i in range(0, len(childOfNode)):
                if (childOfNode[i] in closedList2): # if we can find the final prime
#                     print("found child of node: " + str(childOfNode[i]))
                    copyCurrent = childOfNode[i]
                    line1 = str(childOfNode[i])
                    line2 = ""
                    while currentNode != startingPrime:  # backtrack starting prime
                        line1 = str(currentNode) + " " + line1
                        currentNode = closedList[currentNode]
                    line1 = str(startingPrime) + " " + line1
#                     print("copy current: " + str(copyCurrent))
                    while copyCurrent != finalPrime:  # backtrack final prime
                        line2 = str(copyCurrent) + " " + line2
                        copyCurrent = closedList2[copyCurrent]
                    line2 = str(finalPrime) + " " + line2

#                     file = open('output.txt', 'w')
#                     print >> file, line1 + "\n" + line2
#                     file.close()
                    sys.stdout.write(line1 + "\n" + line2)
                    return

            for i in range(0, len(childOfNode)): # indicate who the parent is
                closedList[childOfNode[i]] = currentNode

            frontier.remove(currentNode)

            additionalNodes = childOfNode[:]
            for i in range(0, len(childOfNode)):
                if (childOfNode[i] in frontier):
                    additionalNodes.remove(childOfNode[i])

            for i in range(0, len(additionalNodes)):
                frontier.append(additionalNodes[i])


#     file = open('output.txt', 'w')
#     print >> file, 'UNSOLVABLE'
#     file.close()
    sys.stdout.write('UNSOLVABLE')

    return getPath

def main():
    primes = str(sys.stdin.readline()).split()
    t0 = time.time()
    getPath(int(primes[0]), int(primes[1]))
    t1 = time.time()
    #print t1 - t0

if __name__ == '__main__':
    main()
