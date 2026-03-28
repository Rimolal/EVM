from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(x for x in s if x.isalnum()).lower()
        if len(c) == 0:
            return True
        
        len_c = len(c)
        for i in range(len_c // 2):
            if c[i] != c[len_c - i - 1]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))