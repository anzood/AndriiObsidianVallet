---
tags:
  - type/journal
---

# Journal <% tp.file.title %>

## Tasks

```dataviewjs
const dateStr = "<% tp.file.title %>";
const targetDate = dv.date(dateStr);

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

## 📝 Notes

<% tp.file.cursor() %>

## 🍲 Menu

## 🔄 Progress on Goals

_Brief reflection on goal progress_

## 💭 Daily Reflection

_What went well? What could be improved?_

---
