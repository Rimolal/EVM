class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 0:
            return x
        
        left, right = 1, x
        
        while left <= right:
            mid = (left + right) // 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
x = 4
solution = Solution()
print(solution.mySqrt(x))