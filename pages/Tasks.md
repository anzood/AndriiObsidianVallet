## Tasks
- [ ] Task from tasks #sphere/health 
- [ ] Task work from tasks #family


## Spheres tasks
```dataview
TASK
WHERE !completed GROUP BY file.link
```
## Completed tasks
```dataview
TASK
WHERE completed GROUP BY file.link
```