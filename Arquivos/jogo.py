from Config.Definições import *

while True:
    print("\n[ 0 ] Mudar sua cor \n[ 1 ] Mudar tamanho\n[ 2 ] Mudar raça\n[ 3 ] Mostrar Info\n[ 4 ] Terminar edição\n")  
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
        escolha = str(input("Terminar edição de personagem? S/N  ")).upper().strip()[0]
        if escolha == "S":
            break
        elif escolha == "N":
            pass
        else:
            print("Opção invalida!!")

while True:
     #elif escolha == 4:
        escolha = str(input("Quer jogar um dado? S/N " )).upper()[0]
        if escolha == "S":
            print(f"Seu dado foi {JogarDado()}\n")
        elif escolha == "N":
            print("Fim do dado")
            break
        else:
            print("Opção invalida!! ")