---
tags:
  - type/project
  - sphere/wealth
  - status/idea
created: 2025-12-10 09:48
up:
  - "[[Map of Content]]"
related:
  - 
lang: en
---
# Crypto rush

## 📝 Content
The idea is to catch the crypto market movements paying attentions on the market deals - the volume and number of deals.
## 🛠️ Stack
- [Vercel](https://vercel.com/) - frontend
- [Railway](https://railway.com/dashboard) - backend
- [Supabase](https://supabase.com/) - database and authentications
## 🗺️ Roadmap
## Understand, what to show


---
## Notes

Here is the "Silent Killers" checklist for the **Supabase + Prisma + Railway** stack.
These are the exact issues that break this specific combination. I have ranked them by "Likelihood of Causing a 3 AM Panic."
### 1\. The "Transaction Mode" Trap (Most Common)

Supabase now forces you to use their connection pooler (Supavisor) for scalability. This pooler runs in **Transaction Mode**, which Prisma *can* use but often hates during migrations.
  * **The Killer:** You try to run `prisma migrate deploy` using your regular connection string. It fails with errors about "prepared statements" or "advisory locks."
  * **The Fix:** You need **TWO** URLs in your `.env` file.
      * `DATABASE_URL`: Use the **Transaction** pooler (Port **6543**). Used by your *app* (long-running).
      * `DIRECT_URL`: Use the **Session** pooler or Direct connection (Port **5432**). Used *only* by Prisma migrations.
  * **Action:** Update your `schema.prisma`:
    ```prisma
    datasource db {
      provider  = "postgresql"
      url       = env("DATABASE_URL")
      directUrl = env("DIRECT_URL")
    }
    ```

### 2\. The "Missing Build Command" (Railway Specific)

Railway is smart, but it's not psychic. If you just push your code, your Node app will start, but the Prisma Client files (`node_modules/.prisma`) won't exist yet because they are generated on the fly.

  * **The Killer:** Your app crashes on startup with `Error: @prisma/client did not initialize yet.`
  * **The Fix:** In your Railway service settings, change the **Build Command** to:
    `npm install && npx prisma generate`
    *(Note: If you are using Yarn/Pnpm, adjust accordingly. This ensures the client is built before the app starts.)*

### 3\. Connection Exhaustion (The "Too Many Clients")

Even though you are on Railway (a long-running server), Supabase's free tier has a hard limit of about **60 direct connections**.

  * **The Killer:** You scale your Railway service to 2 or 3 instances (replicas). Each instance opens a pool of 20 connections. Suddenly, you hit 60, and your app crashes with `FATAL: remaining connection slots are reserved for non-replication superuser`.
  * **The Fix:** Explicitly limit Prisma's pool size in your `.env` file.
    `DATABASE_URL="postgres://...?pgbouncer=true&connection_limit=10"`
      * Set `connection_limit` to something low (like 5 or 10). Your volume indicator bot is single-threaded; it doesn't need 20 connections.

### 4\. The "Zombie" Migrations

On Vercel, you never run migrations in production. on Railway, you *can*, but you have to tell it when.

  * **The Killer:** You push a code change that requires a DB schema change, but you forget to apply it. The new code tries to write to a column that doesn't exist yet.
  * **The Fix:** Add a "Pre-start" or "Deploy" command in Railway, OR just update your **Start Command** to run migrations before the app boots:
    `npx prisma migrate deploy && node dist/index.js`
    *(Colloquially called "migrations at boot time"—safe for small apps, risky for huge ones, but perfect for your stage).*

### Summary Checklist


**Next Step:** Your Volume Indicator will need to calculate moving averages. Would you like a **Python (Pandas)** or **Node.js (TechnicalIndicators)** snippet to calculate this efficiently without re-looping through the whole array every time a new trade comes in?
## 📚 References

-
