We have an array

```py
nums = [1,3,5,7,9,0]
```

1. Insert an element `4` to the end of the array (TC : O(1))

```py
nums = [1, 3, 5, 7, 9, 4]
```

2. Insert an element `4` to the start of the array (TC : O(n))

```py
nums = [4, 1, 3, 5, 7, 9]
```

3. Insert an element `4` to index 2 (TC : O(n))

```py
nums = [1, 3, 4, 5, 7, 9]
```

Do not use built-in methods. This is for understanding of arrays.

<details>

  <summary>Answer</summary>

```py
# 1. Insert an element `4` to the end of the array (TC : O(1))
nums = [1,3,5,7,9,0]
nums[len(nums)-1] = 4

print(nums)

# 2. Insert an element `4` to the start of the array (TC : O(n))
nums = [1,3,5,7,9,0]

for i in range(len(nums)-2, -1, -1):
    nums[i+1] = nums[i]
nums[0] = 4

print(nums)

# 3. Insert an element `4` to index 2 (TC : O(n))
nums = [1,3,5,7,9,0]

for i in range(len(nums)-2, 1, -1):
    nums[i+1] = nums[i]
nums[2] = 4

print(nums)
```

</details>
