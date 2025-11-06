# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):

            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            root_idx = inorder_map[root_val]

            root = TreeNode(root_val)
            self.pre_idx += 1

            root.left = helper(left, root_idx-1)
            root.right = helper(root_idx+1, right)

            return root

        out_root = helper(0, len(preorder)-1)
        return out_root
