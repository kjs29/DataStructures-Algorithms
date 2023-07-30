Given a 6 x 6 2D Array, `arr` :

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

```
a b c
  d
e f g
```

There are 16 hourglasses in `arr`. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be 6 x 6.

Example

```
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
```
The 16 hourglass sums are:

```
-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
```

The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

```
0 4 3
  1
8 6 6
```

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

- int arr[6][6]: an array of integers

Returns

- int: the maximum hourglass sum

# Code

```py
def hourglassSum(arr):

```

<details>

  <summary>python
  
  Time Complexity: O(1)
  Space Complexity: O(1)
  </summary>

```py
def hourglassSum(arr):
    max_number = float('-inf')

    for row in range(4):
        for col in range(4):
            top = arr[row][col] + arr[row][col+1] + arr[row][col+2]
            middle = arr[row+1][col+1]
            bottom = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            sum = top + middle + bottom

            if sum > max_number:
                max_number = sum
    return max_number
```

</details>
