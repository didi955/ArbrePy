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
        # Create the graph
        vertices = ["one", "two", "three"]
        edges = [(0, 2), (2, 1), (0, 1)]

        g = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=True)

        visual_style = {}

        # Scale vertices based on degree
        outdegree = g.outdegree()
        visual_style["vertex_size"] = [x / max(outdegree) * 50 + 110 for x in outdegree]

        # Set bbox and margin
        visual_style["bbox"] = (800, 800)
        visual_style["margin"] = 100

        # Define colors used for outdegree visualization
        colours = ['#fecc5c', '#a31a1c']

        # Order vertices in bins based on outdegree
        bins = np.linspace(0, max(outdegree), len(colours))
        digitized_degrees = np.digitize(outdegree, bins)

        # Set colors according to bins
        g.vs["color"] = [colours[x - 1] for x in digitized_degrees]

        # Also color the edges
        for ind, color in enumerate(g.vs["color"]):
            edges = g.es.select(_source=ind)
            edges["color"] = [color]

        # Don't curve the edges
        visual_style["edge_curved"] = False

        # Plot the graph
        plot(g, **visual_style)


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


list = [0, 1, 2, 3, 4, 5]
arbre = Arbre("Salut", list)
arbre.draw()
