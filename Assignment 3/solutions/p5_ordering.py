# -*- coding: utf-8 -*-
import operator
from operator import itemgetter
from p1_is_complete import is_complete

import sys

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """
    # TODO implement this


    if is_complete(csp):
        return True

    unassignedList = []
    unassignedFlag = False
    min_val = sys.maxint

    for variable in csp.variables:
        if not variable.is_assigned():
            if len(variable.domain) == min_val:
                unassignedList.append(variable)
                unassignedFlag = True

            elif len(variable.domain) < min_val:
                unassignedList = [variable]
                min_val = len(variable.domain)
                unassignedFlag = True

    if unassignedFlag:
        if (len(unassignedList)) == 1:
            return unassignedList[0]

        else:
            max_constraint = -sys.maxint
            var = None
            for variable in unassignedList:
                count = 0 
                for constraint in csp.constraints[variable]:               
                    if not constraint.var2.is_assigned():   #count only the unassigned variables
                        count += 1
                        
                if count > max_constraint:
                    var = variable
                    max_constraint = count
            
            return var


        #
        # sortList = sorted(unassignedList, key=itemgetter(1))
        # front = sortList[0]
        # tieList = []
        # tieList.append(front)
        # if(len(sortList) > 1):
        #     for var in range(1, len(sortList)):
        #         if front[1] == sortList[var][1]:
        #             tieList.append(sortList[var])
        #         else:
        #             break
        #
        #  #No repeat take the head
        # if len(tieList) == 1:
        #     return front[0]
        # else:
        #     maxVar = max(tieList, key=lambda i:len(csp.constraints[i[0]]))
        #     #print "maxVar: " + str(maxVar[0])
        #     return maxVar[0]
        # #return front[0]

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
    #print sortedList
    return newList

    pass
