Create a `tower_of_hanoi` function using recursive algorithm.

```
| Tower1  |  Tower2  |  Tower3  |
|         |          |          |
| [disk1] |          |          |
| [disk2] |          |          |
| [disk3] |          |          |
```

We want to move disk1, disk2, disk3 to Tower3, so it looks like the following.

```
| Tower1  |  Tower2  |  Tower3  |
|         |          |          |
|         |          |  [disk1] |
|         |          |  [disk2] |
|         |          |  [disk3] |
```

Rules: 
    - only the top disk in each tower can move

    - only one disk can move at a time

```py
def tower_of_hanoi(number_of_disks, start_tower, target_tower, spare_tower):
    # write code
    pass

tower_of_hanoi(3,1,3,2)

# Desired output
# disk1 is moved from Tower1 to Tower3
# disk2 is moved from Tower1 to Tower2
# disk1 is moved from Tower3 to Tower2
# disk3 is moved from Tower1 to Tower3
# disk1 is moved from Tower2 to Tower1
# disk2 is moved from Tower2 to Tower3
# disk1 is moved from Tower1 to Tower3
```

<details>

  <summary>Answer</summary>

```py
def tower_of_hanoi(number_of_disks, start_tower, target_tower, spare_tower):
    if number_of_disks == 1:
        print(f"disk{number_of_disks} is moved from Tower{start_tower} to Tower{target_tower}")
    else:
        tower_of_hanoi(number_of_disks-1,start_tower,spare_tower, target_tower)
        print(f"disk{number_of_disks} is moved from Tower{start_tower} to Tower{target_tower}")
        tower_of_hanoi(number_of_disks-1,spare_tower,target_tower,start_tower)
```

</details>
