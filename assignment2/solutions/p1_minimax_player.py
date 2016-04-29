# -*- coding: utf-8 -*-
__author__ = 'hdharmaw@ucsd.edu, A91413023, mdarmadi@ucsd.edu, A11410141, vcchandr@ucsd.edu, A12496582'


from assignment2 import Player, State, Action
import sys
import time

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        #t0 = time.time()
        best_act = None
        best_v = -sys.maxint

        for actions in state.actions():
            t = self.minVal(state.result(actions))

            if best_v < t:
                best_v = t
                best_act = actions
                
        #t1 = time.time()
        #print "Time: " + str(t1-t0)
        return best_act

    def minVal(self, state):
        if state.is_terminal():
            return state.utility(self)

        v = sys.maxint

        if not state.actions():
            v = min(v, self.maxVal(state.result(None)))
        else:
            for a in state.actions():
                v = min(v, self.maxVal(state.result(a)))

        return v

    def maxVal(self, state):
        if state.is_terminal():
            return state.utility(self)

        v = -sys.maxint

        if not state.actions():
            v = max(v, self.minVal(state.result(None)))
        else:
            for a in state.actions():
                v = max(v, self.minVal(state.result(a)))

        return v
