# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min_dif = 100000
        self.prev = None

        def cal_dif(node):

            if not node:
                return

            cal_dif(node.left)

            if self.prev != None:
                self.min_dif = min(self.min_dif, node.val-self.prev)

            self.prev = node.val

            cal_dif(node.right)

        cal_dif(root)
        return self.min_dif
