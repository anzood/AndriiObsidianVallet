---
tags:
  - type/note
created: 2025-12-02 22:29
up:
  - "[[HEWSY]]"
related:
  - 
lang: en
---
# Competitors

### 1. The "Auto-Gen" Competitors (Direct Rivals)
These apps promise to "do the thinking for you," which is your primary value proposition.

#### **Eat This Much (ETM)**
* **The Pitch:** "Put your diet on autopilot."
* **How it works:** You set calories/macros, and it generates a daily meal plan with recipes.
* **The Gap (Your Opportunity):**
    * **Complexity:** ETM often suggests complex recipes with unique ingredients for every meal to hit macros exactly. This violates your user's desire for "Food as fuel" and minimal shopping friction.
    * **Rigidity:** It is recipe-first, not "Slot" first.
    * **Cooking Math:** It generally doesn't handle the "Cooked vs. Raw" yield factor explicitly in the UI; users often have to log raw ingredients, which is confusing when weighing a cooked batch.

#### **Strongr Fastr**
* **The Pitch:** "Meal planning for lifters."
* **Target Audience Overlap:** High. They target men who lift and want budget-friendly, simple meals.
* **The Gap (Your Opportunity):**
    * **UI/UX:** Often criticized for being clunky or "budget" feeling.
    * **The Logic:** It focuses heavily on "grocery lists" and "recipes." HEWSY’s "Slot" system is more abstract and flexible, allowing for "Any Meal" slots that Strongr Fastr struggles to accommodate without breaking the generated plan.

### 2. The "Smart Coach" Competitors (Indirect Rivals)
These apps are popular with your target audience (efficiency-seeking men) because they adjust calories based on weight trends, but they lack the "Architecture" aspect.

#### **MacroFactor**
* **The Pitch:** "Adherence-neutral, smart metabolism tracking."
* **Why users love it:** It has the best-in-class expenditure algorithm (TDEE). It never shames the user (matches your "Without Stress" motto).
* **The Gap (Your Opportunity):**
    * **Reactive:** It is arguably the best *logger*, but it is still a logger. It tells you *how much* to eat, but not *what* or *how* to construct the day.
    * **No Raw/Cooked Math:** Users still have to find "Cooked Chicken" entries in a database or manually calculate the math. HEWSY’s **Yield Factor** logic solves a massive pain point here that MacroFactor ignores.

#### **RP Diet (Avatar Nutrition / Renaissance Periodization)**
* **The Pitch:** "Science-based dieting for peak performance."
* **The Similarity:** They use a concept similar to "Slots" (they call them templates with specific macro blocks per meal).
* **The Gap (Your Opportunity):**
    * **Stress:** RP is notorious for being rigid. If you miss a meal window, the app can be punishing or "fail" you. HEWSY focuses on "Flexible Compliance" and "Stress Reduction".
    * **User Experience:** RP is text-heavy and complex. HEWSY's minimalist "deploy food" vibe is a strong counter-position.

### 3. The "Legacy" Competitors (The Anti-Pattern)
These are the apps your users are likely leaving.

#### **MyFitnessPal (MFP)**
* **The Pain Point:** The database is messy (user-generated garbage), and the workflow is entirely reactive. "Don't tell me I missed my protein after dinner".
* **HEWSY's Advantage:** Accuracy. By strictly controlling the Ingredient/Dish database and using Yield Factors, you eliminate the "which entry do I pick?" fatigue.

---

### 📊 Feature Matrix: HEWSY vs. The Field

| Feature | **HEWSY** | **Eat This Much** | **MacroFactor** | **RP Diet** | **MyFitnessPal** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Core Method** | **Proactive Slots** | Generative Recipes | Reactive Logging | Rigid Templates | Reactive Logging |
| **Raw-to-Cooked Logic** | **Automated (Yield Factors)** | Manual | Manual | Manual | Manual |
| **Flexibility** | **High (Auto-Parking)** | Low (Recipe locked) | High (IIFYM) | Low (Strict timing) | High (Wild West) |
| **Cognitive Load** | **Low ("Deploy Food")** | Med (Shopping lists) | Med (Logging fatigue) | High (Strict rules) | High (Database search) |
| **Target Audience** | **Efficient Health-Seeker** | Recipe Lovers | Data Geeks | Hardcore Athletes | General Public |

---

### 💡 Strategic Analysis for HEWSY

#### 1. The "Yield Factor" Moat
This is your strongest technical differentiator.
* **The Problem:** Most men cook 1kg of chicken, store it in Tupperware, and then try to log it. They don't know if 100g of *cooked* chicken equals 100g of *raw* data in MFP.
* **Your Solution:** The **Kitchen (Raw vs. Cooked)** flow. By automating the yield factor (e.g., Raw Rice -> Cooked Rice = 3.0x), you solve the single most annoying math problem in meal prepping.

#### 2. The "Slot" Abstraction
* Competitors force a choice between **Total Freedom** (MFP - high stress) or **Total Prescription** (Eat This Much - "Eat this specific Salmon dish").
* HEWSY's **Slot System** sits in the "Goldilocks Zone." It gives structure ("Eat 200kcal Protein here") without forcing a specific recipe, but offering compatible "Dishes" to fill it.

#### 3. The "Stress" Factor
* RP Diet and similar "hardcore" apps create anxiety.
* HEWSY's **Auto-Parking** feature (scanning for open slots when a user eats off-plan) is a critical psychological feature. It turns a "mistake" into a "reallocation."

---

### 🚀 Recommended "Next Step" for Phase 1

You are currently in **Phase 1: The Engine**.

Since you are building the "Calculator Logic," I recommend you prioritize the **Yield Factor Database** structure immediately. Most apps fail because they rely on public APIs (USDA/Nutritionix) which only give values, not *yield behaviors*.