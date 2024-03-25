from random import randint
from Config.Funções import JogarDado
class Personagem:
   def __init__(self,raca, cor, tamanho, arma, armadura): 
      self.tamanho = tamanho
      self.cor = cor
      self.ListaCor = ["AMARELO", "VERMELHO", "AZUL", "VERDE", "ROSA", "MORENO"]
      self.raca = raca
      self.ListaRaca = ["HUMANO", "ORC", "GIGANTE", "DRAGONETE", "FADA"]
      self.arma = arma
      self.ListaArma = ["MÃO", "ESPADA CURTA", "ESPADA LONGA", "ADAGA"]
      self.armadura = armadura
      self.ListaArmadura = ["ARMADURA LEVE", "ARMADURA PESADA", "SEM ARMADURA"]
      
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
      
   def TrocarArma(self, nova_arma):
      if nova_arma in self.ListaArma:
         self.arma = nova_arma
   
   def MostrarInfo(self):
        print(self.cor)
        print(self.tamanho,"cm")
        print(self.raca)
        print(self.arma)
        print(self.armadura)
       

cliente = Personagem("HUMANO","MORENO", 145, "MÃO", "SEM ARMADURA")
