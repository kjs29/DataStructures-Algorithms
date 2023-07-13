Query the total population of all cities in CITY where District is California.

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
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';
```

</details>
