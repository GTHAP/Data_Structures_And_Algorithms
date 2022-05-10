# Time - O(n(log(n)))
# Space - O(n)

def mergesort(array):
    if len(array) == 1:
        return array
    middleidx = len(array) // 2
    lefthalf = array[:middleidx]
    righthalf = array[middleidx:]
    return mergesortedarrays(mergesort(lefthalf), mergesort(righthalf))

def mergesortedarrays(lefthalf, righthalf):
    sortedarray = [None] * (len(lefthalf) + len(righthalf))
    k = i = j = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[j]:
            sortedarray[k] = lefthalf[i]
            i += 1 
            k += 1 
        else:
            sortedarray[k] = righthalf[j]
            j += 1 
            k += 1 
    while i < len(lefthalf):
        sortedarray[k] = lefthalf[i]
        i += 1 
        k += 1 
    while j < len(righthalf):
        sortedarray[k] = righthalf[j]
        j += 1 
        k += 1 
    return sortedarray
    
array = [4,2,3,1,5,9,8,7]
print(mergesort(array))
