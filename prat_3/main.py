from node import Node
from tree import Tree


def test():
    node_root = Node(name='root_node', heuristic=0)
    node_1 = Node(name='node 1', heuristic=1)
    node_2 = Node(name='node 2', heuristic=2)
    node_3 = Node(name='node 3', heuristic=3)
    node_4 = Node(name='node 4', heuristic=4)
    node_5 = Node(name='node 5', heuristic=5)
    node_6 = Node(name='node 6', heuristic=6)

    # setando os nós filhos
    node_2.set_child_node(node_5)
    node_2.set_child_node(node_6)
    node_1.set_child_node(node_3)
    node_1.set_child_node(node_4)
    node_root.set_child_node(node_1)
    node_root.set_child_node(node_2)

    tree = Tree(node_root)
    found_node = tree.deep_search(root_node=node_root, name='node 2')
    print(found_node)


if __name__ == '__main__':
    test()
