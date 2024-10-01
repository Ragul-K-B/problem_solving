class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(r):
            if not r:
                return None

            r.left, r.right = r.right, r.left

            invert(r.left)
            invert(r.right)

            return r

        return invert(root)
