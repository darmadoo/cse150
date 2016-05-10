# -*- coding: utf-8 -*-
import operator

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

    for variable in csp.variables:
        if not variable.is_assigned():
            unassignedList.append(variable)
            unassignedFlag = True

    if unassignedFlag:
        sortList = sorted(unassignedList, key=lambda temp: temp.domain)
        front = sortList[0]
        n = 0
        tieList = []
        tieList.append(front)
        for var in range(1, len(sortList)):
            if len(front.domain) == len(sortList[var].domain):
                n += 1
                tieList.append(sortList[var])

        # No repeat take the head
        if n == 0:
            return front
        else:
            maxCon = -1
            for x in tieList:
                if len(csp.constraints[x]) > maxCon:
                    maxCon = len(csp.constraints[x])
                    maxVar = x
            return maxVar
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

    print orderDict

    for constraint in csp.constraints[variable]:
        curDomain = constraint.var2.domain
        for i in curDomain:
            if i in orderDict:
                orderDict[i] += 1
    newList = []
    sortedList = sorted(orderDict.items(), key=operator.itemgetter(1))
    for i in sortedList:
        newList.append(i[0])

    return newList

    pass
