from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = students
        stack = sandwiches
        count = [queue.count(0), queue.count(1)]
        while queue and stack:
            if queue[0] == stack[0]:
                count[stack[0]] -= 1
                queue.pop(0)
                stack.pop(0)
                
            else:
                if count[stack[0]] == 0:
                    break
                queue.append(queue.pop(0))
        return len(queue)
    
    
    
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
solution = Solution()
print(solution.countStudents(students, sandwiches))