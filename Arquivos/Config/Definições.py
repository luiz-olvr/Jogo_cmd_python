from Config.Funções import JogarDado, AcaoInimigo, sleep, PontoInimigo, ArmaduraIN, ArmasIN
class Personagem:
   def __init__(self,raca, cor, tamanho, vida, força, agilidade, sentimentos): 
      self.tamanho = tamanho
      self.cor = cor
      self.ListaCor = ["AMARELO", "VERMELHO", "AZUL", "VERDE", "ROSA", "MORENO"]
      self.raca = raca
      self.ListaRaca = ["HUMANO", "ORC", "GIGANTE", "DRAGONETE", "FADA"]
      self.força = força
      self.agilidade = agilidade
      self.vida = vida
      self.sentimentos = sentimentos
      self.ListaSentimentos = ["RAIVA", "TRISTEZA", "ALEGRIA", "CONFUSO", "MEDO"]
      
   def Mudarcor(self, nova_cor):
      if nova_cor in self.ListaCor:
         self.cor = nova_cor
      else:
         print("Cor invalida!!")
      
   def MudarTamanho(self, novo_tamanho):
      if novo_tamanho >30 and novo_tamanho <200:
         self.tamanho = novo_tamanho
      else:
         print("Tamanho invalido! ")
      
   def MudarRaca(self, nova_raca):
      if nova_raca in self.ListaRaca:
         self.raca = nova_raca
      else:
         print("Raça invalida!")
   
   def MostrarInfo(self):
        print(f"\n\nCor: {self.cor}")
        print(f"Altura: \033[36m{self.tamanho}\033[mcm")
        print(f"Raça: \033[1;37m{self.raca}\033[m")
        print(f"Vida: \033[35m{self.vida}\033[m")
        print(f"Agilidade: \033[33m{self.agilidade}\033[m")
        print(f"Força: \033[33m{self.força}\033[m")
        print(f"Arma: \033[0;31m{itens.arma}\033[m")
        print(f"Armadura: \033[32m{itens.armadura}\033[m \n\n")
        
class armas_armaduras:
   def __init__(self, arma, armadura, arremessaveis, poções):
      self.arma = arma
      self.ListaArma = ["MÃO", "ESPADA CURTA", "ESPADA LONGA", "ADAGA"]
      self.armadura = armadura
      self.ListaArmadura = ["ARMADURA LEVE", "ARMADURA PESADA", "SEM ARMADURA"]
      self.arremessaveis = arremessaveis
      self.ListaArre = ["ESPINHOS"]
      self.pocoes = poções
      self.ListaPocoes = ["VIDA", "FORÇA"]
      
   def MudarArma(self, nova_arma):
      if nova_arma in self.ListaArma:
         self.arma = nova_arma
         
   def MudarArmadura(self, nova_armadura):
      if nova_armadura in self.ListaArmadura:
         self.armadura = nova_armadura
      
   def MostrarArmas(self):
      for i in self.ListaArma:
         print(f"\n \033[0;32m{i}\033[m")
   
   def MostrarArmaduras(self):
      for i in self.ListaArmadura:
         print(f"\n \033[0;32m{i}\033[m")

itens = armas_armaduras("MÃO", "SEM ARMADURA", "ESPINHOS", "VIDA")
jogador = Personagem("HUMANO","MORENO", 145, 100, 20, 0, "SIGMA")
ItesnInimigo = armas_armaduras("MÃO", "SEM ARMADURA", "ESPINHOS", "VIDA")
Inimigo = Personagem("HUMANO","MORENO", 145, 100, PontoInimigo(), PontoInimigo(), "SIGMA")

def MenuPersonalizacao():
   while True:
    print("\nPersonalização!!\n\n[ 0 ] Mudar sua cor \n[ 1 ] Mudar tamanho\n[ 2 ] Mudar raça\n[ 3 ] Mostrar Info\n[ 4 ] Trocar de arma\n[ 5 ] Trocar armadura\n[ 6 ] Terminar edição\n")  
    escolhaComb = int(input("O que deseja fazer? "))
    if escolhaComb == 0:
        jogador.Mudarcor(str(input("\nDigite sua cor: ")).upper().strip())
    elif escolhaComb == 1:
        jogador.MudarTamanho(int(input("\nDigite seu tamanho: ")))
    elif escolhaComb == 2:
        jogador.MudarRaca(str(input("\nDigite sua raça: ")).upper().strip())
    elif escolhaComb == 3:
        jogador.MostrarInfo()
    elif escolhaComb == 4:
         itens.MostrarArmas()
         itens.MudarArma(str(input("\nDigite sua arma: ")).upper().strip())
    elif escolhaComb == 5:
        itens.MostrarArmaduras()
        itens.MudarArmadura(str(input("\nDigite sua armadura: ")).upper().strip())
    elif escolhaComb == 6:
        escolhaComb = str(input("\nTerminar edição de personagem? S/N  ")).upper().strip()[0]
        if escolhaComb == "S":
            break
        elif escolhaComb == "N":
            pass
        else:
            print("Opção invalida!!")
