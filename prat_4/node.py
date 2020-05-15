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
        self.calculate_utility()  # calcula o valor de utilidade do nó (condição de vitória e derrota)

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

    # Methods
    def state_is_equal(self, other_state: dict) -> bool:
        """
        Compara se um passado como parâmetro é igual ao estado armazenado no nó.
        Args:
            other_state: Estado a se comparar.

        Returns: Valor booleano informando se o estado é igual ou diferente.
        """
        for line in range(1, 4):
            for column in range(1, 4):
                key = int('{}{}'.forma(line, column))
                # caso os elementos de mesma chave sejam diferentes
                if self.state[key] != other_state[key]:
                    return False  # já aceleramos o processo retornando falso na operação
        return True  # se passar por todas as comparações os estados são iguais

    def calculate_utility(self, max_char='x') -> None:
        """
        Calcula o valor de utilidade do nó de acordo com o estado e também com a variável de vitória.
        Args:
            max_char: Caracter que buscamos como o definidor de vitória. Vamos definir ele como o máximo

        Returns: None
        """
        min_char: str = ''
        # começamos definindo o caracter de minimização
        if max_char == 'x':
            min_char = 'o'
        elif max_char == 'o':
            min_char = 'x'
        elif max_char != 'x' and max_char != 'o':  # caso onde houve um erro nas atribuições
            # voltamos aos valores padrão
            max_char = 'x'
            min_char = 'o'
        # teste das oito condições de vitória ou derrota
        # primeira condição
        if self.state[11] == max_char and self.state[12] == max_char and self.state[13] == max_char:
            self.utility = 1
            return
        elif self.state[11] == min_char and self.state[12] == min_char and self.state[13] == min_char:
            self.utility = -1
            return
        # segunda condição
        elif self.state[21] == max_char and self.state[22] == max_char and self.state[23] == max_char:
            self.utility = 1
            return
        elif self.state[21] == min_char and self.state[22] == min_char and self.state[23] == min_char:
            self.utility = -1
            return
        # terceira condição
        elif self.state[31] == max_char and self.state[32] == max_char and self.state[33] == max_char:
            self.utility = 1
            return
        elif self.state[31] == min_char and self.state[32] == min_char and self.state[33] == min_char:
            self.utility = -1
            return
        # quarta condição
        elif self.state[11] == max_char and self.state[21] == max_char and self.state[31] == max_char:
            self.utility = 1
            return
        elif self.state[11] == min_char and self.state[21] == min_char and self.state[31] == min_char:
            self.utility = -1
            return
        # quinta condição
        elif self.state[12] == max_char and self.state[22] == max_char and self.state[32] == max_char:
            self.utility = 1
            return
        elif self.state[12] == min_char and self.state[22] == min_char and self.state[32] == min_char:
            self.utility = -1
            return
        # sexta condição
        elif self.state[13] == max_char and self.state[23] == max_char and self.state[33] == max_char:
            self.utility = 1
            return
        elif self.state[13] == min_char and self.state[23] == min_char and self.state[33] == min_char:
            self.utility = -1
            return
        # sétima condição
        elif self.state[11] == max_char and self.state[22] == max_char and self.state[33] == max_char:
            self.utility = 1
            return
        elif self.state[11] == min_char and self.state[22] == min_char and self.state[33] == min_char:
            self.utility = -1
            return
        # oitava condição
        elif self.state[31] == max_char and self.state[22] == max_char and self.state[13] == max_char:
            self.utility = 1
            return
        elif self.state[31] == min_char and self.state[22] == min_char and self.state[13] == min_char:
            self.utility = -1
            return
        # se caso nenhuma das condições de vitória forem satisfeitas logos temos 0 utilidade ou um empate
        else:
            self.utility = 0

    # Static methods
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
