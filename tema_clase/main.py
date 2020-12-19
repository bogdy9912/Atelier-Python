class Fractie:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return str(self.numarator) + '/' + str(self.numitor)

    def __add__(self, other):
        numarator = self.numarator * other.numitor + other.numarator * self.numitor
        numitor = self.numitor * other.numitor
        fractie = Fractie(numitor, numarator)
        return fractie

    def __sub__(self, other):
        numarator = self.numarator * other.numitor - other.numarator * self.numitor
        numitor = self.numitor * other.numitor
        return numarator, numitor

    def inverse(self):
        fractie = Fractie(self.numitor, self.numarator)
        return fractie
