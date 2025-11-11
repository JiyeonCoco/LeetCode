# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        queue = deque([root])
        avg_list = []

        while queue:

            size = len(queue)
            sum_val = 0
            
            for _ in range(size):
                node = queue.popleft()
                sum_val += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            avg_val = sum_val / size
            avg_list.append(avg_val)

        return avg_list

        
