# Binary serach will only work on a sorted list/array.
# Binary search iterative solution
# Time complexity - O(log(n)
# Space complexity - O(1)

def binarySearch(array, target):
    start = 0
    end = len(array) - 1 
    if target > array[end]:
        return False
    if target < array[start]:
        return False
    while start <= end:
        middleIndex = (start + end) // 2
        if target == array[middleIndex]:
            return middleIndex
        elif target < array[middleIndex]:
            end = middleIndex - 1 
        elif target > array[middleIndex]:
            start = middleIndex + 1
    return False
    
array = [10,50,52,64,92,101,103,110] 
target = 110
binarysearch(array, target)
