import FreeSimpleGUI as sg

# Constantes
LIN = 6
COL = 7
TAM = 80
COR_BG = "#1E3A8A"
COR_VAZ = "#E5E7EB"
COR_J1 = "#EF4444"  # Vermelho
COR_J2 = "#FACC15"  # Amarelo


def criar_tabuleiro()
    """Cria a matriz 6x7 preenchida com zeros."""
    return [[0 for _ in range(COL)] for _ in range(LIN)]

def inserir_ficha(tab, col, jog):
    """Insere a ficha na posição mais baixa disponível da coluna."""
    for lin in range(LIN - 1, -1, -1):
        if tab[lin][col] == 0:
            tab[lin][col] = jog
            return True
    return False  # Coluna cheia
