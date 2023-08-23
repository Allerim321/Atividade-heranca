# Classe pai, onde estão contidas as informações que são comuns a todos os tipos de pássaros
class Aves:
# Metodo com uma informação que é comum a todos os pássaros 
    def botarOvo(self):
        print ("É um animal ovíparo")

    def pena(self):
        print ("Possui penas")

    def bico(self):
        print ("Possui um bico, não possui dentes")

# Classe que contem as similaridades apenas dos pássaros que voam, a classe "Aves" entre parenteses significa que ela foi herdada pela classe "Voar", sendo assim a classe "Voar" tem seus metodos proprios mais os metodos da classe "Aves"
class Voar (Aves):
    def voar(self):
        print ("Possui asas e é capaz de voar")

# Classe que contem as similaridades apenas dos pássaros que não voam, a classe "Aves" entre parenteses significa que ela foi herdada pela classe "NãoVoar", sendo assim a classe "NãoVoar" tem seus metodos proprios mais os metodos da classe "Aves"
class NãoVoar (Aves):
    def nãovoar(self):
        print ("Não é capaz de voar")

# Classes para cada passáros que decidimos colocar, essas classes herdam as classes "Voar" ou "NãoVoar" de acordo com qual característica elas possuem e por conseguinte herdam a classe "Aves"
class Aguia(Voar):
# Metodo que contem breves informações sobre o pássaro
   def informações(self):
       print("As águias são aves de rapina, conhecidas por sua grande envergadura, visão aguçada, força e agilidade no voo. As águias têm um significado cultural significativo em muitas sociedades. Por exemplo, a águia careca é um símbolo nacional dos Estados Unidos, e são frequentemente associadas a símbolos de poder, liberdade e nobreza.")

class Falcão(Voar):
   def informações(self):
       print("Os falcões são aves de rapina, admirados por sua incrível habilidade de caça e adaptação a diferentes ambientes. Eles desempenham um papel importante nos ecossistemas como predadores de topo e também têm uma presença significativa na cultura humana ao longo da história.")

class Pato(Voar):
   def informações(self):
       print("Os patos são aves aquáticas. Eles são encontrados em todo o mundo, em uma variedade de ambientes aquáticos, incluindo lagos, rios, lagoas, pântanos e oceanos costeiros. Os patos são conhecidos por sua aparência variada, comportamento social e adaptabilidade.Muitas espécies de patos são migratórias e viajam grandes distâncias entre suas áreas de reprodução e áreas de inverno.")

class Gaivota(Voar):
   def informações(self):
       print("Gaivotas são aves marinhas da família Laridae, que compreende cerca de 50 espécies diferentes. Elas são conhecidas por sua capacidade de voo ágil, adaptabilidade a ambientes costeiros e comportamento social, comunicando-se por meio de vocalizações e posturas corporais.")

class Coruja(Voar):
   def informações(self):
       print("As corujas são aves de rapina noturnas conhecidas por sua aparência distinta, comportamento silencioso de voo e associações culturais com a sabedoria, mistério, conhecimento oculto e, em algumas culturas, até mesmo de morte. ")

class BeijaFlor (Voar):
    def informações(self):
       print("Os beija-flores são aves pequenas, coloridas e incrivelmente ágeis. Eles são conhecidos por sua capacidade de voar em qualquer direção, incluindo para trás, e por sua habilidade de pairar no ar enquanto se alimentam do néctar das flores. Beija-flores são frequentemente associados à beleza, graça e delicadeza, e muitas vezes são considerados símbolos de amor e alegria em várias culturas.")

class PicaPau(Voar):
   def informações(self):
       print("O pica-pau é uma ave caracterizada pelo bico longo e forte, usado para bater em troncos de árvores em busca de insetos. Ele tem uma cabeça distintiva que produz um som de tamborilar. Os pica-paus têm habilidades de escalada excepcionais e são encontrados em várias regiões, desempenhando um papel importante na saúde das florestas ao controlar populações de insetos.")

class Cegonha(Voar):
    def informações(self):
       print("A cegonha é uma ave de pernas longas, conhecida por sua migração anual e por construir grandes ninhos em locais altos. Ela é frequentemente associada à entrega de bebês (embora mito). Cegonhas são encontradas em várias partes do mundo e se alimentam de uma variedade de presas, incluindo insetos, peixes e pequenos animais.")

class Albatroz(Voar):
   def informações(self):
       print("O albatroz é uma ave marinha de grande porte, conhecida por suas asas longas e envergadura impressionante. Ele é um mestre planador, passando a maior parte de sua vida voando sobre os oceanos. Albatrozes têm um papel importante nos ecossistemas marinhos, mas muitas espécies estão ameaçadas devido à pesca incidental e outras ameaças humanas.")

class Gavião(Voar):
   def informações(self):
       print("O gavião é uma ave de rapina encontrada em várias partes do mundo. Ele é conhecido por suas garras afiadas, excelente visão e habilidade em caçar presas. Gaviões desempenham um papel importante no controle de populações de animais, ajudando a manter o equilíbrio nos ecossistemas.")

class Tucano(Voar):
   def informações(self):
       print("O tucano é uma ave tropical conhecida por seu bico colorido e grande, que pode ter várias cores. Ele habita florestas e selvas na América Central e do Sul. Sua aparência vibrante e bico distintivo o tornam uma espécie icônica da região.")

class Pelicano(Voar):
   def informações(self):
       print("O pelicano é uma ave aquática com grande bolsa na mandíbula inferior. Ele é conhecido por mergulhar de grande altura para capturar peixes. Suas asas são largas e suas colônias podem ser encontradas em várias partes do mundo.")

class Pinguim(NãoVoar):
   def informações(self):
       print("Os pinguins são aves marinhas adaptadas para nadar, não voar. Têm penas à prova d'água, nadadeiras e vivem principalmente em regiões frias, como a Antártida. Caçam peixes e krill debaixo d'água, formam colônias sociais e enfrentam ameaças devido às mudanças climáticas e poluição.")

class Casuar(NãoVoar):
   def informações(self):
       print("O casuar é uma grande ave não voadora, nativa da Oceania, conhecida por sua aparência única, plumagem escura e pernas fortes. Vive em florestas tropicais e é considerado uma espécie pré-histórica. Suas garras afiadas e velocidade o tornam um dos pássaros mais perigosos, podendo ser agressivo quando ameaçado.")

class Ema(NãoVoar):
    def informações(self):
       print("A ema é uma ave nativa da América do Sul, conhecida por ser grande, não voadora e ter plumagem marrom. Habita diversas paisagens, desde savanas até florestas. Sua agilidade e velocidade a tornam uma corredora habilidosa.")

class Kiwi(NãoVoar):
    def informações(self):
       print("O kiwi é uma pequena ave nativa da Nova Zelândia, reconhecida por sua aparência única, asas atrofiadas e bico longo. É principalmente noturno, tem hábitos terrestres e é um símbolo nacional da Nova Zelândia.")

class Pavão(NãoVoar):
    def informações(self):
       print("O pavão é uma ave famosa por sua plumagem colorida e cauda em leque, que os machos exibem para atrair fêmeas. Originários da Ásia, os pavões são conhecidos por sua beleza e comportamento de cortejo elaborado.")

class Bico_de_Tamanco(NãoVoar):
    def informações(self):
       print("O bico de tamanco é uma ave encontrada principalmente na América do Sul, notável pelo seu bico largo e chato, semelhante à forma de um tamanco. Vive em ambientes aquáticos e se alimenta filtrando pequenos organismos da água.")

class Avestruz (NãoVoar):
    def informações(self):
       print("O avestruz é a maior ave do mundo, conhecida por sua incapacidade de voar, pernas longas e velocidade terrestre impressionante. Originário da África, possui plumagem macia e é adaptado a ambientes áridos.")

class Galinha(NãoVoar):
    def informações(self):
       print("A galinha é uma ave doméstica comum, conhecida por ser criada para carne e ovos. Originou-se de aves selvagens e é caracterizada por sua plumagem, bico e hábitos de forrageamento.")

class Codorna(NãoVoar):
    def informações(self):
       print("A codorna é uma ave pequena e terrestre, frequentemente criada para carne e ovos. Possui plumagem discreta e é encontrada em várias regiões do mundo. Suas características incluem tamanho compacto e vocalizações distintas.")
