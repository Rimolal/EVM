from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(i)
            
            else:
                y = float(stack.pop())
                x = float(stack.pop())
                if i == '/':
                    stack.append(x // y)
                elif i == '*':
                    stack.append(x * y)
                elif i == '+':
                    stack.append(x + y)
                else:
                    stack.append(x - y)
        return int(stack[0])

solution = Solution()
tokens = ["2","1","+","3","*"]
print(solution.evalRPN(tokens))