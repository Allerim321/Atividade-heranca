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

class Aguia(Voar):
   def informações(self):
       print("")

class Falcão(Voar):
   def informações(self):
       print("")

class Pato(Voar):
   def informações(self):
       print("")

class Gaivota(Voar):
   def informações(self):
       print("")

class PicaPau(Voar):
   def informações(self):
       print("")

class Gavião(Voar):
   def informações(self):
       print("")

class Tucano(Voar):
   def informações(self):
       print("")

class Pelicano(Voar):
   def informações(self):
       print("")

class Albatroz(Voar):
   def informações(self):
       print("")

class Avestruz (Voar):
    def informações(self):
       print("")

class Beija_flor (Voar):
    def informações(self):
       print("")

class Cegonha(Voar):
    def informações(self):
       print("")

class Coruja(Voar):
   def informações(self):
       print("")

class Codorna(NãoVoar):
    def informações(self):
       print("")


class Ema (NãoVoar):
    def informações(self):
       print("")

class Bico_de_Tamanco(NãoVoar):
    def informações(self):
       print("")

class Casuar(NãoVoar):
   def informações(self):
       print("")
