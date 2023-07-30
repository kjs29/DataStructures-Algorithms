
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

example 1.

```
Input: s = "anagram", t = "nagaram"
Output: true
```

example 2.

```
Input: s = "rat", t = "car"
Output: false
```

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
```

<details>

  <summary>python 06/28</summary>

```py
# Time Complexity: O(A+B), when A, B represent length of s, and t respectively
# Space Complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        
        for letter in t:
            if letter in hashmap:
                hashmap[letter] -= 1
            else:
                return False
        
        for k in hashmap:
            if hashmap[k] > 0:
                return False
        
        return True
```
</details>


<details>

  <summary>python 06/28 (2)</summary>

```py
# Time Complexity: O(nlogn), because sorted() in python uses Timsort, which has time complexity of O(nlogn)
# Space Complexity: O(n), whichever n is longer between s length, t length
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
</details>
