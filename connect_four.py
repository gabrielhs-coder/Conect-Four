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

def verificar_vitoria(tab, jog):
    """Verifica 4 fichas alinhadas na horizontal, vertical e diagonais."""
    # Horizontal
    for lin in range(LIN):
        for col in range(COL - 3):
            if all(tab[lin][col + i] == jog for i in range(4)):
                return True

    # Vertical
    for lin in range(LIN - 3):
        for col in range(COL):
            if all(tab[lin + i][col] == jog for i in range(4)):
                return True

    # Diagonal principal (\)
    for lin in range(LIN - 3):
        for col in range(COL - 3):
            if all(tab[lin + i][col + i] == jog for i in range(4)):
                return True

    # Diagonal secundária (/)
    for lin in range(3, LIN):
        for col in range(COL - 3):
            if all(tab[lin - i][col + i] == jog for i in range(4)):
                return True

    return False


def tabuleiro_cheio(tab):
    """Retorna True se o topo estiver completamente ocupado."""
    return all(tab[0][col] != 0 for col in range(COL))
