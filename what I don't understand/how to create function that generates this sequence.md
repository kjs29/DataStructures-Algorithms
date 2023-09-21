We have a sequence

```
2 5 11 17 23 31 41 47 ...
```

I have come up with a solution iteratively, but I would like to create a solution recursively.

<details>

  <summary>answer</summary>

```py
def is_prime(n):
    if n < 0:
        return None
    
    if 0 <= n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def sequence(n):
    if n < 1:
        return None
    res = []
    num = 2
    while len(res) < n*2:
        if is_prime(num):
            res.append(num)
        num += 1

    return res[-2]
        
for i in range(100):
    print(sequence(i))
```


</details>
