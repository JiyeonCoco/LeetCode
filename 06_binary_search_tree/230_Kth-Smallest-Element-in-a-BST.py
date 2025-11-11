# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 
        
        self.cnt = 0
        self.k = k
        self.k_num = -1

        def order_tree(node):

            if not node:
                return

            order_tree(node.left)
            self.cnt += 1

            if self.cnt == self.k:
                self.k_num = node.val
                
            order_tree(node.right)

            return self.k_num
 
        return order_tree(root)
