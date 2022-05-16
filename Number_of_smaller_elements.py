# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original 
# input array.
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0]

# Time complexity - O(N^2)
# Space complexity - O(N)

def smallerElements(array):
    newArray = []
    start = 0
    next = 1
    count = 0
    while start < len(array) - 1:
        if array[start] > array[next]:
            count += 1
        next += 1
        if next == len(array) - 1:
            if array[start] > array[next]:
                count += 1
                newArray.append(count)
                count = 0
                start += 1
                next = start
    newArray.append(0)
    return newArray

array = [3, 4, 9, 6, 1]
smallerElements(array)
