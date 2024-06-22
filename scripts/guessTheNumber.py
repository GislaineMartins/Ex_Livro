# Este é um jogo de adivinhar o número.
import random
secretNumber = random.randint(1, 20)
print('Estou pensando em um número de 1 a 20.')

# Peça para o jogador adivinhar 6 vezes.
for guessesTaken in range(1, 7):
    print('Adivinhe.')
    guess = int(input())

    if guess < secretNumber:
        print('Esse número é baixo')
    elif guess > secretNumber:
        print('Esse número é alto')
    else:
        break # Essa condição corresponde ao palpite correto

if guess == secretNumber:
     print('Bom trabalho! Você adivinhou meu número em ' + str(guessesTaken) + ' palpites!')
else:
    print('Não. O número que eu tinha pensado era: ' + str(secretNumber))
    
    

    
