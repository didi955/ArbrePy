
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

    def __init__(self, abre, name, pere, value):
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
        if(self.pere == None):
            return False
        else:
            return True

    def hasFils(self):
        for f in self.getArbre().getNoeuds():
            if(f.getPere == self):
                return True
            else:
                return False;

    def getName(self):
        return self.name

    def getArbre(self):
        return self.arbre


def initAbre():
    n = []

    arbre = Arbre("Mon arbre", n)

    for n in range(0, 15):
        if (n < 1):
            noeud = Noeud(arbre, "Noeud 1", None, 1)
            arbre.addNoeud(noeud)
        else:
            noeuds = arbre.getNoeuds()
            name = "Noeud {}".format(n)
            noeud = Noeud(arbre, name, noeuds[n - 1], False)
            arbre.addNoeud(noeud)

initAbre()
arbre = arbres[0]
print(arbre.getName())
for n in arbre.getNoeuds():
    name = n.getName()
    value = n.getValue()
    print("Liste des noueuds dans {}: {} -> {}".format(arbre.getName(), name, value))

