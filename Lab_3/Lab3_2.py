from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        summa = sum(nums[0: k])
        maxim = summa/k
        for r in range(k, len(nums)):
            summa += nums[r]
            summa -= nums[r - k]
            maxim = max(maxim, summa/k)
        return maxim
        
nums = [1,12,-5,-6,50,3]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))