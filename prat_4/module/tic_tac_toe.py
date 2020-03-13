class TicTacToe:
    play_id = 0
    line1 = []
    line2 = []
    line3 = []
    game_state = [line1,line2,line3]
    """
        A logica eh a seguinte:
            cada no vai receber o estado do jogo e a id da jogada.
            a medida que formos permutando as jogadas na matriz (colocando x ou o),
            vamos salvando este estado com a nova play_id no nó, e ai vamos inserindo
            estes nós na árvore on-the-go.
    """
