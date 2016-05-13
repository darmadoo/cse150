# -*- coding: utf-8 -*-

from p1_is_complete import is_complete
from p2_is_consistent import  is_consistent

import time

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
    """
    t0 = time.time()
    
    if backtrack(csp):
        t1 = time.time()
        print "Execution time for simple backtrack: " + str(t1 - t0)
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """
    #implement the algorithm in slide 11-12 ch6
    # TODO implement this
    if is_complete(csp):  #if assigment is completed, return true
        return True
    
    var = select_unassigned_variable(csp)
    print var
    
    for value in order_domain_values(csp, var):
        csp.variables.begin_transaction()
        

        if is_consistent(csp, var, value):            
            var.assign(value)   #add var=value to assignment

            inferences = inference(csp, var) # get the inferences
            if(inferences):
                #add inferences to assignment???
                #need to implement above!!!!
                result = backtrack(csp)
                if(result):
                    return result
        csp.variables.rollback()
    
    return False
    pass



