Create a class `BinarySearchTree` that has `add`, `traverse` methods.

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
root.traverse()

# Desired output
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

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(f"depth = {self.depth}, val = {self.val}")
        if self.right:
            self.right.traverse()
```

</details>
