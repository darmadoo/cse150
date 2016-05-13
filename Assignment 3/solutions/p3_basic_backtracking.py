# -*- coding: utf-8 -*-

#from p1_is_complete import is_complete
#from p2_is_consistent import  is_consistent

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
    
    for value in order_domain_values(csp, var):
        csp.variables.begin_transaction()

        if is_consistent(csp, var, value):            
            var.assign(value)   #add var=value to assignment

            if backtrack(csp):
                return True
            # inferences = inference(csp, var) # get the inferences
            # if(inferences):
            #     #add inferences to assignment???
            #     #need to implement above!!!!
            #     result = backtrack(csp)
            #     if(result):
            #         return result
        csp.variables.rollback()
    
    return False
    pass



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




