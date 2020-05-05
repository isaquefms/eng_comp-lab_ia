import math
from .node import Node
# from node import Node


class Tree:
    """
    Classe responsável por fazer a representação da árvore no nosso problema do algoritmo minmax.
    """

    def __init__(self, root_node: Node):
        """
        Construtor da classe. Quando criamos uma árvore do jogo, o nó raiz é o nó que contém o estado inicial, onde
        todos os seus campos são com valores iguais a string vazia.
        Args:
            root_node: Nó pai, ou primeiro nível na hierarquia da árvore.
        """
        self.root_node = root_node

    @staticmethod
    def initial_state() -> dict:
        """
        Monta um dicionário com os valores representando o estado inicial. Nesse dicionário, todas as posições são
        preenchidas com string vazia, inicio de um jogo da velha.
        Returns: Dicionário com o estado inicial do jogo da velha.
        """
        return_dict: dict = {}
        for line in range(1, 4):
            for column in range(1, 4):
                key = int('{}{}'.format(line, column))  # chave do dicionário será a string representante da posição
                return_dict[key] = ''  # todas as posições do dicionário serão preenchidas com uma string vazia
        return return_dict

    @staticmethod
    def deep_search(root_node: Node, name: str) -> bool:
        """
        Método que realiza a busca em profundidade em uma árvore.
        :param root_node: Nó raiz da árvore.
        :param name: Nome do nó que queremos procurar.
        :return: Sucesso ou falha na busca por esse nó.
        """
        # caso base da recursão, se o nó for o nó procurado
        if root_node.get_name() == name:
            return True
        # começamos pesquisando todos os nós do nó raiz
        child_nodes = root_node.get_child_nodes()
        for child_node in child_nodes:
            # exibe o nó visitado atualmente
            print(child_node.get_name())
            # encontrou
            if child_node.get_name() == name:
                return True
            # não encontrou na profundidade atual porém tem filhos
            elif child_node.get_child_nodes():
                # chamada recursiva e verificação ao mesmo tempo
                if Tree.deep_search(child_node, name):
                    return True
            # é nó terminal, não sendo o que nós queremos e não tem filho, segue para o nó "irmão"
        # se ao final não encontrar nada, podemos retornar false
        return False

    def search_a_star(self, node: Node, destiny: str) -> None:
        """
        Algoritmo A* implementado. Ele irá procurar pelos filhos do nó pai e exibir o custo de cada um dos filhos pela
        função f(n) = g(n) + h(n).
        :return:
        Args:
            node: Nó raiz.
            destiny: String com o destino que desejamos alcançar.

        Returns: Não há retorno.
        """
        # exibição das mensagens
        print('Estou em: {}'.format(node.get_name()))
        print('Preço real para se chegar ate aqui: {}'.format(node.get_cost()))
        print('Distância em linha reta até Bucareste: {}'.format(node.get_heuristic()))
        print('Preço total: {}'.format(node.get_cost_function()))

        # caso base, o no atual é o nó procurado
        if node.get_name() == destiny:
            return
        # atualizar a borda
        for child_node in node.get_child_nodes():
            self.edge.append(child_node)
        # procura pelo nó mais barato para expandir
        price: float = math.inf  # nesse caso atribuímos a price um valor infinito
        priceless_node: Node = None  # futuro nó mais barato
        # para cada nó na borda
        for edge_node in self.edge:
            if edge_node.get_cost_function() < price:
                priceless_node: Node = edge_node
                price = edge_node.get_cost_function()
        # retirar o nó da borda
        self.edge.remove(node)
        self.search_a_star(priceless_node, destiny)

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
            return node.get_heuristic()
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
