Create a class `BinarySearchTree` that has `add`, `traverse`,`find` methods.

`traverse` should be depth-first search in-order traversal.

```py
class BinarySearchTree:
    # write code here
    pass

root = BinarySearchTree(5)
root.add(3)
root.add(7)
root.add(1)
root.add(2)
root.find(3)
root.find(4)
root.find(5)
root.traverse()

# 3 exists at depth 2
# 4 does not exist
# 5 exists at depth 1
# depth = 3, val = 1
# depth = 4, val = 2
# depth = 2, val = 3
# depth = 1, val = 5
# depth = 2, val = 7
```

<details>

  <summary>Answer</summary>

```py
class BinarySearchTree:
    def __init__(self, val, depth=1):
        self.val = val
        self.depth = depth
        self.left = None
        self.right = None

    def add(self, val):
        if val < self.val:
            if not self.left:
                self.left = BinarySearchTree(val, self.depth+1)
            else:
                self.left.add(val)
        else:
            if not self.right:
                self.right = BinarySearchTree(val, self.depth+1)
            else:
                self.right.add(val)
    
    def find(self, val):
        if val == self.val:
            print(f"{val} exists at depth {self.depth}")
        elif val < self.val:
            if self.left:
                self.left.find(val)
            else:
                print(f"{val} does not exist")
        elif val > self.val:
            if self.right:
                self.right.find(val)
            else:
                print(f"{val} does not exist")
            
    def traverse(self):
        if self.left:
            self.left.traverse()
        print(f"depth = {self.depth}, val = {self.val}")
        if self.right:
            self.right.traverse()
```

</details>
