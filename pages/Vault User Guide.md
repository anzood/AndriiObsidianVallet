---
tags:
  - type/article
  - pkm
lang: en
---
# Vault User Guide

Welcome to your **Hybrid Zettelkasten/MOC System**. This vault is designed for action, clarity, and connection.

## 1. The Core Philosophy

- **Spheres over Folders:** Everything belongs to a Life Sphere (e.g., `#sphere/health`, `#sphere/career`).
- **Links over Hierarchy:** Notes live in `pages/` and are connected via links (`[[Link]]`) and MOCs (Maps of Content).
- **Action-Oriented:** Every note should have a purpose (Resource, Project, or Area).

## 2. The Workflow (The Loop)

### 📥 Step 1: Capture (Daily Note)

- Use `Opt-D -> Open today's daily note`.
- **Tags:** Automatically tagged `#type/journal` and `#status/raw`.
- **Content:** Dump tasks, quick thoughts, and links here.
- **Dashboard:** Your Homepage shows all "Daily notes to process" (notes with `#status/raw`).

### ⚙️ Step 2: Process (Refine)

- Review your Daily Notes regularly (e.g., end of day or week).
- **Extract:** Turn bullet points into real notes (Atomic Notes) in `pages/`.
- **Cleanup:** Once a Daily Note is processed (empty of value), **remove the `#status/raw` tag**. This removes it from your Homepage dashboard.

### 🔗 Step 3: Connect (Context)

- **Link Up:** In your new note, set the `up:` property to a relevant MOC (e.g., `[[Health]]`).
- **Tag It:** Apply the correct Sphere and Type tags.

## 3. The Tagging System

We use a **Hybrid System**:

1.  **Container Tags (Nested):** Define _what_ the file is.
    - `#sphere/growth` (Where does it belong?)
    - `#type/resource` (What format is it?)
    - `#status/wip` (What is its state?)
2.  **Content Tags (Atomic):** Define _what it's about_.
    - `#python`, `#investing`, `#recipes` (No nesting, just the topic).

## 4. Language Policy

- **Default:** English (`lang: en`).
- **Rule:** Use English for technical notes and general knowledge. Keep source language (Russian/Ukrainian) for specific resources (e.g., recipes, local documents) if preferred.
- **Property:** If a note is not in English, explicitly set `lang: ru` or `lang: ua` in the frontmatter.

## 5. Key Structures

### 🏠 Homepage

- **Spheres:** Quick access to your 8 main areas.
- **Active Projects:** Lists anything with `#type/project` and `#status/wip`.
- **Recent Thoughts:** Your latest edited notes.

### 🗺️ Maps of Content (MOCs)

- **Root:** `[[Map of Content]]` is the entry point.
- **Sphere MOCs:** Each Sphere (e.g., `[[Wealth]]`) is a high-level MOC.
- **Inbox:** Every MOC has an automated "Inbox" section showing notes linked to it via the `up` property.

## 6. Task Management

- **Daily Tasks:** Live in your Daily Note.
- **Project Tasks:** Live in the specific Project note.
- **Global View:** `[[Tasks]]` aggregates everything.
