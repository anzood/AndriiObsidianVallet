---
tags:
  - type/project
  - status/idea
  - sphere/wealth
lang: en
---

# **Project Spenc: Lean Budget & AI Receipt Scanner**

## **1\. Project Overview**

### **1.1. The Mission**

Most personal budget apps are either too simple (basic lists) or too complex (bank syncs, investment tracking). "Project Spenc" is a minimalist, privacy-first web app that answers one question: **"How much money do I have left to spend in my key categories this month?"**  
Its core differentiator is an AI-powered receipt scanner that uses Gemini to eliminate the friction of manual data entry.

### **1.2. Core Features**

- **Budget "Envelopes":** Create simple monthly budgets (e.g., "Groceries: $500", "Fun: $150").
- **Manual Transaction Entry:** Quickly add, edit, or delete expenses manually.
- **AI Receipt Scanning:** Upload or snap a photo of a receipt. The app will use AI to pre-fill the merchant, total, date, and suggested category.
- **Visual Dashboard:** The homepage will feature a clean dashboard of progress bars showing the remaining funds in each category.
- **Data Ownership:** Export all transaction data to a CSV file at any time.

## **2\. Technology Stack**

This stack is chosen for its high developer velocity, excellent free tiers, and seamless integration.

| Technology           | Role                 | Rationale (Why?)                                                                                                                                                                                              |
| :------------------- | :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **SvelteKit**        | Full-stack Framework | The core of the app. Handles both the reactive frontend UI and the secure backend API (Form Actions). Its server-driven approach is perfect for this task.                                                    |
| **Supabase**         | Database & Auth      | Provides a powerful Postgres database, user authentication, and file storage (for receipts) all in one. The free tier is generous, and it integrates perfectly with SvelteKit.                                |
| **Vercel**           | Deployment / Hosting | Offers a zero-configuration, CI/CD deployment pipeline for SvelteKit. Serverless functions will host our backend logic, and the edge network will deliver the app globally.                                   |
| **Tailwind CSS**     | Utility-First CSS    | Allows for rapid, custom UI development without writing traditional CSS files. Ensures a consistent design system.                                                                                            |
| **shadcn-svelte**    | UI Component Library | Provides a set of beautiful, accessible, and unstyled components (like Buttons, Dialogs, Cards) that work on top of Tailwind. This saves 100s of hours on UI development.                                     |
| **Gemini 1.5 Flash** | AI Data Extraction   | The "magic" feature. Used via the Gemini API to parse receipt images. It's far more powerful than simple OCR as it can _understand_ context (e.g., "Starbucks" \= "Fun" category) and return structured JSON. |

## **3\. Architecture & Data Flow**

### **3.1. Standard Transaction (Manual)**

1. **Client:** User fills a form in SvelteKit (+page.svelte).
2. **Server:** User submits the form. SvelteKit's **Form Action** (+page.server.ts) receives the data on the server.
3. **Database:** The server action validates the data and uses the Supabase client to insert a new row into the transactions table.

### **3.2. AI Receipt Scan Data Flow ("Smart Scan")**

This is the key flow that uses the full stack:

1. **Client (Upload):** User clicks the "Scan Receipt" button. The SvelteKit frontend (+page.svelte) POSTs the image File to a dedicated SvelteKit Form Action (?/scanReceipt).
2. **Server (Process):** The action (+page.server.ts), running on a Vercel Serverless Function, receives the image. It securely uses the GEMINI_API_KEY to send the image buffer to the Gemini 1.5 Flash API.
3. **AI (Parse):** Gemini analyzes the image and returns a structured **JSON** object, as defined by our API schema (e.g., { "merchant": "Walmart", "total": 42.50, ... }).
4. **Client (Review):** The server action _does not save_ the data. Instead, it returns the JSON object to the frontend. The SvelteKit page (form.scannedData) updates, **pre-filling** the form fields.
5. **Client (Save):** The user verifies the pre-filled data, makes any changes, and clicks "Save." This submits the _final_ data to the standard ?/saveExpense server action, which saves it to Supabase.

## **4\. Database Schema (Supabase Postgres)**

The schema is designed to be as "lean" as possible.  
**Table: categories**

- id (uuid, primary key)
- user_id (uuid, foreign key to auth.users.id)
- created_at (timestamp)
- name (text, e.g., "Groceries")
- monthly_limit (decimal, e.g., 500.00)

**Table: transactions**

- id (uuid, primary key)
- user_id (uuid, foreign key to auth.users.id)
- category_id (uuid, foreign key to categories.id)
- created_at (timestamp)
- amount (decimal, e.g., 42.50)
- merchant (text, e.g., "Walmart")
- date (date, e.g., "2025-11-17")
- note (text, optional)

**Note on Users:** The users table is provided by **Supabase Auth** (auth.users). We only need to reference its id in our tables.

## **5\. Deployment & Environment**

The app will be deployed to Vercel using the @sveltejs/adapter-vercel. The following environment variables will be required:

### **5.1. Public (Client-Side)**

- PUBLIC_SUPABASE_URL: The Supabase project URL.
- PUBLIC_SUPABASE_ANON_KEY: The Supabase project anon key.

### **5.2. Private (Server-Side only)**

- GEMINI_API_KEY: The Google AI Studio API key. This will be stored in Vercel's private environment variables and accessed securely in SvelteKit via $env/static/private.
