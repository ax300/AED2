class Node(object):

    def __init__(self, x, y, id):
        # Id composto pelas coordenadas concatenadas
        self.id = id
        # coordenadas
        self.x = x
        self.y = y
        self.frequentadores = []

    def add_frequentadores(self, id):
        if (id not in self.frequentadores): #adiciona id dos frequentadores sem repetir
            self.frequentadores.append(id)