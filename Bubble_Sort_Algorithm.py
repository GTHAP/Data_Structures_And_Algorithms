# Time complexity - O(N^2)
# Space complexity - O(1)

unsortedArray = [1,2,10,-1,-3,4,1]

def bubbleSort(unsortedArray):
    for i in range(len(unsortedArray)):
        for j in range(len(unsortedArray) - i - 1):
            if unsortedArray[j] > unsortedArray[j + 1]:
                unsortedArray[j], unsortedArray[j + 1] = unsortedArray[j + 1], unsortedArray[j]
    return unsortedArray
    
bubbleSort(unsortedArray)
