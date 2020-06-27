class Node(object):
    x = 0
    y = 0
    frequentadores = list()

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # self.listaAdj.add(Adj)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def add_frequentadores(self, id):
        if (id not in self.frequentadores):
            self.frequentadores.append(id)
            

    def getFrequentadores(self):
        return self.frequentadores

    # def getAdj(self):
    #     return self.listaAdj