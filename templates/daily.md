---
tags:
  - journal
---
# Journal <% tp.file.title %>

## Tasks
```dataview
TASK
WHERE !completed
AND (
    (due != null AND due <= date(<% tp.file.title %>)) OR
    (scheduled != null AND scheduled <= date(<% tp.file.title %>)) OR
    (start != null AND start <= date(<% tp.file.title %>))
)
FLATTEN choice(length(tags) = 0, list("No Tag"), tags) AS T
GROUP BY T
SORT default(due, default(scheduled, start)) ASC
```
## 📝 Notes
<% tp.file.cursor() %>

## 🍲 Menu

## 🔄 Progress on Goals
*Brief reflection on goal progress*

## 💭 Daily Reflection
*What went well? What could be improved?*

---