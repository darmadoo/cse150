# -*- coding: utf-8 -*-

from collections import deque

import time

from p1_is_complete import  is_complete
from p2_is_consistent import is_consistent
from p5_ordering import select_unassigned_variable
from p5_ordering import order_domain_values


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


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
    
    var = select_unassigned_variable(csp)
    #print var
    
    for value in order_domain_values(csp, var):
        csp.variables.begin_transaction()
        # print var

        if is_consistent(csp, var, value):            
            var.assign(value)   #add var=value to assignment


            inferences = inference(csp, var) # get the inferences
            if(inferences):
                #add inferences to assignment???
                #need to implement above!!!!   already implemented when running ac3??
                result = backtrack(csp)
                if(result):
                    return result
        csp.variables.rollback()
    
    return False


def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    # TODO copy from p4
    while (queue_arcs):
        (xi, xj) = queue_arcs.pop()

        if revise(csp, xi, xj):
            if len(xi.domain) == 0 or xi.domain is None:
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

