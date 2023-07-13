Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

The STATION table is described as follows:

STATION

|FIELD|TYPE|
|---|---|
|ID|NUMBER|
|CITY|VARCHAR(2)|
|STATE|VARCHAR(20)|
|LAT_N|NUMBER|
|LONG_W|NUMBER|

<details>

  <summary>MySQL</summary>

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTR(CITY, 1, 1) IN ('a','e','i','o','u');      -- SUBSTR(STRING, START, LENGTH), 1 INDEXING
```

</details>
