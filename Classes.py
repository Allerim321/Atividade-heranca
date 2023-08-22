class Aves:
    def botarOvo(self):
        print ("É um animal ovíparo.")

    def pena(self):
        print ("Essa ave possui penas")

    def bico(self):
        print ("Essa ave possui um bico, não possui dentes")

class Voar (Aves):
    def voar(self):
        print ("Essa ave possui asas e é capaz de voar")

class NãoVoar (Aves):
    def nãovoar(self):
        print ("Essa ave ão é capaz de voar")

