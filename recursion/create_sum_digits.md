Create a function that adds each digit, using recursive algorithm.

if n is negative number, print "n should be a positive number".

```py
sum_digit(12)   #3
sum_digit(1)    #1
sum_digit(123)  #6
```


<details>

  <summary>answer</summary>

```py
def sum_digit(n):
    if n < 0:
        print("n should be positive number")
        return
    if n < 10:
        return n
    last = n % 10
    return last + sum_digit(n//10)
```

</details>
