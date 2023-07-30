We have an array

```py
nums = [1,3,5,7,9,0,0]
```

1. Insert elements `100 101` to the end of the array (TC : O(1))

```py
nums = [1,3,5,7,9,100,101]
```

2. Insert elements `100 101` to the start of the array (TC : O(n))

```py
nums = [100,101,1,3,5,7,9]
```

3. Insert elements `100 101` to index 2 (TC : O(n))

```py
nums = [1,3,100,101,5,7,9]
```

Do not use built-in methods. This is for understanding of arrays.

<details>

  <summary>Answer</summary>

```py
# 1. Insert elements `100 101` to the end of the array (TC : O(1))
nums = [1,3,5,7,9,0,0]
nums[len(nums)-1] = 101
nums[len(nums)-2] = 100

print(nums)

# 2. Insert elements `100 101` to the start of the array (TC : O(n))
nums = [1,3,5,7,9,0,0]

for i in range(len(nums)-3, -1, -1):
    nums[i+2] = nums[i]
nums[0] = 100
nums[1] = 101

print(nums)

# 3. Insert elements `100 101` to index 2 (TC : O(n))
nums = [1,3,5,7,9,0,0]

for i in range(len(nums)-3, 1, -1):
    print(i)    
    nums[i+2] = nums[i]
nums[2] = 100
nums[3] = 101

print(nums)

```

</details>
