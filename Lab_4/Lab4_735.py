from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        aster = []
        
        
        for i in asteroids:
            
            destroy = True
            while aster and aster[-1] > 0 and i < 0:
                if aster[-1] < abs(i):
                    aster.pop()
                elif aster[-1] == abs(i):
                    aster.pop()
                    destroy = False
                    break
                else:
                    destroy = False
                    break
            if destroy:
                aster.append(i)
        return aster
        
solution = Solution()
asteroids = [3,5,-6,2,-1,4]
print(solution.asteroidCollision(asteroids))