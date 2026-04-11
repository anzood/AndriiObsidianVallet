---
tags:
  - moc
up:
  - "[[Homepage]]"
lang: en
created: 2025-11-30
---
# Map of Content

## 📝 Content

Here is a root of the Knowledge database.
All the documents here have to go up to this document in the end.

## 📑 Topics
- [[Web development]] - here are collected the resources, related to the... web development, actually. 🙂
## 📥 [[Inbox]]

> [!NOTE] TODO
> Check and fix the query below

_New or unfiled notes related to this topic._

```dataview
LIST
FROM #note
WHERE contains(up, this.file.link)
AND !contains(file.outlinks, this.file.link)
```
