from dados import boas_vindas, opcoes, pontos_robo, pontos_jogador, escolha, agradecimento, erro
import random

print(boas_vindas)

while True:
    jogador = input(escolha).lower() # Opção do jogador
    robo = random.choice(opcoes) # Escolha aleatória do robô 

    if jogador in opcoes:
        print("\nVocê escolheu " + jogador) # Output das oções do jogador
        print("Eu escolho " + robo) # Output das oções do robô
        
        if jogador == robo: # Empate
            print("\nEmpate! :/\n")
        
        elif jogador == "papel": # PAPEL
            if robo == "tesoura":
                print("\nEu venci! Minha tesoura cortou seu papel :D\n")
                pontos_robo += 1
            else: # robo == "pedra"
                print("\nVocê venceu! Seu papel cobriu minha pedra :(\n")
                pontos_jogador += 1
        
        elif jogador == "tesoura": # TESOURA
            if robo == "papel":
                print("\nVocê venceu! Sua tesoura cortou meu papel :(\n")
                pontos_jogador += 1
            else: # robo == "pedra"
                print("\nEu venci! Minha pedra quebrou sua tesoura :D\n")
                pontos_robo += 1
        
        elif jogador == "pedra": # PEDRA
            if robo == "papel":
                print("\nEu venci! Meu papel enrolou sua pedra :D\n")
                pontos_robo += 1
            else: # robo == tesoura
                print("\nVocê venceu! Sua pedra quebrou minha tesoura :(\n")
                
                pontos_jogador += 1
        print("---------PLACAR---------")
        print("Eu: " + str(pontos_jogador))
        print("Robô: " + str(pontos_robo))
        print("------------------------")
    
    elif jogador == "sair":
        print(agradecimento)
        break
    
    else:
        print(erro)
