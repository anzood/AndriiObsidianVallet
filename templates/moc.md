---
tags:
  - moc
created: <% tp.file.creation_date() %>
---

# <% tp.file.title %>

## 🗺️ Context

_Brief description of what this map covers._

## 🗂️ Key Topics

- [[Topic 1]]
- [[Topic 2]]

## 📥 Inbox

_New or unfiled notes related to this topic._

```dataview
LIST
FROM #note
WHERE contains(up, this.file.link)
AND !contains(file.outlinks, this.file.link)
```
