import pyperclip

def add_bullet_points(text):
    # Divide o texto em linhas
    lines = text.split('\n')
    # Adiciona um asterisco a cada linha
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i]
    # Junta as linhas novamente em um único texto
    return '\n'.join(lines)

# Passo 1: Obter o texto do clipboard
text = pyperclip.paste()

# Passo 2: Fazer algo com o texto (adicionar marcadores)
new_text = add_bullet_points(text)

# Passo 3: Copiar o novo texto para o clipboard
pyperclip.copy(new_text)

print("Texto processado e copiado para o clipboard.")
