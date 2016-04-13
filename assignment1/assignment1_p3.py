# _ _author_ _ = 'mdarmadi@ucsd.edu, A11410141, '
import sys
from Queue import LifoQueue

closedList = {} # closedList is going to be a dictionary showing the parent of number
MAXDEPTH = 8

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

    #print("possible actions for " + str(currentPrime) + " is: " + str(listOfPrimes))
    return listOfPrimes


def getPath(startingPrime, finalPrime,depth):
	# your code here
	#reset the closed list for fresh search
	closedList.clear()	
	#declare stack
	stack = LifoQueue()
	
	#push <startingPrime (currentPrime), 0 (depth)> into the stack
	stack.put((startingPrime , 0))
	
	#while stack is not empty 
	while(not stack.empty()):
		#pop a from stack
		a = stack.get()

		#if a.currentPrime == finalPrime
		if(a[0] == finalPrime):
			break
		#else if a.depth >= 5
		elif(a[1] >= depth):
			continue
		
		#find all neighbor of currentPrime
		neighbor = getPossibleActions(a[0])
		
		for i in range(0,len(neighbor)):
			#set the parent of the neighbor to currentPrime
			closedList[str(neighbor[i])] = a[0]
			#push all neighbor as <neighbor,a.depth + 1> into the stack
			stack.put((str(neighbor[i]),a[1] + 1))
		
	
	#if(currentPRime != finalPrime)
	if(a[0] != finalPrime):
		#unsolvable
		return False		
	else:
		return True

def getIterativePath(startPrime, finalPrime):
	for i in range(0, MAXDEPTH+1):
		result = getPath(startPrime, finalPrime, i)
		if(result):
			break
	
	if(result == False):
		outputString = 'UNSOLVABLE'
	else:
		current = finalPrime
		outputString = ""
		outputString = current + " " + outputString
		while(current != startPrime):
			current = closedList[current]
			outputString = current + " " + outputString
	
	file = open('output.txt','w')
 	print >> file,outputString
	print(outputString)
	file.close()
	return 	

def main():
	primes = str(sys.stdin.readline()).split()
	getIterativePath(primes[0], primes[1])


if __name__ == '__main__':
	main()