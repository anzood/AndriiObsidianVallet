## Tasks
```dataview
TASK
WHERE !completed GROUP BY file.link
```
## Completed tasks
```dataview
TASK
WHERE completed GROUP BY file.link
```

## Test
```dataview
TASK
WHERE !completed
FLATTEN choice(length(tags) = 0, list("No Tag"), tags) AS T
GROUP BY T
SORT due ASC
```