Create a mergeSort algorithm.

```py
arr = [1,3,5,2,9,0,8,6,4,7]
print(mergeSort(arr))       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<details>

  <summary>Answer - recursively</summary>

```py
def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    
    i=j=0
    merged = []

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    if i < len(left):
        merged += left[i:]
    
    if j < len(right):
        merged += right[j:]
    
    return merged
```

</details>
