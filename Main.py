import csv
import sys
import numpy
from No import No


def printNos(Nos):
    for No in Nos:
        print(" Coord x:" + No.getX() + " Coord y:" + No.getY() + "\n")

if __name__ == '__main__':

    with open(r"OD_2017.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        Nos = list()
        for row in csv_reader:
            # print(row)
            if (line_count != 0):
                if (No not in Nos):
                    No = No(row[84], row[85])  # coordenadas
                    No.ADD(row[43])  # Id do freq
                    Nos.append(No)
printNos(Nos)

