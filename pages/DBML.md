---
tags:
  - type/note
created: 2026-02-04 13:22
up:
  - "[[Map of Content]]"
related:
  - 
lang: en
---
# DBML

DBML is incredibly intuitive because it reads like a simplified version of SQL. It maps 1:1 with Postgres types.

## 1. Table Basics

Code snippet

```dbml
Table users {
  id uuid [pk, default: `gen_random_uuid()`] // pk = primary key
  username varchar(255) [unique, not null]
  email varchar [unique]
  bio text [note: 'Bio is optional']
  created_at timestamp [default: `now()`]
}
```

## 2. Relationships (Foreign Keys)

There are two ways to define relationships. You can do it inline or at the end of the file.

**Inline (Short & Clean):**

Code snippet

```dbml
Table posts {
  id serial [pk]
  author_id uuid [ref: > users.id] // ">" means many-to-one
}
```

**At the end (Better for complex schemas):**

Code snippet

```
// <  one-to-many
// >  many-to-one
// <> many-to-many
// -  one-to-one

Ref: posts.author_id > users.id
Ref: profiles.user_id - users.id
```

## 3. Indexes & Constraints

You can define single or multi-column indexes.

Code snippet

```
Table products {
  id serial [pk]
  name varchar
  category_id int

  indexes {
    name [name: 'name_index']
    (category_id, name) [unique] // Multi-column unique index
  }
}
```

## 4. Enums

Perfect for status fields in Supabase.

Code snippet

```
Enum post_status {
  draft
  published
  archived
}

Table posts {
  id serial [pk]
  status post_status [default: 'draft']
}
```

---

## Summary of Symbols

| **Symbol** | **Meaning**      | **Example**                   |
| ---------- | ---------------- | ----------------------------- |
| `pk`       | Primary Key      | `id uuid [pk]`                |
| `>`        | Many-to-one      | `posts.user_id > users.id`    |
| `<`        | One-to-many      | `users.id < posts.user_id`    |
| `-`        | One-to-one       | `users.id - profiles.user_id` |
| `` ` ``    | Raw SQL/Defaults | ``default: `now()` ``         |

---

### Useful Resources:

- **Official Docs:** [dbml.org](https://www.google.com/search?q=https://dbml.org/docs/)
- **Visual Editor:** [dbdiagram.io](https://dbdiagram.io/) (You can write DBML on the left and see the ER Diagram on the right—highly recommended to avoid mistakes before sending to AI).