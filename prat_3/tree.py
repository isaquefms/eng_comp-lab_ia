import sys
import math

from node import Node


class Tree:
    """
    Classe responsável por fazer a representação da árvore no nosso problema do algoritmo A*.
    """
    # Borda da procura executada pelo algoritmo A*
    edge: list = []

    def __init__(self, root_node: Node):
        """
        Construtor da classe.
        :param root_node: Nó pai, ou primeiro nível na hierarquia da árvore.
        """
        self.root_node = root_node

    @staticmethod
    def deep_search(root_node: Node, name: str) -> bool:
        """
        Método que realiza a busca em profundidade em uma árvore.
        :param root_node: Nó raiz da árvore.
        :param name: Nome do nó que queremos procurar.
        :return: Sucesso ou falha na busca por esse nó.
        """
        # começamos pesquisando todos os nós do nó raiz
        child_nodes = root_node.get_child_nodes()
        for child_node in child_nodes:
            # encontrou
            if child_node.get_name() == name:
                return True
            # não encontrou na primeira profundidade porém tem filhos
            elif child_node.get_child_nodes():
                return Tree.deep_search(child_node, name)
            # é nó terminal, não sendo o que nós queremos e não tem filho
            else:
                continue
        return False

    def search_a_star(self, node: Node, destiny: str):
        """
        Algoritmo A* na prática. Ele irá procurar pelos filhos do nó pai e exibir o custo de cada um dos filhos pela
        função f(n) = g(n) + h(n).
        :return: Custo para se alcançar cada uma das cidades.
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
