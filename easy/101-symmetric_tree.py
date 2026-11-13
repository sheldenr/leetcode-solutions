# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def symm(root_a, root_b):
            if not root_a and not root_b:
                return True

            if not (root_a and root_b):
                return False

            return root_a.val == root_b.val and symm(root_a.left, root_b.right) and symm(root_a.right, root_b.left)
        
        return symm(root.left, root.right)

