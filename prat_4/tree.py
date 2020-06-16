import math
from .node import Node
# from node import Node


class Tree:
    """Classe responsável por fazer a representação da árvore no nosso problema
    do algoritmo minmax.
    """

    def __init__(self, root_node: Node):
        """
        Construtor da classe. Quando criamos uma árvore do jogo, o nó raiz é o
        nó que contém o estado inicial, onde todos os seus campos são com
        valores iguais a string vazia.
        Args:
            root_node: Nó pai, ou primeiro nível na hierarquia da árvore.
        """
        self.root_node = root_node
        self.root_node.set_state(Node.initial_state())

    def mount_all_possibilites_tree(self, initial_caracter: str = 'x') -> None:
        """
        Método que monta a árvore com todas as possibilidades do jogo da velha.
        Para a montagem ele utiliza o próprio pai dos nós como referência.
        Args:
            initial_caracter: Caracter inicial.
        Returns: None
        """
        # avaliação dos estados iniciais passados como parâmetro
        if initial_caracter == 'x':
            second_caracter = 'o'
        elif initial_caracter == 'o':
            second_caracter = 'x'
        # caso haja alguma coisa fora do padrão, voltamos ao padrão
        else:
            initial_caracter = 'x'
            second_caracter = 'o'
        # define a profundidade da iteração atual
        depth: int = 0  # 0 profundidade inicial e 9 profundidade final
        # fila de possibilidades a serem tratadas
        queue: List[dict] = []
        # adicionamos a raiz na fila
        queue.append(self.root_node)
        # enquanto a fila não estiver vazia
        while queue != []:
            father = queue.pop(0) # obtemos o primeiro nó da fila
            # se chegarmos a maior profundidade, já montamos todas as possibilidades
            if depth == 9:
                return
            # se não for o último objeto montados os seus filhos com base nele
            father_state: dict = father.get_state() # estado do pai
            child_nodes List[Node] = [] # lista que armazenará os filhos
            # para cada campo não preenchido, ele adiciona o campo e envia o mesmo a um nó filho
            for line in range(4):
                for column in range(4):
                    key = int(f'{line}{column}')
                    # se na determinada posição avaliada não houver marcações
                    if father_state[key] == '':
                        # adicionamos uma marcação
                        child_state = father_state
                        child_state[key] = initial_caracter
                        child = Node(child_state)
                        child_nodes.append(child)
                        queue.append(child)
                        father.set_child_node(child)

    def deep_search(self, root_node: Node, search_state: dict) -> bool:
        """
        Realiza a busca em profundidade na árvore de estados.
        Args:
            root_node: Nó inicial de pesquisa.
            search_state: Estado que desejamos procurar.

        Returns: True em caso de estado encontrado e False caso contrário.
        """
        # caso base da recursão, se o nó for o nó procurado
        if root_node.state_is_equal(search_state):
            return True
        # começamos pesquisando todos os nós do nó raiz
        child_nodes = root_node.get_child_nodes()
        for child_node in child_nodes:
            # encontrou
            if child_node.state_is_equal(search_state):
                return True
            # não encontrou na profundidade atual porém tem filhos
            elif child_node.get_child_nodes():
                # chamada recursiva e verificação ao mesmo tempo
                if self.deep_search(child_node, search_state):
                    return True
            # é nó terminal, não sendo o que nós queremos e não tem filho, segue para o nó "irmão"
        # se ao final não encontrar nada, podemos retornar false
        return False

    def minmax_algorithm(self, node: Node, depth: int, maxmizing_player: bool) -> int:
        """
        Implementação do algoritmo minmax.
        Args:
            node: Nó raiz para início do cálculo do algoritmo.
            depth: Profundidade de pesquisa.
            maxmizing_player: Flag que habilita se iremos maximizar ou minimizar.

        Returns: Inteiro da avaliação realizada na iteração atual.
        """
        # se caso a profundidade tenha sido alcançada ou o nó não tenha filhos
        if depth == 0 or not node.get_child_nodes():
            return node.get_utility()
        # caso o objetivo seja maximizar a jogada
        if maxmizing_player:
            # atribuímos um valor exorbitante para comparação
            value = -math.inf
            # para cada filho avaliamos qual será a jogada maximizada
            for child in node.get_child_nodes():
                # para isso avaliamos a qual foi a menor jogada do nível inferior
                value = max(value, self.minmax_algorithm(child, depth-1, False))
            return value
        # caso o objetivo seja minimizar a jogada
        else:
            value = math.inf
            # analisamos o valor que possui a jogada minimizada
            for child in node.get_child_nodes():
                # para isso avaliamos qual foi a maior jogada no nível inferior
                value = min(value, self.minmax_algorithm(child, depth-1, True))
            return value
