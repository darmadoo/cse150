#!/usr/bin/env python

from BayesianNetwork import *
#
#   * Creates and tests the guilty network as given in the book.
#

class GuiltyNetwork(object):
    """ generated source for class Guilty Network """

    @classmethod
    def main(cls, args):
        guiltynet = BayesianNetwork()

        # Add variables
        breaklaw = RandomVariable("Break")
        prosecutor = RandomVariable("Prosecutor")
        indicted = RandomVariable("Indicted")
        guilty = RandomVariable("Guilty")
        jail = RandomVariable("Jail")

        guiltynet.addVariable(breaklaw)
        guiltynet.addVariable(indicted)
        guiltynet.addVariable(prosecutor)
        guiltynet.addVariable(guilty)
        guiltynet.addVariable(jail)

        # Add edges
        guiltynet.addEdge(breaklaw, indicted)
        guiltynet.addEdge(prosecutor, indicted)
        guiltynet.addEdge(breaklaw, guilty)
        guiltynet.addEdge(indicted, guilty)
        guiltynet.addEdge(prosecutor, guilty)
        guiltynet.addEdge(guilty, jail)

        # initialize probability tables
        breaklawProbs = [0.9]
        prosecutorProbs = [0.1]
        indictedProbs = [0.9, 0.5, 0.5, 0.1]
        guiltyProbs = [0.9, 0.8, 0.0, 0.0, 0.2, 0.1, 0.0, 0.0]
        jailProbs = [0.9, 0.0]

        guiltynet.setProbabilities(breaklaw, breaklawProbs)
        guiltynet.setProbabilities(prosecutor, prosecutorProbs)
        guiltynet.setProbabilities(indicted, indictedProbs)
        guiltynet.setProbabilities(guilty, guiltyProbs)
        guiltynet.setProbabilities(jail, jailProbs)

        #  Perform sampling tests
        #  ----------------------
        #  P(J=1|B=1,M=1)
        print("Test 1")
        given1 = {}
        given1[breaklaw]=True
        given1[prosecutor]=False
        print("rejection sampling: " + str(guiltynet.performRejectionSampling(jail, given1, 99999)))
        print("weighted sampling: " + str(guiltynet.performWeightedSampling(jail, given1, 99999)))
        print("gibbs sampling: " + str(guiltynet.performGibbsSampling(jail, given1, 99999)))

        #  P(M=1|J=1)
        print("Test 2")
        given2 = {}
        given2[jail] = True
        print("rejection sampling: " + str(guiltynet.performRejectionSampling(prosecutor, given2, 99999)))
        print("weighted sampling: " + str(guiltynet.performWeightedSampling(prosecutor, given2, 99999)))
        print("gibbs sampling: " + str(guiltynet.performGibbsSampling(prosecutor, given2, 99999)))


if __name__ == '__main__':
    import sys
    GuiltyNetwork.main(sys.argv)
import sys
GuiltyNetwork.main(sys.argv)
