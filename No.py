class No:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frequentadores = list()
        # self.listaAdj.add(Adj)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def ADD(self, Id):
        if (Id not in self.frequentadores):
            self.frequentadores.append(Id)

    def getFrequentadores(self):
        return self.frequentadores

    # def getAdj(self):
    #     return self.listaAdj