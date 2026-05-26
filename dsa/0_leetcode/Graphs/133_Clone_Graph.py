# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node):
        if not node:
            return
        cloned = {}

        def clone(node):
            if node in cloned:
                return cloned[node]

            temp = Node(node.val)
            cloned[node] = temp

            for neighbor in node.neighbors:
                if neighbor not in cloned:
                    temp.neighbors.append(clone(neighbor))
                else:
                    temp.neighbors.append(cloned[neighbor])

            return cloned[node]

        clone(node)
        return cloned[node]
