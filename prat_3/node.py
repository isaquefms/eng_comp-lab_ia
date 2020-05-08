class Node:
    """
    Classe utilizada para representar um nó de uma árvore de procura.
    """
    def __init__(self, name: str, heuristic: int, cost: int = 0, child_nodes: list = None):
        """
        Construtor do nó. Esses nós representam qualquer objeto da árvore que modelamos.
        Inicialmente, ele será usado para modelar a procura do melhor caminho com o algoritmo A*.
        :param name: Nome da cidade que será atribuída ao nó.
        :param heuristic: Distância em linha reta da cidade atual até a cidade objetivo.
        :param cost: Custo para alcançar o nó. Distância do nó anterior para o atual.
        :param child_nodes: Nós filhos do nó atual
        """
        self.name = name
        self.heuristic: int = heuristic
        self.cost: int = cost
        self.child_nodes: list = []
        # iterando sobre os nós filhos passados, caso eles existam
        if child_nodes:
            for node in child_nodes:
                self.child_nodes.append(node)

    # Getters
    def get_heuristic(self) -> int:
        """
        Retorna a distância em linha reta da cidade atual para a cidade de Bucareste.
        :return: Distância em linha reta para a cidade de Bucareste
        """
        return self.heuristic

    def get_cost(self) -> int:
        """
        Retorna o valor do custo para se alcançar a cidade até o momento.
        :return: Custo para se chegar a cidade.
        """
        return self.cost

    def update_cost(self, father_cost: int):
        self.cost += father_cost

    def get_name(self) -> str:
        """
        Retorna o nome da cidade que foi atribuído ao nó.
        :return: Nome da cidade que foi atribuída ao nó.
        """
        return self.name

    def get_child_nodes(self) -> list:
        """
        Lista dos nós filhos do nó atual. Caso essa lista exista.
        :return: Nós filhos do atual nó.
        """
        return self.child_nodes

    def get_cost_function(self) -> int:
        """
        Retorna o valor total do custo f(n). Sendo este custo igual a f(n) = g(n) + h(n).
        :return: Custo até o momento mais a heurística.
        """
        return self.get_cost() + self.get_heuristic()

    # Setters
    def set_child_node(self, node):
        """
        Atribui um novo nó a lista de nós filhos.
        :param node: Nó filho.
        :return: None
        """
        self.child_nodes.append(node)
