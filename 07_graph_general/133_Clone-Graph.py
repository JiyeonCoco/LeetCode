"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        new_graph = {}

        def dfs(n):

            if n in new_graph:
                return new_graph[n]

            new_node = Node(n.val)
            new_graph[n] = new_node

            for nei in n.neighbors:
                cur_nei = dfs(nei)
                new_node.neighbors.append(cur_nei)

            return new_node

        return dfs(node)
