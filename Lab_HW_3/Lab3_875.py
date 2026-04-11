from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            sum_h = 0
            for i in piles:
                sum_h += math.ceil(i / mid)
            if sum_h <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

piles = [3,6,7,11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))