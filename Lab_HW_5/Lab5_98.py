class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(borders, node):
            if not node:
                return True
            n = node.val
            if n <= borders[0] or n >= borders[1]:
                return False
            return (check([borders[0], n], node.left) and check([n, borders[1]], node.right))
        return check([-10**10, 10**10], root)