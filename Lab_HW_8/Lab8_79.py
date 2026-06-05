from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def backtrack(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row][col] or board[row][col] != word[i]):
                return False

            visited[row][col] = True
            
            found = (backtrack(row + 1, col, i + 1) or
                    backtrack(row - 1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row, col - 1, i + 1))
            visited[row][col] = False
            return found
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False