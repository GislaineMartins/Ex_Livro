#Este programa diz hello e pergunta o meu nome.
print('Hello world!') # pergunta o nome
print('What is your name?')
myName = input()

print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # pergunta a idade
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
