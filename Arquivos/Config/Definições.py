from random import randint
from Config.Funções import JogarDado
class Personagem:
   def __init__(self,raca, cor, tamanho): 
      self.cor = cor
      self.ListaCor = ["AMARELO", "VERMELHO", "AZUL", "VERDE", "ROSA", "MARROM"]
      self.tamanho = tamanho
      self.raca = raca
      self.ListaRaca = ["HUMANO", "ORC", "GIGANTE", "DRAGONETE", "FADA"]
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
        print(self.cor)
        print(self.tamanho,"cm")
        print(self.raca)
       

cliente = Personagem("HUMANO","AMARELO", 130)
