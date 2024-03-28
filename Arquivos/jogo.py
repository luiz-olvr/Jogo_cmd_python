from Config.Definições import *
esp =0
potion =0
potionI =0

    #Edição de personagem 
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

            
    #começo do jogo
while True:
    if jogador.vida <=0:
        print("\nVOCÊ MORREU!!!\n")
        break
    print("*"*20)
    print(f"Sua vida: \033[32m{jogador.vida}\033[m".center(5))
    print(f"Vida do inimigo: \033[31m{Inimigo.vida}\033[m".center(5))
    print("*"*20)
    action = AcaoInimigo()
    if esp != 0 and esp <= 4 and action != 5:
        Inimigo.vida -= 3
        esp += 1
        print("Seus espinhos causam dano")
        print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")
    if esp == 4:
        esp = 0
    if action == 5 and esp !=0:
        esp =0
        print("\nSeu inimigo tirou os espinhos da arena!\n")
    if action == 7 and esp != 0:
        esp = 0
        print("\n Seu inimigo joga os espinhos em você causando grande dano!\n")
        if itens.armadura == "SEM ARMADURA":
            jogador.vida -= 21
        elif itens.armadura =="ARMADURA LEVE":
            jogador.vida -=13
        elif itens.armadura == "ARMADURA PESADA":
            jogador.vida -=3
        print(f"\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
    if action == 8:
        print("\nSeu inimigo joga uma faca em você!\n")
        if itens.armadura == "SEM ARMADURA":
            jogador.vida -= 25
        elif itens.armadura =="ARMADURA LEVE":
            jogador.vida -=15
        elif itens.armadura == "ARMADURA PESADA":
            jogador.vida -=5
        print(f"\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
        
    if Inimigo.vida >0:
        if action == 1:
            if itens.armadura == "SEM ARMADURA":
                jogador.vida -= 10
            elif itens.armadura =="ARMADURA LEVE":
                jogador.vida -=6
            elif itens.armadura == "ARMADURA PESADA":
                jogador.vida -=2
            print(f"\nO inimigo te bateu\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
        if AcaoInimigo() == 2 and potionI != 4:
            potionI +=1
            Inimigo.vida +=30
            print(f"Seu inimigo usou uma poção, vida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")
        escolhaComb = str(input("O que você ira fazer?"))
        if escolhaComb == "a":
            if action == 2 or action == 4:
                print("\nO inimigo esquivou\n")
            else:    
                if itens.arma == "ADAGA":
                    Inimigo.vida -=2
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")
                elif itens.arma == "ESPADA CURTA":
                    Inimigo.vida -=5
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")
                elif itens.arma == "ESPADA LONGA":
                    Inimigo.vida -=10
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")  
                elif itens.arma == "MÃO":
                    Inimigo.vida -=0.1
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida:.1f}\033[m\n") 
        elif escolhaComb == "e" and esp == 0:
            esp = 1
            print("\nVocê joga espinhos no chão que causam dano ao inimigo!!\n")
        elif escolhaComb == "e" and esp !=0:
            print("\nVocê já jogou espinhos, epere alguns turnos para lançar de novo!!\n")
        elif escolhaComb == "p" and potion != 3:
            potion +=1
            jogador.vida +=20
            print(f"\nVocê usou uma poção de vida, sua vida atual é {jogador.vida}\n")
        elif potion ==3:
            print("Suas poções acabaram\n")


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