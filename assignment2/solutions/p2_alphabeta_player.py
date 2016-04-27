# -*- coding: utf-8 -*-
__author__ = 'mdarmadi@ucsd.edu, A11410141, hdharmaw@ucsd.edu, A91413023, vcchandr@ucsd.edu, A12496582'


from assignment2 import Player, State, Action
import sys

class AlphaBetaPlayer(Player):

    nextState = None

    def move(self, state):
        """Calculates the best move from the given board using the minimax
        algorithm with alpha-beta pruning and transposition table.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        return self.abSearch(state)
        raise NotImplementedError("Need to implement this method")

    def abSearch(self, state):
        global nextState

        self.maxVal(state, -sys.maxint, sys.maxint)

        best_act = nextState

        return best_act


    def maxVal(self, state, alpha, beta):
        global nextState

        if state.is_terminal():
            return state.utility(self)

        v = -sys.maxint

        if not state.actions():
            v = max(v, self.minVal(state.result(None), alpha, beta))
        else:
            for a in state.actions():
                v = max(v, self.minVal(state.result(a), alpha, beta))
                if v >= beta:
                    return v
                if (v > alpha):
                    nextState = a
                alpha = max(v, alpha)


        return v

    def minVal(self, state, alpha, beta):
        global nextState

        if state.is_terminal():
            return state.utility(self)

        v = sys.maxint

        if not state.actions():
            v = min(v, self.maxVal(state.result(None), alpha, beta))
        else:
            for a in state.actions():
                v = min(v, self.maxVal(state.result(a), alpha, beta))
                if v <= alpha:
                    return v
                beta = min(v, beta)

        return v
