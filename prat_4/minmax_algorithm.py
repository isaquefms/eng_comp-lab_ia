# Pseudocódigo do algoritmo minmax
"""
function minmax(node, depth, maxmizingPlayer):
    if depth == 0 or node is a terminal node:
        return the heuristic value of node
    if maxmizingPlayer:
        value = - infinity
        for child in node.childs():
            value = max(value, minmax(child, depth-1, False))
        return value
    else:
        value = + infinity
        for child in node.childs():
            value = min(value, minmax(child, depth-1, True))
        return value
"""

# Initial call
# minmax(origin, depth, True)
