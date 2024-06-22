def spam():
    global eggs
    eggs = 'spam' #essa é a variavel global

def bacon():
    eggs = 'bacon' # essa é uma varivel local

def ham():
    print(eggs) # essa é a variavel global

eggs = 42 # essa é a variavel global
spam()
print(eggs)
