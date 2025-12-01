# 🏷️ The Hybrid Tag System

## 1\. The Golden Rule

  * **Use Nested Tags (`#root/child`)** for the **Container**.
      * *Describes: What kind of file is this? Where does it live in my system?*
  * **Use Atomic Tags (`#tag`)** for the **Content**.
      * *Describes: What is this actually about?*

-----

## 2\. System Tags (Nested)

*These provide the structural "skeleton" of your vault.*

### 🟢 Life Spheres (`#sphere/...`)

*Assign exactly one of these to every Project, Goal, or Area.*

  * `#sphere/health`
  * `#sphere/family`
  * `#sphere/career`
  * `#sphere/wealth`
  * `#sphere/social`
  * `#sphere/growth`
  * `#sphere/play`
  * `#sphere/admin`

### 🔵 File Types (`#type/...`)

*Defines the format or template of the note.*

  * `#type/project` (An active outcome with a deadline)
  * `#type/area` (An ongoing responsibility, e.g., Car Maintenance)
  * `#type/resource` (General resource, if it doesn't fit any other type)
  * `#type/note` (Note)
  * `#type/book` (Book)
  * `#type/course` (Course)
  * `#type/video` (Video)
  * `#type/article` (Article)
  * `#type/podcast` (Podcast)
  * `#type/post` (Post)
  * `#type/meeting` (Meeting notes)
  * `#type/person` (CRM profile)
  * `#type/journal` (Daily/Weekly notes)

### 🟠 Status (`#status/...`)

*Tracks the lifecycle of a Project or Task.*

  * `#status/idea` (Someday/Maybe)
  * `#status/todo` (Planned but not started)
  * `#status/wip` (Work In Progress)
  * `#status/waiting` (Blocked by someone else)
  * `#status/done` (Completed/Archived)

-----

## 3\. Topic Tags (Atomic)

*These describe the subject matter. No nesting. Use kebab-case.*

  * `#python`
  * `#investing`
  * `#psychology`
  * `#recipes`
  * `#obsidian`
  * `#marketing`

-----

## ⚡ Examples in Action

**Scenario 1: You are taking a Python Course.**

> Tags: `#sphere/growth` `#type/course` `#status/wip` `#python`

**Scenario 2: You are planning a Vacation to Italy.**

> Tags: `#sphere/play` `#type/project` `#status/todo` `#travel` `#italy`

**Scenario 3: A meeting note with your Boss.**

> Tags: `#sphere/career` `#type/meeting` `#management`

-----

## 📊 Why do it this way? (The Dataview Payoff)

By nesting your system tags, you can create powerful dashboards effortlessly.

**Example: Show me all active learning resources:**

```dataview
TABLE without id file.link as "Resource", status as "Status"
FROM #type/resource
WHERE contains(file.tags, "#status/wip")
```

**Example: Show me everything related to Python (regardless of type):**

```dataview
LIST
FROM #python
```

## Idea to  concider
### The "Resonance" Dimension (Quality)

_The filter for "Signal vs. Noise"._

When you revisit your vault in 2 years, Status tells you if you finished reading the book. `Resonance` tells you if the book changed your life.

- **Why use it:** To instantly surface your "Gold Standard" material.
- **The Tags:**
  - `#resonance/gold` (Top 1% - The foundational concepts you live by)
  - `#resonance/high` (Great, worth re-reading)
  - `#resonance/low` (Reference only, dry facts)

- **Alternative (Frontmatter):** Instead of tags, many users use a key in the YAML frontmatter: rating: ⭐⭐⭐⭐⭐

**Example:**

You search for `tag:#topic/investing AND tag:#resonance/gold`. Result: You get the 3 core principles that actually make you money, filtering out the 50 news articles you clipped.