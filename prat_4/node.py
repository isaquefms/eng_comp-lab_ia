class Node:
    """ Classe utilizada para representar um nó de uma árvore de procura. Para a prática 4 precisamos de uma pequena
    alteração. Agora um nó contém também um estado que pode não ser informado. Esse nó irá armazenar o estado do jogo
    da velha naquele momento. Vamos adicionar um método que retorna o estado do nó.
    """
    def __init__(self, state: dict, utility: int = 0, child_nodes: list = None):
        """
        Construtor do nó. Esses nós representam qualquer objeto da árvore que modelamos.
        O nó atualmente representa um estado do jogo da velha. Modelagem necessária para a prática 4.
        Args:
            state: Estado que o nó representa no jogo da velha.
            utility: Avaliação desse estado de acordo com o jogo. Será definido via algoritmo maxmin.
            child_nodes: Nós filhos do nó atual.
        """
        self.state = state
        self.utility = utility
        # iterando sobre os nós filhos passados, caso eles existam
        if child_nodes:
            for node in child_nodes:
                self.child_nodes.append(node)
        else:
            self.child_nodes = child_nodes

    # Getters
    def get_state(self) -> dict:
        """
        Retorna o estado do nó atual.
        Returns: Dicionário com os valores dos estados atuais.
        """
        return self.state

    def get_utility(self) -> int:
        """
        Retorna o valor de utilidade do estado atual.
        Returns: Inteiro representando o valor de utilidade do estado atual.
        """
        return self.utility

    def get_child_nodes(self) -> list:
        """
        Lista dos nós filhos do nó atual. Caso essa lista exista.
        Returns: Nós filhos do atual nó.
        """
        return self.child_nodes

    # Setters
    def set_child_node(self, node) -> None:
        """
        Atribui um novo nó a lista de nós filhos.
        Args:
            node: No filho que será adicionado.

        Returns: None
        """
        self.child_nodes.append(node)

    def set_state(self, state: dict) -> None:
        """
        Atribui um valor ao estado do nó.
        Args:
            state: Estado do jogo da velha.

        Returns: None
        """
        self.state = state

    def set_utility(self, utility: int) -> None:
        """
        Atribui um valor de utilidade ao nó atual.
        Args:
            utility: Inteiro representando a utilidade do nó e ao mesmo tempo do estado também.

        Returns: None
        """
        self.utility = utility
