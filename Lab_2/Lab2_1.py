def sortedSquares(nums):
    
    mid = len(nums)//2
    new_nums = [nums[mid]**2]
    for i in range(1, mid + 1):
        x = nums[mid + i]**2
        y = nums[mid - i]**2
        new_nums.append(min(x, y))
        new_nums.append(max(x, y))
    return new_nums

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))