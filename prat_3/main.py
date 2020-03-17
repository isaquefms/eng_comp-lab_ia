from node import Node
from tree import Tree


def test():
    # criando os nós
    arad = Node(name='Arad', heuristic=360, cost=0)
    timisoara = Node(name='Timisoara', heuristic=329, cost=118)
    lugoj = Node(name='Lugoj', heuristic=244, cost=111)
    mehadia = Node(name='Mehadia', heuristic=241, cost=70)
    dobreta = Node(name='Dobreta', heuristic=242, cost=75)
    craiova = Node(name='Craiova', heuristic=160, cost=120)  # possui dois pais
    pitesti_from_craiova = Node(name='Pitesti', heuristic=10, cost=138)  # possui dois pais
    pitesti_from_rimnu_vilcea = Node(name='Pitesti', heuristic=10, cost=97)
    bucharest_from_fagaras = Node(name='Bucharest', heuristic=0, cost=211)
    bucharest_from_pitesti = Node(name='Bucharest', heuristic=0, cost=101)
    fagaras = Node(name='Fagaras', heuristic=176, cost=99)
    giurgiu = Node(name='Giurgiu', heuristic=77, cost=90)
    zerind = Node(name='Zerind', heuristic=374, cost=75)
    oradea = Node(name='Oradea', heuristic=380, cost=71)
    sibiu_from_oradea = Node(name='Sibiu', heuristic=253, cost=151)  # possui dois pais
    sibiu_from_arad = Node(name='Sibiu', heuristic=253, cost=140)  # possui dois pais
    pagaras = Node(name='Pagaras', heuristic=500, cost=99)
    rimnicu_vilcea_from_sibiu = Node(name='Rimnicu Vilcea', heuristic=193, cost=80)
    rimnicu_vilcea_from_craiova = Node(name='Rimnicu Vilcea', heuristic=193, cost=146)
    urziceni = Node(name='Urziceni', heuristic=80, cost=85)
    hirsova = Node(name='Hirsova', heuristic=151, cost=98)
    eforie = Node(name='Eforie', heuristic=161, cost=85)
    vaslui = Node(name='Vaslui', heuristic=199, cost=142)
    iasi = Node(name='Iasi', heuristic=226, cost=92)
    neamt = Node(name='Neamt', heuristic=234, cost=87)


    arad.set_child_node(timisoara)
    arad.set_child_node(zerind)
    arad.set_child_node(sibiu_from_arad)
    timisoara.set_child_node(lugoj)
    lugoj.set_child_node(mehadia)
    mehadia.set_child_node(dobreta)
    dobreta.set_child_node(craiova)
    craiova.set_child_node(rimnicu_vilcea_from_craiova)
    craiova.set_child_node(pitesti_from_craiova)
    rimnicu_vilcea_from_craiova.set_child_node(pitesti_from_rimnu_vilcea)
    rimnicu_vilcea_from_sibiu.set_child_node(pitesti_from_rimnu_vilcea)
    zerind.set_child_node(oradea)
    oradea.set_child_node(sibiu_from_oradea)
    sibiu_from_oradea.set_child_node(rimnicu_vilcea_from_sibiu)
    sibiu_from_oradea.set_child_node(fagaras)
    sibiu_from_arad.set_child_node(rimnicu_vilcea_from_sibiu)
    sibiu_from_arad.set_child_node(fagaras)
    fagaras.set_child_node(bucharest_from_fagaras)
    pitesti_from_rimnu_vilcea.set_child_node(bucharest_from_pitesti)
    pitesti_from_craiova.set_child_node(bucharest_from_pitesti)

    tree = Tree(arad)
    found_node = tree.search_a_star(arad, 'Bucharest')
    print(found_node)


if __name__ == '__main__':
    test()
