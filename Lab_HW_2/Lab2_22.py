from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def recur(cur: str, open_count: int, close_count: int):
            if len(cur) == 2 * n:
                result.append(cur)
                return
            
            if open_count < n:
                recur(cur + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                recur(cur + ')', open_count, close_count + 1)
        
        recur('', 0, 0)
        return result
    
    
n = 3
solution = Solution()
print(solution.generateParenthesis(3))