from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        result = []
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        result = sorted(dict.keys(), key=lambda x: dict[x])
        return result[-k:]
    
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k))