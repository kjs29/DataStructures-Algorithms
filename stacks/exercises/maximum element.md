You have an empty sequence, and you will be given  queries. Each query is one of these three types:

```
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
```

Function Description

Complete the getMax function in the editor below.

getMax has the following parameters:
- string operations[n]: operations as strings

Returns
- int[]: the answers to each type 3 query

Input Format

The first line of input contains an integer, . The next  lines each contain an above mentioned query.

Constraints

```
1 <= n <= 10^5
1 <= x <= 10^9
1 <= type <= 3
All queries are valid.
```

Sample Input

```
STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
```

Sample Output

```
26
91
```

# Answer

```py
def getMax(operations):
    # Your code here
```

<details>

  <summary>My first try</summary>

```py
def getMax(operations):
    
    # 1. create stack to be added integer of numbers from the input, 
    # 2. create max_stack to be added for only current maximum numbers
    # 3. if the operation starts with 1, push the number to the stack
    # 4. if the operation starts with 2, remove the last number in the stack
    # 5. if the operation starts with 3, find the maximum value in the stack, and push the max number to the max_stack

    stack = []
    max_stack = []
    
    for op in operations:
        op = op.split()
        
        if op[0] == '1':
            stack.append(int(op[1]))
        elif op[0] == '2':
            stack.pop()
        elif op[0] == '3':
            max_number = max(stack)
            max_stack.append(max_number)
            
    return max_stack
```

  The problem of this code is that it exceeded its time limit.

  The reason is that `max(stack)`'s runtime is O(m), so the whole time complexity of this code is O(n*m).
</details>


<details>

  <summary>My second try</summary>

  Since my first try exceeded time limit, I have to focus on reducing the time complexity.

  One possible solution to reduce time complexity is to get rid of this line below.
  
  ```
  max_number = max(stack)
  ```

  `max(stack)` iterates through the whole stack of numbers, and find the max.

  Instead of putting maximum number when it shows '3',

  we can always put the maximum number on the top of the stack every time the input is '1 <number>'.

```py
# Time Complexity: O(n)
# Space Complexity: O(n)

def getMax(operations):
    # 1. create an empty array, stack
    # 2. create an empty array, max_stack
    # 3. iterate through each operations
    #     a. if the first part is 1
    #         i. if stack is empty, push the second part of the input(number) to stack
    #         ii. if stack is not empty, find the maximum value 
    #             between the second part of the input, and the last number in stack,
    #             and then push it to the stack
    #     b. if the first part is 2, remove the last number in stack
    #     c. if the first part is 3, append the last number in stack to the max_stack
    
    stack = []
    max_stack = []

    for op in operations:
        op = op.split()

        if op[0] == '1':
            if not stack:
                stack.append(int(op[1]))
            else:
                stack.append(max(stack[-1], int(op[1])))
        elif op[0] == '2':          
            stack.pop()
        else:
            max_stack.append(stack[-1])

    return max_stack
```

</details>
