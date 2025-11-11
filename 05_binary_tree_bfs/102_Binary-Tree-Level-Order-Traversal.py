# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        order_list = []

        while queue:
            size = len(queue)
            cur_list = []

            for _ in range(size):
                node = queue.popleft()
                cur_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            order_list.append(cur_list)

        return order_list
