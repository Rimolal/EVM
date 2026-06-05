class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(x, y, visited):
            visited[x][y] = True
            for b_x, b_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                cur_x, cur_y = x + b_x, y + b_y
                if 0 <= cur_x < m and 0 <= cur_y < n:
                    if not visited[cur_x][cur_y] and heights[cur_x][cur_y] >= heights[x][y]:
                        dfs(cur_x, cur_y, visited)
        
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        for i in range(m):
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(m-1, j, atlantic)
        
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        return result