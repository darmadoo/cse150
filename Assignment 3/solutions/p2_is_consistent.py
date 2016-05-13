# -*- coding: utf-8 -*-

import time

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
