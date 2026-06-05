from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, cur, remnant):
            if remnant == 0:
                result.append(cur.copy())
                return
            if remnant < 0:
                return
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                backtrack(i, cur, remnant - candidates[i])
                cur.pop()
        backtrack(0, [], target)
        return result