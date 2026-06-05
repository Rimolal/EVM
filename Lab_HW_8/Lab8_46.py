from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(cur, remnant):
            if not remnant:
                result.append(cur.copy())
                return
            for i in range(len(remnant)):
                cur.append(remnant[i])
                backtrack(cur, remnant[:i] + remnant[i+1:])
                cur.pop()
        
        backtrack([], nums)
        return result