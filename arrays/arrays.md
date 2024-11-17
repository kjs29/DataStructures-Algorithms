# Definition of Array

An array is an ordered and contiguous collection of homogenous data.

Dynamically-typed languages such as JavaScript and Python, achieve mixed array types, because each data type and value are interpreted at runtime.

Python lists include Arrays, and ArrayLists. However it is important to understand how arrays and arraylists work behind the scenes. This will help us write codes related to arrays more efficiently.

# Array has fixed size.

Python lists include both arrays and arraylists, so it is better to use Java example to demonstrate.

<em>Arrays.java</em>

```java
int[] array = new int[5];       // creating an array that has 5 elements , [0, 0, 0, 0, 0]
```

This `array` won't change its size.

# ArrayList has dynamic size.

<em>ArrayList.java</em>

```java
ArrayList<Integer> arrayList = new ArrayList<>();
```

We just created `arrayList` that consists of integer.

# Why do we use ArrayList?

Before we get to ArrayList, we have to think about why we need to use ArrayList.

The reason why we use ArrayList is that ArrayList allows us to manipulate data,

including inserting, removing, and deleting.

### Autoboxing 

Notice that it is not `int`, but `Integer`. `int` is a primitive data type, but `Integer` is a wrapper class that acts like integers. So `Integer` is an object.

When `Integer` type automatically converts to `int`, or vice versa, which is called `autoboxing`.


```java
ArrayList<Integer> arrayList = new ArrayList<>();

arrayList.add(5);       // autoboxing, 2(int) converts to Integer type.
```

# Accessing an element


Array indexing takes O(1) regardless of the size of an array.

Let's test it.

<i>Javascript example</i>
```js
let cars = ["tesla","bmw","kia","ford"];
let oneToMillion = [];
for (let i=0;i<1000000;i++){
    oneToMillion.push(i);
}

let startCars = Date.now();
cars[2];
let endCars = Date.now();

let startOneToMillion = Date.now();
oneToMillion[499999];
let endOneToMillion = Date.now();

console.log("Accessing 3rd element takes "+(endCars-startCars)+"ms");
console.log("Accessing 500000th element takes "+(endOneToMillion-startOneToMillion)+"ms");
```

Result:

```
Accessing 3rd element takes 0ms
Accessing 500000th element takes 0ms
```

# Dynamic arrays in JavaScript - Comparison time complexity between push() and unshift()

`Array.push()` takes O(1)

`Array.shift()` and `Array.unshift()` takes O(n)

Testing `push()` vs `unshift()`

```js
nArr = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000];

for (n of nArr) {
    let startPush = Date.now();
    pushFunc(n);
    let endPush = Date.now();
    
    let startUnshift = Date.now();
    unshiftFunc(n);
    let endUnshift = Date.now();
    
    console.log("Push when n is "+n+" takes "+(endPush-startPush)+"ms");
    console.log("Unshift when n is "+n+" takes "+(endUnshift-startUnshift)+"ms");
    console.log('--------')
}

function pushFunc(n) {
    const arr = [];
    for (let i=0;i<n;i++){
        arr.push(i+1);
    }
    return arr;
}

function unshiftFunc(n) {
    const arr = [];
    for (let i=0;i<n;i++) {
        arr.unshift(i-1);
    }
    return arr;
}
```

Result

```
Push when n is 10000 takes 0ms
Unshift when n is 10000 takes 9ms
--------
Push when n is 20000 takes 2ms
Unshift when n is 20000 takes 38ms
--------
Push when n is 30000 takes 1ms
Unshift when n is 30000 takes 84ms
--------
Push when n is 40000 takes 1ms
Unshift when n is 40000 takes 167ms
--------
Push when n is 50000 takes 1ms
Unshift when n is 50000 takes 279ms
--------
Push when n is 60000 takes 2ms
Unshift when n is 60000 takes 436ms
--------
Push when n is 70000 takes 1ms
Unshift when n is 70000 takes 623ms
--------
Push when n is 80000 takes 2ms
Unshift when n is 80000 takes 846ms
--------
Push when n is 90000 takes 3ms
Unshift when n is 90000 takes 1092ms
--------
Push when n is 100000 takes 2ms
Unshift when n is 100000 takes 1356ms
```

We can see that as n increases, `push()`'s runtime does not increase so much, but `unshift()`'s runtime will increase a lot.

`.push()` Time Complexity: O(1)

`.unshift()` Time Complexity: O(n)

# Inserting an element in Python

<em>list.py</em>

```py
lst = [1,3,5]

lst.insert(1, 2)        # insert 2 at index 1

print(lst)      # [1,2,3,5]
```

# Deleting an element in Python

- Removing an element by index

    - Removing the last element

        ```py
        a = ['a','b','c','d','e']

        a.pop(2)        # removing an element at 2nd index

        print(a)        # ['a','b','d','e']
        ```

        `pop()` Time complexity: O(1)
    
    - Removing element that is not the last element


        ```py
        b = [2,4,6,8,10]

        b.pop(3)        # removing an element at index position 3

        print(b)        # [2,4,6,10]
        ```

        `pop(3)` Time complexity: O(n)

- Removing an element by value

```py
b = [1,3,5,7,3]

b.remove(3)     # removing the first element that is 3

print(b)        # [1,5,7,9]
```

`remove()` Time complexity: O(n)

# Conclusion

# Array

- Accessing an element: O(1) - Good!

- Searching for an element:

    - Linear Search: O(n)

- Inserting an element:

    - Inserting at the end: O(1)

    - anywhere else: O(n)

- Deleting an element: 

    - Deleting at the end: O(1)

    - anywhere else: O(n)