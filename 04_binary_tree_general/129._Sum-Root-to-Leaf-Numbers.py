# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        total_sums = 0
        stack = [(root, 0)]

        while stack:
            node, cur_sum = stack.pop()
            cur_sum = (cur_sum * 10) + node.val

            if not node.left and not node.right:
                total_sums += cur_sum
            else:
                if node.right:
                    stack.append((node.right, cur_sum))
                if node.left:
                    stack.append((node.left, cur_sum))

        return total_sums
