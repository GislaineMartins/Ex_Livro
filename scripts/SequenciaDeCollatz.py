def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
    try:
        numero = int(input('Digite um valor inteiro:'))
        break
    except ValueError:
         print('Erro: Digite um número inteiro válido.') 

numero = numero + 1 


for n in range(1,numero):
    print('numero de vezes: {}'.format(n))
    print(collatz(numero))
    numero = numero -1

     
    
