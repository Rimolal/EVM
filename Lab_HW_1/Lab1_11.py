from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_s = 0
        
        while l < r:
            s = (r - l) * min(height[l], height[r])
            max_s = max(max_s, s)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_s

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))