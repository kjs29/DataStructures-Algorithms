This is the code for reversing a linked list using recursion.

Why `head.next.next`?

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)
        
        # Adjust pointers: make the next node point back to the current head
        head.next.next = head
        head.next = None  # avoid cycle in linked list
        
        return new_head
```
