---
tags:
  - type/note
created: 2025-12-17 20:16
up:
  - "[[HEWSY]]"
related:
  - "[[HEWSY Roadmap]]"
  - "[[HEWSY Architecture]]"
lang: en
---
# UI

## Today (main screen)
### Top bar
- Shows calories (consumed over required)
- Shows proteins
### Bottom buttons
- Quick buttons to auto fill food
- Dishes
- Ingredients
- Menu
### Main screen
- Divided to sections (meals)
- Each meal contains set of categories
## Workflow
### Pre-filled menu
- Single press confirms that dish was consumed.
- Long press brings menu, that allows to change the dish.
### Empty menu
- Single press brings dish selector.
- Long press brings menu, that allows to change the dish.

## Units
For a food consumption app, the most important thing to understand is that Americans use **volume (cups)** for almost everything except meat and cheese. If you only provide weight, your users will have to weigh their food on a scale, which many find tedious.
Here is a standard mapping table for your backend. Note that "1 Cup" of different foods has vastly different weights.
### Common US "Cup" to Grams Mapping

| **Food Category** | **Ingredient**             | **1 US Cup (Volume)** | **Grams (Weight)** |
| ----------------- | -------------------------- | --------------------- | ------------------ |
| **Liquids**       | Water, Milk, Juice         | 1 cup                 | **240g**           |
|                   | Oils                       | 1 cup                 | **217g**           |
|                   | Honey, Syrups              | 1 cup                 | **336g**           |
| **Grains**        | All-Purpose Flour          | 1 cup                 | **125g**           |
|                   | White Rice (uncooked)      | 1 cup                 | **185g**           |
|                   | Rolled Oats                | 1 cup                 | **90g**            |
|                   | Pasta (dry, short shape)   | 1 cup                 | **100g**           |
| **Dairy/Fats**    | Butter (1 stick = 1/2 cup) | 1 cup                 | **227g**           |
|                   | Greek Yogurt               | 1 cup                 | **285g**           |
|                   | Shredded Cheese            | 1 cup                 | **113g**           |
| **Produce**       | Chopped Vegetables         | 1 cup                 | **~150g**          |
|                   | Sliced Fruits (Apple/Pear) | 1 cup                 | **~125g**          |
|                   | Leafy Greens (Spinach)     | 1 cup                 | **~30g**           |

---

### Implementation Tips for Your App
1. **The "Meat" Exception:** Americans almost never measure meat in cups. For beef, chicken, or fish, always default to **Ounces (oz)** or **Pounds (lb)**.
2. **Small Increments:** For things like spices, oils, or dressings, use **Tablespoons (tbsp)** and **Teaspoons (tsp)**.
    - 1 tbsp = 15ml (approx. 15g for water-like liquids).
    - 1 tsp = 5ml (approx. 5g for water-like liquids).
3. **Density is Key:** If you allow users to input "1 cup," your database must know _what_ the food is to convert it accurately to grams. "1 cup" of lead weighs much more than "1 cup" of feathers; similarly, "1 cup" of peanut butter (250g) is much heavier than "1 cup" of popcorn (8g).
4. **"Handfuls" and "Items":** For a truly great user experience, allow for "1 medium fruit" or "1 slice." Users prefer these over both grams and ounces.
If you are building the database now, it is best to store everything as **grams** and use these conversion factors only for the UI display and input.

## UI inspirations
- https://motherduck.com/
- https://www.nngroup.com/articles/neobrutalism/
- https://medium.com/@sepidy/how-can-i-design-in-the-neo-brutalism-style-d85c458042de
- https://www.neobrutalism.dev/

## Design notes
That makes a lot of sense—you’re leaning into a "Retro-Digital" or **"Neo-Brutalist"** aesthetic rather than the typical sleek SaaS look.

That "sticker" look comes from high-contrast borders and a lack of depth cues like shadows, favoring flat, layered elements instead. Since you prefer **sharp edges** and **pale, distinct colors**, here is a UI guidance tailored to that specific "Lo-Fi Tech" vibe.
### 1. The "Sticker & Paper" Layout

To get that physical, "pasted on" look, you want to avoid seamless transitions.
- **Sharp 90° Corners:** Use zero border-radius. Every box, button, and input should have hard, sharp corners.
- **The "Hard Shadow" (Sticker Effect):** Instead of soft, blurry shadows, use "hard" shadows. This is a solid block of color offset by a few pixels.
    - _Example:_ A button with a 2px black border and a solid 4px black offset to the bottom right.
- **Layering:** Elements should look like they are sitting on top of each other, like notes on a desk. Use distinct borders to separate everything.
### 2. Pale & Distinct Color Palette
MotherDuck uses "Duck Yellow," but for your version, we’ll move toward a **"Solarized"** or **"Windows 95 Pastel"**palette:
- **Base Background:** Pale Cream (`#F5F2ED`) or a very light "Old Paper" Grey (`#E0E0E0`).
- **Element Backgrounds:** Use "Post-it" pales:
    - Pale Mint (`#D4EDDA`)
    - Pale Lavender (`#E2D9F3`)
    - Faded Peach (`#FCE5CD`)
- **Accent/Action Colors:** Use distinct but "washed out" colors. Instead of neon blue, use a Slate Blue; instead of bright red, use a Muted Terracotta.
### 3. Typography: The "Old Computer" Feel
- **System Fonts:** Use fonts that look native to an OS. **IBM Plex Mono** or **Roboto Mono** are great for that "data/technical" look.
- **High Contrast:** Keep text strictly black (`#1A1A1A`) against the pale backgrounds. No light grey text—that ruins the "printed paper" effect.
### 4. Borders & Lines
- **The "Ink" Rule:** Use a consistent border weight for everything. A 1.5px or 2px solid black border around every card and button makes it feel like a physical sticker.
- **Dividers:** Use dashed or dotted lines (`border-style: dashed;`) to separate sections, mimicking the "perforated paper" look.
### Examples for Inspiration

If you want to see this "Sharp/Pale/Sticker" style in the wild, check out:
1. **Gumroad:** They are the kings of "Neo-Brutalist" design—sharp edges, bold outlines, and pastel blocks.
2. **Figma (specifically their FigJam tool):** Look at how their sticky notes and menus are styled.
3. **Cron (now Notion Calendar):** They use a very refined, pale palette with very distinct, sharp-edged segments.
### Suggested Table of Elements

|**Element**|**Style Choice**|
|---|---|
|**Corners**|0px (Strictly Square)|
|**Borders**|2px Solid Black|
|**Shadows**|Solid (No blur), Offset 4px|
|**Palette**|Pale Creams, Sage, and Muted Blues|
|**Interactive**|Buttons "depress" (shadow disappears) when clicked|
