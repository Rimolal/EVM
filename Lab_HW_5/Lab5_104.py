class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        rigth = self.maxDepth(root.right)
        return 1 + max(left, rigth)