from Config.Definições import *

while True:
    print("[ 0 ] Mudar sua cor \n[ 1 ] Mudar tamanho\n[ 2 ] Mudar raça\n[ 3 ] Mostrar Info\n[ 4 ] Jogar dado")  
    escolha = int(input("O que deseja fazer? "))
    if escolha == 0:
        cliente.Mudarcor(str(input("Digite sua cor: ")).upper().strip())
    elif escolha == 1:
        cliente.MudarTamanho(int(input("Digite seu tamanho: ")))
    elif escolha == 2:
        cliente.MudarRaca(str(input("Digite sua raça: ")).upper().strip())
    elif escolha == 3:
        cliente.MostrarInfo()
    elif escolha == 4:
        escolha = str(input("Quer jogar um dado?")).upper()[0]
        if escolha == "S":
            JogarDado()
        else:
            print("Tudo bem! ")