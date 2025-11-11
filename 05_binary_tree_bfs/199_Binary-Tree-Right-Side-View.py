# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque([root])
        prev = None

        right_side = []

        while queue:

            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if not prev:
                    right_side.append(node.val)
                prev = node

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            prev = None

        return right_side
