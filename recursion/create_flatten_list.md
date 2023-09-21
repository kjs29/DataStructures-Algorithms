Create a `flatten` that flattens a nested list taken as a parameter, using **recursive algorithm**.

The element should still be contained in the list.

For example,

```py
arr = [1,[2],[3,[4]],5]

print(flatten(arr))     # [1, 2, 3, 4, 5]
```

<details>

  <summary>answer</summary>

```py
def flatten(arr):

    res = []
    for each in arr:
        if isinstance(each, list):
            res += flatten(each)
        else:
            res.append(each)
    return res
```

</details>
