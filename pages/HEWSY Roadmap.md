---
tags:
  - sphere/wealth
  - type/note
up:
  - "[[HEWSY]]"
---

# 🗺️ HEWSY: Non-Technical Task Roadmap

## 1. Data & Content Strategy ("The Fuel")

_Since you are manually entering data, you need to curate strictly. Quality > Quantity._

- **Define the "MVP Pantry":** Do not try to support every food exists. Create a list of the **top 20-30 staples** that fit your "Efficient Health-Seeker" profile (e.g., Chicken Breast, Rice, Oats, Eggs, Whey Protein, Olive Oil).
- **Standardize "The Unit":** Decide now: will everything be measured in grams? Do you accept "1 cup"? For a "medical/scientific" vibe, sticking to weight (grams) is safer and easier to code.
- **Yield Factor Reference Sheet:** Create a master spreadsheet (Excel/Google Sheets) defining the math for your "Raw vs Cooked" logic. You need to define the multiplier for every item in your MVP Pantry (e.g., Rice = 3.0x expansion, Chicken = 0.75x shrinkage).
- **Recipe/Dish "stubbing":** Define 5-10 "Dishes" that are just combinations of your MVP Pantry. You need these to test the "Slot" system logic.

## 2. Design & UX ("The Flow")

_You have two distinct user flows (Pre-planned vs. Just-in-time). The UI needs to handle both._

- **Flow Charting:** Sketch the "Just-in-Time" flow.
  - _Scenario:_ User is hungry -> Taps empty Slot -> Sees list -> Selects "Chicken & Rice" -> App asks: "How much?" OR App suggests: "Eat 200g". -> User confirms.
- **The "Deploy Food" Interaction:** Design the specific feedback loop for logging a meal. Since the vibe is minimalist and fast, this shouldn't require 5 clicks. Maybe a swipe action?.
- **Onboarding Script:** Since you are going public immediately, you won't be there to explain the app. You need 3-4 screens that explain:
  1.  What a "Slot" is.
  2.  The difference between Ingredients and Dishes.
  3.  How to set their biological goal.

## 3. Marketing & "Stealth Education" ("The Hype")

_Building authority before the product exists._

- **The "Why" Content:** Write a blog post or thread about _why_ existing apps fail men who just want to "Deploy Food." Use the pain points you listed (reactive tracking vs. proactive planning).
- **Waitlist Landing Page:** Create a simple page gathering emails. Value prop: "The first nutrition app that tells you what to eat, instead of shaming you for what you ate.".
- **Lead Magnet:** You mentioned a "Free simple calculator." Build a tiny web tool that calculates "How much cooked rice equals 100g raw rice?" and lets people use it for free in exchange for an email. This validates your "Yield Factor" problem.

## 4. Legal & Admin ("The Safety")

_Public launch requirements._

- **Disclaimers:** You are giving nutrition advice (algorithmically). You need a clear Terms of Service stating you are _not_ a doctor and this is for informational purposes only.
- **Support Channel:** Set up a dedicated email (e.g., `hello@hewsy.com`) or a Discord server link so early users can report bugs without crashing your personal inbox.

---

## 💡 Insight on the "Two Options" Flow

You mentioned two ways to use the app:

1.  **Planner:** Create menu upfront -> Confirm later.
2.  **Ad-hoc:** Tap slot -> Pick from list -> Confirm.

**Recommendation:** For the MVP, prioritize the **Ad-hoc (Option 2)** flow in your design.
_Why?_ The "Efficient Health-Seeker" often _intends_ to plan but fails (that's the pain point). If they forget to plan, the app must still work instantly when they are hungry. If the app relies 100% on them pre-planning, they will churn the first day they forget to plan.


## Ideas
You are absolutely right. The word "tells" can sound authoritarian, and for a brand that aims to be "warm" and "friendly", you want to sound like a **partner**, not a drill sergeant.
Your target audience wants to reduce "decision fatigue," but they still want to feel like the captain of the ship.
Here are a few variations that keep the _proactive_ benefit without stripping away the user's agency:
### Option 1: The "Problem Solver" (Focus on utility)
> "The first nutrition app that **answers** 'what should I eat?' instead of judging what you already ate."
- **Why it works:** "Answers" implies you have a question and the app provides a solution, rather than issuing a command.
### Option 2: The "Architect" (Focus on the system)
> "The app that **designs** your meals for you, so you don't have to track them later."
- **Why it works:** This leans into your "Smart Nutrition Architect" description. It sounds constructive and professional.
### Option 3: The "Assistant" (Focus on ease)
> "Finally, an app that **handles** the planning, so you can just enjoy the eating."
- **Why it works:** It focuses on offloading the work (the "cognitive load" you mentioned) rather than dictating the action.
### Option 4: The "Action-Oriented" (Focus on the button)
> "Don't track. Just **deploy**. The app that prepares the plan so you don't have to."
- **Why it works:** This uses your internal "Deploy Food" concept. It is very masculine and efficient, fitting the "Men driven by Aesthetics & Health" profile.
**Which direction feels closer to the "Medical but warm" vibe you are aiming for?** Option 1 feels the safest, but Option 4 is the most unique to your specific audience.