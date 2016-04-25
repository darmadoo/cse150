# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action
import sys

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
        best_act = None
        best_v = -sys.maxint

        for actions in state.actions():
            v = self.minVal(state.result(actions))
            if best_v < v:
                best_v = v
                best_act = actions

        print "FINAL"
        print best_act
        print best_v
        return best_act

    def minVal(self, state):
        if state.is_win():
            print "won"
            return state.utility(self)

        v = sys.maxint

        if not state.actions():
            state.result(None)
        else:
            for a in state.actions():
                min(self.maxVal(state.result(a)), v)

        return v

    def maxVal(self, state):
        if state.is_win():
            print "won"
            return state.utility(self)

        v = -sys.maxint

        if not state.actions():
            state.result(None)
        else:
            for a in state.actions():
                max(self.minVal(state.result(a)), v)

        return v
