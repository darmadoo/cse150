# -*- coding: utf-8 -*-

from collections import deque

import time

#from p1_is_complete import  is_complete
#from p2_is_consistent import is_consistent
#from p4_ac3 import ac3
#from p4_ac3 import revise
from p5_ordering import select_unassigned_variable
#from p3_basic_backtracking import select_unassigned_variable
from p5_ordering import order_domain_values
#from p3_basic_backtracking import order_domain_values


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())
    #return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    t0 = time.time()
    if backtrack(csp):
        t1 = time.time()
        print "execution time: " + str(t1 -t0)
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO copy from p3
    
    if is_complete(csp):  #if assigment is completed, return true
        return True
    #t3 = time.time()
    var = select_unassigned_variable(csp)
    #t4 = time.time()
    #print "Selecting: " + str(t4 - t3)
    #print var
    
    ordered = order_domain_values(csp, var)
    #print ordered
    
    for value in ordered:
        csp.variables.begin_transaction()
        #print var
        if is_consistent(csp, var, value):            
            var.assign(value)   #add var=value to assignment
            #print "Assigned " + str(value) + " to " + str(var)
            inferences = inference(csp, var) # get the inferences
            if(inferences):
                #add inferences to assignment???
                #need to implement above!!!!   already implemented when running ac3??
                result = backtrack(csp)
                if(result):
                    return result
        #print "call rollback"
        csp.variables.rollback()
        #print csp.variables
    
    return False


def is_complete(csp):
    """Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""

    # Hint: The list of all variables for the CSP can be obtained by csp.variables.
    # Also, if the variable is assigned, variable.is assigned() will be True.
    # (Note that this can happen either by explicit assignment using variable.assign(value),
    # or when the domain of the variable has been reduced to a single value.)

    # TODO implement this
    for i in csp.variables:
        if not i.is_assigned():
            return False

    return True

    pass


def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""

    #t0 = time.time()

    # TODO implement this
    for constraint in csp.constraints[variable]:
        if constraint.var2.is_assigned():
            if not constraint.is_satisfied(value, constraint.var2.value):
                return False

    #t1 = time.time()
    #print "Execution time for is_consistent: " + str(t1 - t0)

    return True

    pass


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    # TODO implement this
    while (queue_arcs):
        (xi, xj) = queue_arcs.pop()

        if revise(csp, xi, xj):
            if (len(xi.domain) == 0 or xi.domain is None):
                return False

            for const in csp.constraints[xi]:
                xk = const.var2
                if not (xk == xi or xk == xj):
                    pair = (xk, xi)
                    queue_arcs.append(pair)

    return True
    pass

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.

    revised = False
    newdomain = xi.domain[:]

    for x in xi.domain:
        const = False
        for y in xj.domain:
            for constraint in csp.constraints[xi, xj]:
                if constraint.is_satisfied(x, y):
                    const = True
                    break # break out of constraint loop

            if const:
                break # break out of y xj.domain loop

        if not const:
            newdomain.remove(x)
            revised = True
            
    xi.domain = newdomain[:]
    return revised

    pass

