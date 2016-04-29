# -*- coding: utf-8 -*-

__author__ = 'hdharmaw@ucsd.edu, A91413023, mdarmadi@ucsd.edu, A11410141, vcchandr@ucsd.edu, A12496582'


from assignment2 import Player, State, Action
import sys
import time 

DEPTH = 10  # customizable depth

class CustomAgentPlayer10(Player):
    """The custom player implementation.
    """

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """

        # VARIABLES
        self.tTable = {} # transposition table
        self.aTable = {} # action transposition table

        pass

    def move(self, state):
        global DEPTH
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        t0 = time.time()
        (self.tTable).clear()
        (self.aTable).clear()

        best_act = None
        best_v = -sys.maxint

        for d in range(1, DEPTH):
            actions = state.actions()

            for action in actions:
                util = self.minVal(state.result(action), d + 1, -sys.maxint, sys.maxint)
                self.aTable[action] = util

        # go through the action table to find the best move
        for action in self.aTable:
            if (self.aTable.get(action) > best_v):
                best_v = self.aTable.get(action)
                best_act = action
        t1 = time.time()
        print "Time: " + str(t1 - t0)
        return best_act

        # raise NotImplementedError("Need to implement this method")


    def maxVal(self, state, depth, alpha, beta):
        global nextAction, DEPTH

        # if time's up
        if self.is_time_up() or depth >= DEPTH:
            return self.evaluate(state, state.player_row)

        if state.is_terminal():
            self.tTable[state] = state.utility(self) # add to transposition table
            return state.utility(self)

        v = -sys.maxint

        if not state.actions():
            v = max(v, self.minVal(state.result(None), depth + 1, alpha, beta))
        else:
            for a in state.actions():
                # if value can be found in transposition table
                if not self.tTable.get(state.result(a)) is None:
                    v = max(v, self.tTable[state.result(a)])

                else:
                    v = max(v, self.minVal(state.result(a), depth + 1, alpha, beta))

                if v >= beta:
                    return v

                if (v > alpha):
                 nextAction = a
                alpha = max(v, alpha)

        return v

    def minVal(self, state, depth, alpha, beta):
        global nextAction, DEPTH

        # if time's up
        if self.is_time_up() or depth >= DEPTH:
            return - self.evaluate(state, state.player_row)

        if state.is_terminal():
            self.tTable[state] = state.utility(self)  # add to transposition table
            return state.utility(self)

        v = sys.maxint

        if not state.actions():
            v = min(v, self.maxVal(state.result(None),depth + 1, alpha, beta))
        else:
            for a in state.actions():
                if not self.tTable.get(state.result(a)) is None:
                    v = min(v, self.tTable[state.result(a)])

                else:
                    v = min(v, self.maxVal(state.result(a), depth + 1,  alpha, beta))

                if v <= alpha:
                    return v

                beta = min(v, beta)

        return v

    def evaluate(self, state, my_row):
        """
        Evaluates the state for the player with the given row
        """

        goalStone = state.board[state.opponent_goal_idx]
        oppStones = state.board[state.player_goal_idx]
        stonesYourSide = 0
        stonesOppSide = 0
        m = float(state.M)
        n = float(state.N)

        oppRange = state.possible_action_range()
        for a in range(oppRange[0], oppRange[1]):
            stonesOppSide += state.board[a]

        if my_row == 0:
            for i in range(0, state.player_goal_idx):
                stonesYourSide += state.board[i]
        else:
            for i in range((state.player_goal_idx + 1), (state.opponent_goal_idx)):
                stonesYourSide += state.board[i]

        result = (1 / (2 * m * n)) * (goalStone - oppStones + stonesYourSide - stonesOppSide)

        return result
        # raise NotImplementedError("Need to implement this method")
