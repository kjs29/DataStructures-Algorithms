Leetcode 534

I solved it using the answer, but I still don't understand how it works fully.

My answer is 

```py
class Solution:
    def __init__(self):
        self.curr_diameter = 0
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.curr_diameter = max(self.curr_diameter, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.curr_diameter
```
