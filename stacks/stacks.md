Stack is a data structure that implements Last-In, First-Out (LIFO).

Arrays that we know follow this rule.

Let's consider the following code.

```py
lst = []

lst.append(1)       #[1]
lst.append(2)       #[1,2]
lst.append(3)       #[1,2,3]
lst.pop()           #[1,2]
lst.pop()           #[1]
lst.append(9)       #[1,9]
lst.pop()           #[1]
```


At first `lst` was empty,

and then 1 was added, 2 was added which goes on top of 1, then 3 was added that is on top of the 2.

When we used `pop()`, the last one who joined the array has to get out.


