from Classes import *
import os

def main():
    a = 1
    while a == 1:
        try:            
            print("Bem vindo ao Birdspédia.")
            print("[01] - Águia")
            print("[02] - Albatroz")
            print("[03] - Avestruz")
            print("[04] - Beija-flor")
            print("[05] - Bico-de-Tamanco")
            print("[06] - Casuar")
            print("[07] - Cegonha")
            print("[08] - Codorna")
            print("[09] - Coruja")
            print("[10] - Ema")
            print("[11] - Falcão")
            print("[12] - Gaivota")
            print("[13] - Galinha")
            print("[14] - Gavião")
            print("[15] - Kiwi")
            print("[16] - Pato")
            print("[17] - Pavão")
            print("[18] - Pelicano")
            print("[19] - Pica-Pau")
            print("[20] - Pinguim")
            print("[21] - Tucano")
            print("[22] - Sair")
            menu=input("Digite o número correspondente à ave que gostaria de visitar. \n -")
            
            match menu:
                case "1":
                    ("Aqui estão algumas informações sobre águias para você! \n")
                    aguia = Aguia()
                    aguia.botarOvo()
                    aguia.pena()
                    aguia.bico()
                    aguia.voar()
                    aguia.informações()
                    os.system("pause")
                    os.system("cls")
                case "2":
                    ("Aqui estão algumas informações sobre albatroz para você! \n")
                    albatroz = Albatroz()
                    albatroz.botarOvo()
                    albatroz.pena()
                    albatroz.bico()
                    albatroz.voar()
                    albatroz.informações()
                    os.system("pause")
                    os.system("cls")

                case "3":
                    ("Aqui estão algumas informações sobre avestruz para você! \n")
                    avestruz = Avestruz()
                    avestruz.botarOvo()
                    avestruz.pena()
                    avestruz.bico()
                    avestruz.nãovoar()
                    avestruz.informações()
                    os.system("pause")
                    os.system("cls")

                case "4":
                    ("Aqui estão algumas informações sobre beija-flores para você! \n")
                    beijaflor = BeijaFlor()
                    beijaflor.botarOvo()
                    beijaflor.pena()
                    beijaflor.bico()
                    beijaflor.voar()
                    beijaflor.informações()
                    os.system("pause")
                    os.system("cls")

                case "5":
                    ("Aqui estão algumas informações sobre bicos de tamanco para você! \n")
                    bicotamanco = Bico_de_Tamanco()
                    bicotamanco.botarOvo()
                    bicotamanco.pena()
                    bicotamanco.bico()
                    bicotamanco.nãovoar()
                    bicotamanco.informações()
                    os.system("pause")
                    os.system("cls")
                    
                case "6":
                    ("Aqui estão algumas informações sobre causares para você! \n")
                    causar = Casuar()
                    causar.botarOvo()
                    causar.pena()
                    causar.bico()
                    causar.nãovoar()
                    causar.informações()
                    os.system("pause")
                    os.system("cls")

                case "7":
                    ("Aqui estão algumas informações sobre cegonhas para você! \n")
                    cegonha = Cegonha()
                    cegonha.botarOvo()
                    cegonha.pena()
                    cegonha.bico()
                    cegonha.voar()
                    cegonha.informações()
                    os.system("pause")
                    os.system("cls")

                case "8":
                    ("Aqui estão algumas informações sobre codornas para você! \n")
                    codorna = Codorna()
                    codorna.botarOvo()
                    codorna.pena()
                    codorna.bico()
                    codorna.nãovoar()
                    codorna.informações()
                    os.system("pause")
                    os.system("cls")

                case "9":
                    ("Aqui estão algumas informações sobre corujas para você! \n")
                    coruja = Coruja()
                    coruja.botarOvo()
                    coruja.pena()
                    coruja.bico()
                    coruja.voar()
                    coruja.informações()
                    os.system("pause")
                    os.system("cls")

                case "10":
                    ("Aqui estão algumas informações sobre emas para você! \n")
                    ema = Ema()
                    ema.botarOvo()
                    ema.pena()
                    ema.bico()
                    ema.nãovoar()
                    ema.informações()
                    os.system("pause")
                    os.system("cls")

                case "11":
                    ("Aqui estão algumas informações sobre falcões para você! \n")
                    falcão = Falcão()
                    falcão.botarOvo()
                    falcão.pena()
                    falcão.bico()
                    falcão.voar()
                    falcão.informações()
                    os.system("pause")
                    os.system("cls")

                case "12":
                    ("Aqui estão algumas informações sobre gaivotas para você! \n")
                    gaivota = Gaivota()
                    gaivota.botarOvo()
                    gaivota.pena()
                    gaivota.bico()
                    gaivota.voar()
                    gaivota.informações()
                    os.system("pause")
                    os.system("cls")

                case "13":
                    ("Aqui estão algumas informações sobre galinhas para você! \n")
                    galina = Galinha()
                    galina.botarOvo()
                    galina.pena()
                    galina.bico()
                    galina.nãovoar()
                    galina.informações()
                    os.system("pause")
                    os.system("cls")

                case "14":
                    ("Aqui estão algumas informações sobre gaviões para você! \n")
                    gavião = Gavião()
                    gavião.botarOvo()
                    gavião.pena()
                    gavião.bico()
                    gavião.voar()
                    gavião.informações()
                    os.system("pause")
                    os.system("cls")

                case "15":
                    ("Aqui estão algumas informações sobre kiwis para você! \n")
                    kiwi = Kiwi()
                    kiwi.botarOvo()
                    kiwi.pena()
                    kiwi.bico()
                    kiwi.nãovoar()
                    kiwi.informações() 
                    os.system("pause")
                    os.system("cls")

                case "16":
                    ("Aqui estão algumas informações sobre patos para você! \n")
                    pato = Pato()
                    pato.botarOvo()
                    pato.pena()
                    pato.bico()
                    pato.voar()
                    pato.informações()
                    os.system("pause")
                    os.system("cls")

                case "17":
                    ("Aqui estão algumas informações sobre pavões para você! \n")
                    pavão = Pavão()
                    pavão.botarOvo()
                    pavão.pena()
                    pavão.bico()
                    pavão.nãovoar()
                    pavão.informações()
                    os.system("pause")
                    os.system("cls")

                case "18":
                    ("Aqui estão algumas informações sobre pelicanos para você! \n")
                    pelicano = Pelicano()
                    pelicano.botarOvo()
                    pelicano.pena()
                    pelicano.bico()
                    pelicano.voar()
                    pelicano.informações()
                    os.system("pause")
                    os.system("cls")

                case "19":
                    ("Aqui estão algumas informações sobre pica-paus para você! \n")
                    picapau = PicaPau()
                    picapau.botarOvo()
                    picapau.pena()
                    picapau.bico()
                    picapau.voar()
                    picapau.informações()
                    os.system("pause")
                    os.system("cls")

                case "20":
                    ("Aqui estão algumas informações sobre pinguins para você! \n")
                    pinguim = Pinguim()
                    pinguim.botarOvo()
                    pinguim.pena()
                    pinguim.bico()
                    pinguim.nãovoar()
                    pinguim.informações()
                    os.system("pause")
                    os.system("cls")

                case "21":
                    ("Aqui estão algumas informações sobre tucanos para você! \n")
                    tucano = Tucano()
                    tucano.botarOvo()
                    tucano.pena()
                    tucano.bico()
                    tucano.voar()
                    tucano.informações()
                    os.system("pause")
                    os.system("cls")

                case "22":
                    exit()
                case _:
                    print ("Opção inválida.")        
        
        except:
            print("Erro, opção inválida. Tente novamente.")
            os.system("pause")
            os.system("cls")