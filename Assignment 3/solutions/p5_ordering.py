# -*- coding: utf-8 -*-
import operator
from operator import itemgetter

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this
    unassignedList = []
    unassignedFlag = False
    print "start ordering"

    for variable in csp.variables:
        if not variable.is_assigned():
            unassignedList.append((variable , len(variable.domain)))
            unassignedFlag = True

    if unassignedFlag:
        sortList = sorted(unassignedList, key=itemgetter(1))
        #print "sorted list:"
        #print sortList
        front = sortList[0]
        #print "Front: " + str(front)
        tieList = []
        tieList.append(front)
        if(len(sortList) > 1):
            for var in range(1, len(sortList)):
                if front[1] == sortList[var][1]:
                    tieList.append(sortList[var])
                else:
                    break    
#         if(len(sortList) > 1):
#             i = 1
#             while (i < len(sortList)):
#                 if(len(front.domain) < len(sortList[i].domain)):
#                     break
#                 tieList.append(sortList[i])
#                 i += 1

         #No repeat take the head
        if len(tieList) == 1:
            return front[0]
        else:
#             maxCon = -1
#             for x in tieList:
#                 if len(csp.constraints[x[0]]) > maxCon:
#                      maxCon = len(csp.constraints[x[0]])
#                      maxVar = x
            maxVar = max(tieList, key=lambda i:len(csp.constraints[i[0]]))
            #print "maxVar: " + str(maxVar[0])
            return maxVar[0]
        #return front[0]
    else:   # When all the variables are assigned
        return None

    pass


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # TODO implement this
    orderDict = {}
    domain = variable.domain

    for i in domain:
        orderDict[i] = 0

    # print orderDict

    for constraint in csp.constraints[variable]:
        curDomain = constraint.var2.domain
        for i in curDomain:
            if i in orderDict:
                orderDict[i] += 1
    newList = []
    sortedList = sorted(orderDict.items(), key=operator.itemgetter(1))
    for i in sortedList:
        newList.append(i[0])
    #print "newline"
    #print newList
    return newList

    pass
