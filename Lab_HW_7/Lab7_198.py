from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        houses = [0]*n
        houses[0], houses[1] = nums[0], nums[1]
        houses[2] = max(nums[2] + houses[0], houses[1])
        for i in range(3,n):
            houses[i] = max(nums[i] + max(houses[i-3], houses[i-2]), houses[i-1])
        return max(houses[n-2], houses[n-1])