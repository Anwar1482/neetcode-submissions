"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {node: Node(node.val)}
        
        stack = [node]
        
        while len(stack) !=0:
            current= stack.pop()
            for i in current.neighbors:
                if i not in visited:
                    visited[i] = Node(i.val)
                    stack.append(i)
                visited[current].neighbors.append(visited[i])

        return visited[node]