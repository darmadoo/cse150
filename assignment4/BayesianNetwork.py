#!/usr/bin/env python
""" generated source for module BayesianNetwork """
from Assignment4 import *
import random

#
#  * A bayesian network
#  * @author Panqu
#
class BayesianNetwork(object):
    """ generated source for class BayesianNetwork """
    #
    #     * Mapping of random variables to nodes in the network
    #
    varMap = None

    #
    #     * Edges in this network
    #
    edges = None

    #
    #     * Nodes in the network with no parents
    #
    rootNodes = None

    #
    #     * Default constructor initializes empty network
    #
    def __init__(self):
        """ generated source for method __init__ """
        self.varMap = {}
        self.edges = []
        self.rootNodes = []

    #
    #     * Add a random variable to this network
    #     * @param variable Variable to add
    #
    def addVariable(self, variable):
        """ generated source for method addVariable """
        node = Node(variable)
        self.varMap[variable]=node
        self.rootNodes.append(node)

    #
    #     * Add a new edge between two random variables already in this network
    #     * @param cause Parent/source node
    #     * @param effect Child/destination node
    #
    def addEdge(self, cause, effect):
        """ generated source for method addEdge """
        source = self.varMap.get(cause)
        dest = self.varMap.get(effect)
        self.edges.append(Edge(source, dest))
        source.addChild(dest)
        dest.addParent(source)
        if dest in self.rootNodes:
            self.rootNodes.remove(dest)

    #
    #     * Sets the CPT variable in the bayesian network (probability of
    #     * this variable given its parents)
    #     * @param variable Variable whose CPT we are setting
    #     * @param probabilities List of probabilities P(V=true|P1,P2...), that must be ordered as follows.
    #       Write out the cpt by hand, with each column representing one of the parents (in alphabetical order).
    #       Then assign these parent variables true/false based on the following order: ...tt, ...tf, ...ft, ...ff.
    #       The assignments in the right most column, P(V=true|P1,P2,...), will be the values you should pass in as probabilities here.
    #
    def setProbabilities(self, variable, probabilities):
        """ generated source for method setProbabilities """
        probList = []
        for probability in probabilities:
            probList.append(probability)
        self.varMap.get(variable).setProbabilities(probList)

    #
    #     * Returns an estimate of P(queryVal=true|givenVars) using rejection sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of rejection samples to perform
    #
    def performRejectionSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performRejectionSampling """
        #  TODO
        total = 0
        query = [0, 0]

        for i in range(1, numSamples):
            flag = True
            # assignments
            x = self.priorSampling()
            for j in givenVars:
                if not givenVars[j] == x[j.getName()]:
                    flag = False

            # It is consistens
            if flag:
                if x[queryVar.getName()]:
                    query[0] += 1
                else:
                    query[1] += 1

        return self.normalize(query)

    def normalize(self, arr):

        total = 0
        for i in arr:
            total = total + i

        # to avoid division by 0
        if total == 0:
            return 0, 0

        return float(arr[0])/total, float(arr[1])/total

    def priorSampling(self):
        new = sorted(self.varMap)
        assignments = {}

        for i in new:
            # Generated Random numbers
            rand = random.random()

            if rand > self.varMap.get(i).getProbability(assignments, True):
                assignments[i.getName()] = False
            else:
                assignments[i.getName()] = True

        return assignments

    #
    #     * Returns an estimate of P(queryVal=true|givenVars) using weighted sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numSamples Number of weighted samples to perform
    #
    def performWeightedSampling(self, queryVar, givenVars, numSamples):
        """ generated source for method performWeightedSampling """
        #  TODO

        final = [0, 0]

        for i in range(1, numSamples):
            (x, w) = self.getWeightedSample(givenVars)

            if x[queryVar.getName()]:
                final[0] += w
            else:
                final[1] += w

        return self.normalize(final)

    def getWeightedSample(self, e):

        sample = Sample()
        for i in e:
            sample.setAssignment(i.getName(), e[i])
        
#         print sample.assignments
        
#         print "aaaazzzzzzzzzzzzzzzzz"
        for i in sorted(self.varMap.keys()):
#             print i.getName()
            rand = random.random()
            if sample.getValue(i.getName()) is not None:
                currentWeight = sample.getWeight()
#                print self.varMap.get(i).getVariable().getName(),self.varMap.get(i).getProbability(sample.assignments, sample.assignments.get(i.getName()))
                newWeight = currentWeight * self.varMap.get(i).getProbability(sample.assignments, sample.assignments.get(i.getName()))
                sample.setWeight(newWeight)
            else:
                if rand > self.varMap.get(i).getProbability(sample.assignments, True):
                    sample.assignments[i.getName()] = False
                else:
                    sample.assignments[i.getName()] = True

        return sample.assignments, sample.getWeight()
    #
    #     * Returns an estimate of P(queryVal=true|givenVars) using Gibbs sampling
    #     * @param queryVar Query variable in probability query
    #     * @param givenVars A list of assignments to variables that represent our given evidence variables
    #     * @param numTrials Number of Gibbs trials to perform, where a single trial consists of assignments to ALL
    #       non-evidence variables (ie. not a single state change, but a state change of all non-evidence variables)
    #
    def performGibbsSampling(self, queryVar, givenVars, numTrials):
        """ generated source for method performGibbsSampling """
        #  TODO

        query = [0, 0]
        nonEvidenceVar = []
        sortedGiven = sorted(givenVars)

        # get nonEvidence variables
        for var in self.varMap.keys():
            if var not in sortedGiven:
                nonEvidenceVar.append(var)

        # for var in nonEvidenceVar:
        #     print var.getName()

        newEvent = {}

        # get event
        for var in self.varMap.keys():
            if var in sortedGiven:
                newEvent[var] = givenVars[var]

            else:
                rand = random.random()
                value = False
                if rand > 0.5:
                    value = True
                newEvent[var] = value


        for i in range(1, numTrials):
            for var in nonEvidenceVar:
                currentNode = self.varMap[var]
                # print currentNode.getVariable().getName()
                markovNodes = self.markovBlanket(currentNode)

                currentEvent = {} # make list of event for the nodes in mb
                for node in markovNodes:
                    currentEvent[node.getVariable()] = newEvent[node.getVariable()]
                # print var.getName()
                # print "HEI"
                # for weird in currentEvent:
                #     print weird.getName()
                #     print currentEvent[weird]

                value = self.getNewProbs(var, currentEvent, True)
                rand = random.random()

                newBool = False
                if value < rand:
                    newBool = True

                # update value
                newEvent[currentNode.getVariable()] = newBool

                queryValue = newEvent[queryVar]

                if queryValue:
                    query[0] += 1
                else:
                    query[1] += 1

        result = float(query[0]) / (float(numTrials * len(nonEvidenceVar)))

        return result

    def getNewProbs(self, var, surroundingMap, boolean):
        probabilityTrue = self.getNewOne(var, surroundingMap, True)
        probabilityFalse = self.getNewOne(var, surroundingMap, False)
        alpha = 1.0 / (probabilityFalse + probabilityTrue)

        if boolean:
            alpha = probabilityTrue * alpha
        else:
            alpha = probabilityFalse * alpha

        return alpha


    def getNewOne(self, var, map, boolean):
        node = self.varMap[var]
        #print var.getName()

        queryParents = {}
        for parent in node.getParents():
            queryParents[parent.getVariable()] = map[parent.getVariable()]

        # print var.getName()
        # print "Hei"
        probGivenParents = node.getProbability(queryParents, boolean)
        # print probGivenParents

        probChildren = 1.0

        for child in node.getChildren():
            childrenParents = {}

            for childParent in child.getParents():

                if childParent.getVariable().equals(node.getVariable()):
                    childrenParents[node.getVariable()] = boolean
                else:
                    childrenParents[childParent.getVariable()] = map[childParent.getVariable()]

            probChildren *= child.getProbability(childrenParents, map[child.getVariable()])

        result = probGivenParents * probChildren

        return result


    def markovBlanket(self, node):
        everything = []

        # add parents
        for parent in node.getParents():
            everything.append(parent)

        for child in node.getChildren():
            if child not in everything:
                everything.append(child)

                for childParent in child.getParents():
                    if (childParent not in everything) and not (childParent == node):
                        everything.append(childParent)

        # print "HEI"
        # for node in everything:
        #
        #     print node.getVariable().getName()

        return everything


