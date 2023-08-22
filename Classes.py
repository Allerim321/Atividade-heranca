class Aves:
    def botarOvo(self):
        print ("É um animal ovíparo")

    def pena(self):
        print ("Possui penas")

    def bico(self):
        print ("Possui um bico, não possui dentes")

class Voar (Aves):
    def voar(self):
        print ("Possui asas e é capaz de voar")

class NãoVoar (Aves):
    def nãovoar(self):
        print ("Não é capaz de voar")

