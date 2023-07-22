Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 

The relative order of the elements should be kept the same. 

Return the number of unique numbers in `nums`

```py
nums = [0,0,1,1,1,2,2,3,3,4]

removing_duplicates(nums)

print(nums)    #  [0,1,2,3,4,_,_,_,_,_]
```

source - [26. "Remove Duplicates from Sorted Array" leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

<details>

  <summary>Python answer O(n), O(1)
  
  </summary>

```py
def removing_duplicates(nums):
    index_to_be_replaced_to = 1

    for i in range(1, len(nums)):
        current = nums[i]
        previous = nums[i-1]

        if current != previous:
            nums[index_to_be_replaced_to] = nums[i]
            index_to_be_replaced_to += 1

    return index_to_be_replaced_to
```
</details>

<details>

  <summary>Python O(n), O(1)</summary>

```py
def removing_duplicates(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1
```

</details>

<details>

  <summary>Python answer O(n), O(n)</summary>

```py
def removing_duplicates(nums):
    duplicates = {}

    for i, num in enumerate(nums):
        if num in duplicates:
            nums[i] = float('int')
        else:
            duplicates[num] = i
    
    nums.sort()
```

</details>
