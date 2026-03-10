class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = sorted(s)
        arr_t = sorted(t)
        if len(arr_s) != len(arr_t):
            return False
        for i in range(len(arr_s)):
            if (arr_s[i] != arr_t[i]):
                return False
        return True

s = "rat"
t = "car"
solution = Solution()
print(solution.isAnagram(s, t))