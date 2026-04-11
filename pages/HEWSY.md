---
tags:
  - type/project
  - sphere/wealth
  - status/wip
created: 2025-12-02 15:17
up:
  - "[[Projects]]"
related:
  - "[[HEWSY Roadmap]]"
  - "[[HEWSY UI]]"
  - "[[HEWSY Architecture]]"
lang: en
---

# 🥗 HEWSY: Project Tracker

**"Healthy Eating Without Stress... made easY."**

## 📋 Overview

**Goal**: Build a smart nutrition architect web app (PWA) that automatically constructs balanced eating plans based on biological goals using a "Slot" system.

- **Tech Stack**: SvelteKit, Supabase, Prisma, Tailwind CSS.
- **Current Phase**: Phase 1 - The Engine (MVP Core).

## 🧑‍🧑‍🧒 Target Audience: "The Efficient Health-Seeker"

**Profile**: Men driven by **Aesthetics & Health** (looking good, feeling energetic) who view food as fuel but lack the time or desire to become a chef.

- **The Vibe**: Minimalist. They want a "Deploy Food" button, not a kitchen adventure.
- **Pain Points with Current Solutions**:
  - _Vs. Trackers (MyFitnessPal)_: Too reactive. "Don't tell me I missed my protein _after_ dinner; tell me what to eat _for_ dinner."
  - _Vs. Recipe Apps_: Too complex. Too many obscure ingredients, too much shopping friction, and the classic "Raw vs Cooked" math confusion.
- **The Promise**: "Effortless weight control (loss, gain, or maintenance). Balanced nutrition without the cognitive load."
  - No complex shopping lists for one-off meals.
  - Clear distinction between _Ingredients_ (Raw Rice) and _Dishes_ (Cooked Rice).

## 🎨 Design & Brand Identity

**Style**: Minimalist, Clean, Mobile-first.

- **Visual Language**:
  - Focus on whitespace and typography.
  - "Medical but warm" or "Scientific but friendly".
  - _Action_: Create a moodboard (Pinterest/Dribbble).
- **UX Priorities**:
  - **Mobile-first**: The planner must work seamlessly on a phone in the grocery store.
  - **Speed**: Quick logging and slot swapping.

## 📣 Marketing & Growth

**Strategy**: "Stealth Education" -> Product Reveal.

- **Concept**: Build authority by sharing high-value content about nutrition systems, meal planning logic, and "decision fatigue" in cooking.
- **Channels**:
  - Blog/Articles (Medium, Dev.to, or personal site).
  - Social Media (X/Twitter, Threads) - "Building in Public" (lite version).
- **Brainstorming Ideas**:
  - _Article_: "Why meal planning fails (and how algorithms fix it)."
  - _Tool_: Free simple calculator for "Food Slots" to capture emails.
  - _Content_: "Deconstructing a balanced meal" infographics.

## 💼 Business & Operations

**Model**: Freemium with Monthly Subscription.

- **Free Tier**: Basic slot planning, standard database access.
- **Premium ($X/mo)**: Unlimited history, advanced constraints (macros), auto-shopping lists.
- **Immediate Admin**:
  - [ ] Set up landing page for waitlist. #sphere/wealth

## 🛤️ Roadmap & Tasks

### Phase 1: The Engine (MVP Core)

- **Project Setup**
  - Initialize SvelteKit ✅
  - Setup Tailwind & Shadcn ✅
  - Configure Prisma & Supabase ✅
- **UI skeleton**
  - List of pages 🛠️
  - [[HEWSY UI]]
  - Routes
- **Database Implementation**
  - Create User & Profile models
  - Create Master Data (FoodGroups, Ingredients)
  - Create Plan models (Day, Slot)
- **Core Logic (The Calculator)**
  - Implement Global -> Group mapping
  - Implement Group -> Meal distribution

### Phase 2: The Kitchen

- Ingredient DB structure
- Dish creation & Yield Factors

### Phase 3: The Planner UI

- Drag & Drop Slots
- Daily Logging

## 📝 Notes & Ideas

- _Add your daily notes, random thoughts, or meeting notes here._

- Remember to check the "Yield Factor" logic for raw vs cooked food.

---

## 📚 References

- [[Competitors]]
