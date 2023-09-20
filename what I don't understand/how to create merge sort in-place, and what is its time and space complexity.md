how to create merge sort in-place, and what is its time and space complexity?

Original mergesort's time complexity is O(nlogn),

```py
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]          
    right = nums[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    
    # If I don't use 'merged', and use in-place merge sort, would it affect complexity?
    merged = [0] * (len(left) + len(right))
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
        k += 1
    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1
        
    return merged
```
