import pyperclip

def adicionar_marcadores(texto, marcador='-'):
    """
    Adiciona um marcador no início de cada linha de um texto.

    Args:
    texto (str): O texto ao qual os marcadores serão adicionados.
    marcador (str): O marcador a ser adicionado no início de cada linha.

    Returns:
    str: O texto com marcadores adicionados.
    """
    linhas = texto.split('\n')
    linhas_com_marcadores = [f"{marcador} {linha}" for linha in linhas]
    return '\n'.join(linhas_com_marcadores)

# Pega o texto da área de transferência
texto_original = pyperclip.paste()

# Adiciona os marcadores
texto_com_marcadores = adicionar_marcadores(texto_original, marcador='*')

# Copia o texto com marcadores de volta para a área de transferência
pyperclip.copy(texto_com_marcadores)

print("Texto com marcadores copiado para a área de transferência.")
