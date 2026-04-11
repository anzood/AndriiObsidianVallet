# Tasks
## Current tasks by page
```dataview
TASK
WHERE !completed 
AND (start <= date(today) OR due <= date(today) OR scheduled <= date(today))
GROUP BY file.link
```

## Current tasks by tag
```dataviewjs
const targetDate = dv.date("today");

// Fetch tasks once
const tasks = dv.pages().file.tasks.where(t =>
    !t.completed && (
        (t.due && t.due <= targetDate) ||
        (t.scheduled && t.scheduled <= targetDate) ||
        (t.start && t.start <= targetDate)
    )
);

if (tasks.length === 0) {
    dv.paragraph("No tasks for today! 🎉");
} else {
    // Group by tags
    for (let group of tasks.groupBy(t => t.tags.length > 0 ? t.tags[0] : "No Tag")) {
        dv.header(3, group.key);
        dv.taskList(group.rows, false);
    }
}
```
## Recently completed tasks
```dataview
TASK
WHERE completed 
AND !contains(text, "🔒 archived")
AND (!parent OR parent.completed)
GROUP BY file.link
```

## All tasks
```dataview
TASK
WHERE !completed GROUP BY file.link
```