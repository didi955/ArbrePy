
arbres = []

def getArbres():
    return arbres


class Arbre:

    def __init__(self, name, noeuds):
        self.noeuds = noeuds
        self.name = name
        arbres.append(self)

    def getNoeuds(self):
        return self.noeuds

    def addNoeud(self, noeud):
        self.noeuds.append(noeud)

    def getName(self):
        return self.name


class Noeud:

    def __init__(self, pere, value):
        self.list = list
        self.value = value
        self.pere = pere

    def getValue(self):
        return self.value

    def getPere(self):
        return self.pere


def initAbre():
    n = []

    arbre = Arbre("Mon arbre", n)

    for n in range(0, 15):
        if (n < 1):
            noeud = Noeud(None, 1)
            arbre.addNoeud(noeud)
        else:
            noeuds = arbre.getNoeuds()
            noeud = Noeud(noeuds[n - 1], n)
            arbre.addNoeud(noeud)

initAbre()
arbre = arbres[0]
print(arbre.getName())
for n in arbre.getNoeuds():
    print(n.getValue())




