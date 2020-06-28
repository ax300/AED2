class Node(object):

    def __init__(self, x, y, id):
        # Id composto pelas coordenadas concatenadas
        self.id = id
        # coordenadas
        self.x = x
        self.y = y
        self.frequentadores = []
        # self.listaAdj.add(Adj)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def add_frequentadores(self, id):
        if (id not in self.frequentadores):
            self.frequentadores.append(id)

    def get_frequentadores(self):
        return self.frequentadores

    # def getAdj(self):
    #     return self.listaAdj.