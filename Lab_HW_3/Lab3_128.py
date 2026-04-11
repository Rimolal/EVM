from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lens = {}
        max_len = 0
        nums = set(nums)
    
        for num in nums:
            l = lens.get(num - 1, 0)
            r = lens.get(num + 1, 0)
            cur_len = l + r + 1
            lens[num] = cur_len
            lens[num - l] = cur_len
            lens[num + r] = cur_len
            max_len = max(max_len, cur_len)
        return max_len


solution = Solution()
nums = [100,4,200,1,3,2]
print(solution.longestConsecutive(nums))