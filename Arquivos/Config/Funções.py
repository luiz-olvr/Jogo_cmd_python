from random import randint
def PerguntaNome():
   str(input("Digite seu nome: "))
   
   
def ImparPar():
   num = int(input("Digite um valor: "))
   if num%2 == 0:
      print("Par")
   else:
      print("Impar")


def ParImpar():
   num = int(input("Digite um valor: "))
   if num%2 == 0:
      return 1
   else:
      return 0

def JogarDado():
   return randint(1, 20)