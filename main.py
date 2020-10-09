from igraph import *
import numpy as np

arbres = []


def getArbres():
    return arbres


class Arbre:

    def __init__(self, name, noeuds):
        self.noeuds = noeuds
        self.name = name
        getArbres().append(self)

    def getNoeuds(self):
        return self.noeuds

    def addNoeud(self, noeud):
        self.noeuds.append(noeud)

    def getName(self):
        return self.name

    def draw(self):
        print("Work in progress")
        


class Noeud:

    def __init__(self, arbre, name, pere, value):
        self.list = list
        self.value = value
        self.pere = pere
        self.name = name
        self.arbre = arbre

    def getValue(self):
        return self.value

    def getPere(self):
        return self.pere

    def hasPere(self):
        if self.pere is None:
            return False
        else:
            return True

    def hasFils(self):
        for f in self.getArbre().getNoeuds():
            if f.getPere == self:
                return True
            else:
                return False

    def getFils(self):
        fils = []
        for n in self.getArbre().getNoeuds():
            if n.getPere == self:
                fils.append(n)

        return fils

    def getName(self):
        return self.name

    def getArbre(self):
        return self.arbre

