from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(x for x in s if x.isalnum()).lower()
        if len(cleaned) == 0:
            return True
        
        len_cleaned = len(cleaned)
        for i in range(len_cleaned // 2):
            if cleaned[i] != cleaned[len_cleaned - i - 1]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))