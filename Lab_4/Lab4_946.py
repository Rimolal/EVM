from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_i = 0
        
        for i in pushed:
            stack.append(i)
            while stack and pop_i < len(popped) and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1

        return len(stack) == 0

solution = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(solution.validateStackSequences(pushed, popped))