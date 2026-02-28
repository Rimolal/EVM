def unique(arr):
    uni = set()
    for i in range(0,4):
        if arr[i] in uni:
            return True
        uni.add(arr[i])
    return False


arr = [1, 2, 3, 4]
print(unique(arr))