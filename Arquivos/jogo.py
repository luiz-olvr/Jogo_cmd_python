from Config.Definições import *
esp =0

    #Edição de personagem 
while True:
    print("\nPersonalização!!\n\n[ 0 ] Mudar sua cor \n[ 1 ] Mudar tamanho\n[ 2 ] Mudar raça\n[ 3 ] Mostrar Info\n[ 4 ] Trocar de arma\n[ 5 ] Trocar armadura\n[ 6 ] Terminar edição\n")  
    escolha = int(input("O que deseja fazer? "))
    if escolha == 0:
        jogador.Mudarcor(str(input("\nDigite sua cor: ")).upper().strip())
    elif escolha == 1:
        jogador.MudarTamanho(int(input("\nDigite seu tamanho: ")))
    elif escolha == 2:
        jogador.MudarRaca(str(input("\nDigite sua raça: ")).upper().strip())
    elif escolha == 3:
        jogador.MostrarInfo()
    elif escolha == 4:
         itens.MostrarArmas()
         itens.MudarArma(str(input("\nDigite sua arma: ")).upper().strip())
    elif escolha == 5:
        itens.MostrarArmaduras()
        itens.MudarArmadura(str(input("\nDigite sua armadura: ")).upper().strip())
    elif escolha == 6:
        escolha = str(input("\nTerminar edição de personagem? S/N  ")).upper().strip()[0]
        if escolha == "S":
            break
        elif escolha == "N":
            pass
        else:
            print("Opção invalida!!")

            
    #começo do jogo
while True:
    if jogador.vida <=0:
        print("\nVOCÊ MORREU!!!\n")
        break
    action = AcaoInimigo()
    if esp != 0 and esp <= 4 and action != 5:
        inimigo -= 3
        esp += 1
        print("Seus espinhos causam dano")
        print(f"\nVida atual do inimigo: \033[31m{inimigo}\033[m\n")
    if esp == 4:
        esp = 0
    if action == 5:
        esp =0
        print("\nSeu inimigo tirou os espinhos da arena!\n")
    if action == 7 and esp != 0:
        print("\n Seu inimigo joga os espinhos em você causando grande dano!\n")
        jogador.vida -=10
        print(f"\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
    if action == 8:
        print("\nSeu inimigo joga uma faca em você!\n")
        jogador.vida -= 20
        print(f"\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
        
    if inimigo >0:
        if action == 1:
            jogador.vida -=7
            print(f"\nO inimigo te bateu\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
        if AcaoInimigo() == 2:
            pass
        escolha = str(input("O que você ira fazer?"))
        if escolha == "a":
            if action == 2 or action == 4:
                print("\nO inimigo esquivou\n")
            else:    
                if itens.arma == "ADAGA":
                    inimigo -=2
                    print(f"\nVida atual do inimigo: \033[31m{inimigo}\033[m\n")
                elif itens.arma == "ESPADA CURTA":
                    inimigo -=5
                    print(f"\nVida atual do inimigo: \033[31m{inimigo}\033[m\n")
                elif itens.arma == "ESPADA LONGA":
                    inimigo -=10
                    print(f"\nVida atual do inimigo: \033[31m{inimigo}\033[m\n")  
                elif itens.arma == "MÃO":
                    inimigo -=0.1
                    print(f"\nVida atual do inimigo: \033[31m{inimigo:.1f}\033[m\n") 
        elif escolha == "e" and esp == 0:
            esp = 1
            print("\nVocê joga espinhos no chão que causam dano ao inimigo!!\n")
        elif escolha == "e" and esp !=0:
            print("\nVocê já jogou espinhos, epere alguns turnos para lançar de novo!!\n")
    else:
        break
while True:
    print("O Teste de combate acabou!")
    sleep(2)
        
"""   #elif escolha == 4:
        escolha = str(input("\nQuer jogar um dado? S/N ")).upper()[0]
        if escolha == "S":
            print(f"Seu dado foi",JogarDado())
        elif escolha == "N":
            print("Fim do dado")
            break
        else:
            print("Opção invalida!! ")"""