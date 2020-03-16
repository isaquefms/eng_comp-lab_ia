from node import Node
from tree import Tree


def test():
    # criando os nós
    arad = Node(name='Arad', heuristic=360)
    timisoara = Node(name='Timisoara', heuristic=329, cost=118)
    lugoj = Node(name='Lugoj', heuristic=244, cost=111)
    mehadia = Node(name='Mehadia', heuristic=241, cost=70)
    dobreta = Node(name='Dobreta', heuristic=242, cost=75)
    craiova = Node(name='Craiova', heuristic=160, cost=120)  # possui dois pais
    pitesti = Node(name='Pitesti', heuristic=10, cost=138)  # possui dois pais
    bucharest = Node(name='Bucharest', heuristic=0, cost=101)
    giurgiu = Node(name='Giurgiu', heuritic=77, cost=90)
    zerind = Node(name='Zerind', heuristic=374, cost=75)
    oradea = Node(name='Oradea', heuristic=380, cost=71)
    sibiu = Node(name='Sibiu', heuristic=253, cost=151)  # possui dois pais
    pagaras = Node(name='Pagaras', heuristic=500, cost=99)
    rimnicu_vilcea = Node(name='Rimnicu Vilcea', heuristic=193, cost=80)
    urziceni = Node(name='Urziceni', heuristic=80, cost=85)
    hirsova = Node(name='Hirsova', heuristic=151, cost=98)
    eforie = Node(name='Eforie', heuristic=161, cost=85)
    vaslui = Node(name='Vaslui', heuristic=199, cost=142)
    iasi = Node(name='Iasi', heuristic=226, cost=92)
    neamt = Node(name='Neamt', heuristic=234, cost=87)

    # setando os nós filhos
    node_2.set_child_node(node_5)
    node_2.set_child_node(node_6)
    node_1.set_child_node(node_3)
    node_1.set_child_node(node_4)
    node_root.set_child_node(node_1)
    node_root.set_child_node(node_2)

    tree = Tree(node_root)
    found_node = tree.deep_search(root_node=node_root, name='node 6')
    print(found_node)


if __name__ == '__main__':
    test()
