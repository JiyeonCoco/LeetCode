# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.check = True
        self.prev_val = None

        def check_tree(node):

            if not node:
                return

            check_tree(node.left)

            if (self.prev_val != None) and (self.prev_val >= node.val):
                self.check = False
            
            self.prev_val = node.val

            check_tree(node.right)

        check_tree(root)
        
        return self.check
