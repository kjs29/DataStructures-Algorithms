Given two integer arrays `nums1` and `nums2`, return an array of their intersection. 

Each element in the result must be unique and you may return the result in any order.

example1

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

example2

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```

<details>

  <summary>answer O(n+m) O(n+m)</summary>

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        answer = set()

        for i in range(len(nums2)):
            if nums2[i] in set1:
                answer.add(nums2[i])
        return list(answer)
```

</details>

<details>

  <summary>answer O(nlongn+mlogm)  O(k)</summary>

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        answer = set()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                answer.add(nums1[i])
                i += 1
                j += 1

        return list(answer)
```

</details>
