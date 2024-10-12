"""A binary tree is uni-valued if every node in the tree
has the same value.Given the root of a binary tree,
 return true if the given tree is uni-valued, or false otherwise."""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val

        def uni(root, value):
            if not root:
                return True
            elif root.val != value:
                return False
            return uni(root.left, value) and uni(root.right, value)

        return uni(root, value)
