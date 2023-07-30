# Design Linked List

Design your implementation of the linked list. 

You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: `val` and `next`. 

`val` is the value of the current node, and `next` is a pointer/reference to the next node.

If you want to use the doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list. 

Assume all nodes in the linked list are 0-indexed.


Implement the `MyLinkedList` class:

- `MyLinkedList()` Initializes the `MyLinkedList` object.

- `int get(int index)` Get the value of the `indexth` node in the linked list. If the index is invalid, return `-1`.

- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.

- `void addAtIndex(int index, int val)` Add a node of value `val` before the `indexth` node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end of the linked list. If `index` is greater than the length, the node will not be inserted.

- `void deleteAtIndex(int index)` Delete the `indexth` node in the linked list, if the index is valid.

**Example 1**

```
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
```

```py
class MyLinkedList:

    def __init__(self):
        

    def get(self, index: int) -> int:
        

    def addAtHead(self, val: int) -> None:
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
```

<details>

  <summary>answer</summary>

```py
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self, val=None):
        if val is not None:
            self.head = Node(val)
            self.size = 1
        else:
            self.head = None
            self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        curr = self.head
        if curr is None:
            self.head = new
        else:
            new.next = curr
            self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        curr = self.head
        if curr is None:
            self.head = new
        else:
            for _ in range(self.size-1):
                curr = curr.next
            curr.next = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        curr = self.head
        new = Node(val)
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            for _ in range(index-1):
                curr = curr.next
            new.next = curr.next
            curr.next = new
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head

        # invalid index
        if index < 0 or index >= self.size or curr is None:
            return

        if index == 0:
            self.head = curr.next
            self.size -= 1
        elif index == self.size - 1:
            for _ in range(index-1):
                curr = curr.next
            curr.next = None
            self.size -= 1
        else:
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1
```


</details>
