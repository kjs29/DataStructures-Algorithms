Query the difference between the maximum and minimum populations in CITY.

CITY

|FIELD|TYPE|
|---|---|
|ID|NUMBER|
|NAME|VARCHAR(20)|
|COUNTRYSIDE|VARCHAR(3)|
|DISTRICT|VARCHAR(20)|
|POPULATION|NUMBER|


<details>

  <summary>MySQL</summary>

```sql
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;
```

</details>
