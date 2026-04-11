from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}
        for i in strs:
            sorted_w = tuple(sorted(i))
            if sorted_w not in anag:
                anag[sorted_w] = []
            anag[sorted_w].append(i)
        return list(anag.values())

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))