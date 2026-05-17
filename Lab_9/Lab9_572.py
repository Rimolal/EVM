class Solution:
    def isSametree(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        if not first and not second:
            return True
        if not first or not second:
            return False
        if first.val != second.val:
            return False
        return self.isSametree(first.left, second.left) and self.isSametree(first.right, second.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    