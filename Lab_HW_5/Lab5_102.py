class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(node, count):
            if not node:
                return
            if len(result) == count:
                result.append([])
            result[count].append(node.val)
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        dfs(root, 0)
        return result