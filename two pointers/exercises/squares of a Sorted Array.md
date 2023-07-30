Given an integer array `nums` sorted in **non-decreasing** order, 

return an array of **the squares of each number** sorted in non-decreasing order.

Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

```java
class Solution {
    public int[] sortedSquares(int[] nums) {
        
    }
}
```

<details>

  <summary>Java
  
  tc: O(nlogn)
  sc: O(n)


```java
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] answer = new int[nums.length];
        
        for (int i=0;i<nums.length;i++) {
            answer[i] = nums[i]*nums[i];
        }
        Arrays.sort(answer);
        return answer;
    }
}
```
  
  </summary>

</details>
