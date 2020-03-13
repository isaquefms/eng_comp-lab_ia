from .node import Node


class Tree:
    """
    Classe responsável por fazer a representação da árvore no nosso problema do algoritmo A*.
    """
    def __init__(self, father_node: Node):
        """
        Construtor da classe.
        :param father_node: Nó pai, ou primeiro nível na hierarquia da árvore.
        """
        self.father_node = father_node

    def search_a_star(self) -> str:
        """
        Algoritmo A* na prática. Ele irá procurar pelos filhos do nó pai e exibir o custo de cada um dos filhos pela
        função f(n) = g(n) + h(n).
        :return: Custo para se alcançar cada uma das cidades.
        """
        # busca por todos os filhos do nó pai
        child_nodes = self.father_node.get_child_nodes()
        # iteramos por esses filhos para mostrar o custo para alcançar o mesmo mais a heurística
        print('Partindo de {}'.format(self.father_node.get_name()))
        for child_node in child_nodes:
            print('Chegamos a {} com custo de {} mais {}'.format(child_node.get_name, child_node.get_cost,
                                                                 child_node.get_heuristic))
            # Todo: Agora precisamos verificar como vamos montar a borda e fazer essa mesma iteração sobre o nós filhos
            #   do nó escolhido nessa iteração.
