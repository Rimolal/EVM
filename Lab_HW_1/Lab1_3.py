class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        re = set()
        l = 0
        max_l = 0
        
        for r in range(len(s)):
            while s[r] in re:
                re.remove(s[l])
                l += 1
            re.add(s[r])
            max_l = max(max_l, r - l + 1)
        
        return max_l

s = "dvdf"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))