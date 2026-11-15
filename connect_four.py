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

def desenhar_tabuleiro(graph, tab):
    """Atualiza o desenho das casas e fichas no componente Graph."""
    graph.erase()
    for lin in range(LIN):
        for col in range(COL):
            x1 = col * TAM + 10
            y1 = lin * TAM + 10
            x2 = x1 + TAM - 20
            y2 = y1 + TAM - 20

            val = tab[lin][col]
            cor = COR_VAZ if val == 0 else (COR_J1 if val == 1 else COR_J2)
            # CORREÇÃO AQUI: Passando os pontos como tuplas (x1, y1) e (x2, y2)
            graph.draw_oval(
                (x1, y1),
                (x2, y2),
                fill_color=cor,
                line_color="#111827",
                line_width=2,
            )


def main():
    sg.theme("DefaultNoMoreNagging")
    tab = criar_tabuleiro()
    turno = 1
    fim = False

    layout = [
        [
            sg.Text(
                "Connect Four - INE5201",
                font=("Arial", 16, "bold"),
                justification="center",
                expand_x=True,
            )
        ],
        [
            sg.Text(
                "Turno: Jogador 1 (Vermelho)",
                font=("Arial", 12, "bold"),
                text_color=COR_J1,
                key="-TURNO-",
                justification="center",
                expand_x=True,
            )
        ],
        [
            sg.Graph(
                canvas_size=(COL * TAM, LIN * TAM),
                graph_bottom_left=(0, LIN * TAM),
                graph_top_right=(COL * TAM, 0),
                key="-GRAPH-",
                background_color=COR_BG,
                enable_events=True,
            )
        ],
        [
            sg.Button("Reiniciar Jogo", font=("Arial", 11, "bold")),
            sg.Button("Sair", font=("Arial", 11)),
        ],
    ]

    window = sg.Window("Connect Four - FreeSimpleGUI", layout, finalize=True)
    graph = window["-GRAPH-"]
    desenhar_tabuleiro(graph, tab)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Sair":
            break

        if event == "Reiniciar Jogo":
            tab = criar_tabuleiro()
            turno = 1
            fim = False
            window["-TURNO-"].update(
                "Turno: Jogador 1 (Vermelho)", text_color=COR_J1
            )
            desenhar_tabuleiro(graph, tab)
            continue

        if event == "-GRAPH-" and not fim:
            mouse_x, mouse_y = values["-GRAPH-"]
            col = int(mouse_x // TAM)

            if 0 <= col < COL:
                if not inserir_ficha(tab, col, turno):
                    sg.popup(
                        "Coluna Cheia", "Escolha outra coluna!", title="Aviso"
                    )
                    continue

                desenhar_tabuleiro(graph, tab)

                if verificar_vitoria(tab, turno):
                    fim = True
                    nome = (
                        "Jogador 1 (Vermelho)"
                        if turno == 1
                        else "Jogador 2 (Amarelo)"
                    )
                    window["-TURNO-"].update(
                        f"Vitória do {nome}!", text_color="#059669"
                    )
                    sg.popup(
                        f"Parabéns! {nome} venceu o jogo!", title="Fim de Jogo"
                    )
                    continue

                if tabuleiro_cheio(tab):
                    fim = True
                    window["-TURNO-"].update(
                        "Empate! Tabuleiro cheio.", text_color="#374151"
                    )
                    sg.popup("O jogo empatou!", title="Fim de Jogo")
                    continue

                turno = 2 if turno == 1 else 1
                if turno == 1:
                    window["-TURNO-"].update(
                        "Turno: Jogador 1 (Vermelho)", text_color=COR_J1
                    )
                else:
                    window["-TURNO-"].update(
                        "Turno: Jogador 2 (Amarelo)", text_color="#D97706"
                    )

    window.close()


if __name__ == "__main__":
    main()
    a