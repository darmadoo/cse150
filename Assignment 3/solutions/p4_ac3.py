# -*- coding: utf-8 -*-

from collections import deque


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