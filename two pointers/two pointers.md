
# What is a two pointer

Two pointer is a technique that is used in data structure and algorithm problems, especially in arrays and linked lists traversing problems.

Two pointers set different accessing element, traversing the array by making them move towards each other or moving at different speed.

Two pointers take advantage of the fact that it costs O(1) runtime to access element.

```py
random_numbers = [32,54,3,9,77]

# random_numbers[0] = 32
# random_numbers[1] = 54
# random_numbers[2] = 3
# random_numbers[3] = 9
# random_numbers[4] = 77

# We can see that we can access to any element in the array, random_numbers, 
# so it can be very useful if we could use these elements to derive the answer
```

# Question

There is a famous question called [two sum](https://github.com/kjs29/DataStructures-Algorithms/blob/master/hashing/exercises/1.%20two%20sum.md)


We can solve it by having two pointers.(ONLY if the array is sorted)

```py
def twoSum(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end :
        print(f"start: {start}, end : {end}")
        sum =  arr[start] + arr[end]
        if sum < target :
            print(f"{arr[start]} (arr[start]) + {arr[end]} (arr[end]) = {sum} < target {target}")
            print(f"sum is too small, so we will move start's position to the right by 1, so that sum(arr[start]+arr[end]) gets bigger")
            start += 1
            print('start += 1')
        elif sum == target:
            break
        elif sum > target:
            print(f"{arr[start]} (arr[start]) + {arr[end]} (arr[end]) = {sum} > target {target}")
            print(f"sum is too big, so we will move end's position by 1 to the left, so that sum(arr[start]+arr[end]) gets smaller")
            end -= 1
            print('end -= 1')
        
        print(f"start: {start}, end : {end}\n=====================")

print(twoSum([1,3,5,6],8))
```

Result:

```
start: 0, end : 3
1 (arr[start]) + 6 (arr[end]) = 7 < target 8
sum is too small, so we will move start's position to the right by 1, so that sum(arr[start]+arr[end]) gets bigger
start += 1
start: 1, end : 3
=====================
start: 1, end : 3
3 (arr[start]) + 6 (arr[end]) = 9 > target 8
sum is too big, so we will move end's position by 1 to the left, so that sum(arr[start]+arr[end]) gets smaller
end -= 1
start: 1, end : 2
=====================
start: 1, end : 2
None
```

# Another question

We can reverse a string with two pointer technique.

```py
hello = list('hello')   # ['h', 'e', 'l', 'l', 'o']

def reverseString(s: list[str]) -> str:
    start = 0
    end = len(s) - 1

    while start < end:
        [s[start], s[end]] = [s[end], s[start]]
        start += 1
        end -= 1
    
    return ''.join(s)

print(reverseString(hello))     # olleh
```

In this question example, both `start` and `end` move inward at the same speed.
