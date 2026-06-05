from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, cur):
            result.append(cur.copy())
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        backtrack(0, [])
        return result