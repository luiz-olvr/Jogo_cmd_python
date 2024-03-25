from Arquivos.Config.Definições import *
from Arquivos.Config.Funções import JogarDado
while True:  
    dado = randint(1, 20)
    cliente.Mudarcor(str(input("Digite sua cor: ")).upper().strip())
    cliente.MudarTamanho(int(input("Digite seu tamanho: ")))
    cliente.MudarRaca(str(input("Digite sua raça: ")).upper().strip())
    cliente.MostrarInfo()
    escolha = str(input("Quer jogar um dado?")).upper()[0]
    if escolha == "S":
        JogarDado()
    else:
        print("Tudo bem! ")
   