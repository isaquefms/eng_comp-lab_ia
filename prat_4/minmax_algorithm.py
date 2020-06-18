from tree import Tree
from node import Node

if __name__ == '__main__':
    root_node = Node(Node.initial_state())
    tree = Tree(root_node)
    print(tree)