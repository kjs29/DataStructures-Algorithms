# Definition of array

An array is an ordered and contiguous collection of homogenous data.

Dynamically-typed languages such as JavaScript and Python, achieve mixed array types, because each data type and value are interpreted at runtime.

# Array indexing

Array indexing takes O(1) regardless of the size of an array.

Test

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

console.log("Accessing 3rd element in cars takes "+(endCars-startCars)+"ms");
console.log("Accessing 500000th element in cars takes "+(endOneToMillion-startOneToMillion)+"ms");
```

Result

```
Accessing 3rd element in cars takes 0ms
Accessing 500000th element in cars takes 0ms
```

# Dynamic arrays

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

Conclusion: 

`push()` takes O(1) operations.

`unshift()` takes O(n) operations.[^1]

[^1]: `shift()` takes O(n) as well.
