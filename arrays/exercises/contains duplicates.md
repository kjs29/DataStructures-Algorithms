Given an integer array `nums`, return `true` if any value appears at least twice in the array, 

and return `false` if every element is distinct.

```py
def containsDuplicate(nums: list[int]) -> bool:

```

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        
    }
}
```

<details>

  <summary>python 06/28</summary>

```py
# time complexity: O(n)
# space complexity : O(n)

nums = [1,2,4,5,3]

def contains_duplicate( nums):
    hashmap = set()

    for el in nums:
        if el in hashmap:
            return True
        hashmap.add(el)
        
    return False
        
```

</details>

<details>

  <summary>Python 6/29
  
  TC: O(n)
  
  SC: O(n)
  
  </summary>

```py
# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    hashmap = {}

    for num in nums:
        hashmap[num] = hashmap.get(num,0) + 1
    
    for k in hashmap:
        if hashmap[k] > 1:
            return True
        
    return False
```

</details>


<details>

  <summary>
  
  Java 7/13
  
  TC: O(n)

  SC: O(n)
  
  </summary>

```java
class Solution {
    public static boolean containsDuplicate(int[] nums) {
        HashMap<String, Integer> numsFrequency = new HashMap<>();
        
        for (int num: nums) {
            if (numsFrequency.containsKey(Integer.toString(num))) {
                return true;
            } else {
                numsFrequency.put(Integer.toString(num), 1);
            }
        }
        return false;
    }
}
```

</details>
