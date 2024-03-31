from Config.Definições import *
esp =0
potion =0
potionI =0

    #Edição de personagem 
MenuPersonalizacao()
           
    #começo do jogo
while True:
    if jogador.vida <=0:
        print("\nVOCÊ MORREU!!!\n")
        break
    if Inimigo.vida >0:
        print("*"*20)
        print(f"Sua vida: \033[32m{jogador.vida}\033[m".center(5))
        print(f"Vida do inimigo: \033[31m{Inimigo.vida}\033[m".center(5))
        print("*"*20)
        action = AcaoInimigo()
        escolhaComb = str(input("O que você ira fazer?"))
        if escolhaComb == "a":
            if action == 2 or action == 4:
                print("\nO inimigo esquivou\n")
            else:    
                if itens.arma == "ADAGA":
                    Inimigo.vida -=2 + 0.2*jogador.força
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")
                elif itens.arma == "ESPADA CURTA":
                    Inimigo.vida -=5 + 0.2*jogador.força
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")
                elif itens.arma == "ESPADA LONGA":
                    Inimigo.vida -=10 + 0.2*jogador.força
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida}\033[m\n")  
                elif itens.arma == "MÃO":
                    Inimigo.vida -=0.1 + 0.2*jogador.força
                    print(f"\nVida atual do inimigo: \033[31m{Inimigo.vida:.1f}\033[m\n") 
        if escolhaComb == "e" and esp == 0:
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
            
        #Ação do inimigo 
        
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
                jogador.vida -= 21 + 0.2*Inimigo.força
            elif itens.armadura =="ARMADURA LEVE":
                jogador.vida -=13 + 0.2*Inimigo.força
            elif itens.armadura == "ARMADURA PESADA":
                jogador.vida -=3 + 0.2*Inimigo.força
            print(f"\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
        if action == 8:
            print("\nSeu inimigo joga uma faca em você!\n")
            if itens.armadura == "SEM ARMADURA":
                jogador.vida -= 25 + 0.2*Inimigo.força
            elif itens.armadura =="ARMADURA LEVE":
                jogador.vida -=15+ 0.2*Inimigo.força
            elif itens.armadura == "ARMADURA PESADA":
                jogador.vida -=5+ 0.2*Inimigo.força
            print(f"\nSua vida atual é: \033[32m{jogador.vida}\033[m\n")
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
          
    else:
        break

while True:
    print("O Teste de combate acabou!")
    sleep(2)
