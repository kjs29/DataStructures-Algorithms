Create a function that takes a string reversed string, using recursive algorithm.

For example,

```py
print(reverseString("abc"))     # "cba"
```

<details>

  <summary>Answer</summary>

```py
def reverseString(string):
    if len(string) <= 1:
        return string
    return reverseString(string[-1]) + reverseString(string[:-1])
```

</details>
