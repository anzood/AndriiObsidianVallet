---
tags:
  - type/note
created: 2025-12-28 22:19
up:
  - "[[HEWSY]]"
related:
  - "[[HEWSY Roadmap]]"
lang: en
---
# Developer Guide: Hybrid SvelteKit Architecture

This document outlines the architecture for building a single SvelteKit codebase that deploys to **Vercel** (Server-Side Rendered for SEO) and builds to **Capacitor** (Static SPA for iOS/Android).

## 1. Architecture Overview
To support both SEO (Web) and Mobile Bundle (App), the application uses a **Bimodal Build System**:

| Feature         | Web Build (Vercel)                       | Mobile Build (Capacitor)                         |
| :-------------- | :--------------------------------------- | :----------------------------------------------- |
| **Rendering**   | SSR (Server-Side Rendering) + Hydration  | CSR (Client-Side Rendering) / SPA                |
| **Adapter**     | `@sveltejs/adapter-vercel`               | `@sveltejs/adapter-static`                       |
| **Entry Point** | Server Request (`hooks.server.ts`)       | `index.html` (Shell)                             |
| **Auth**        | Cookies (`httpOnly`) via `@supabase/ssr` | Bearer Tokens via Local Storage / Preferences    |
| **API Calls**   | Relative (`/api/data`)                   | Absolute (`https://api.yourdomain.com/api/data`) |
## 2. Project Configuration
### 2.1 Dependencies
Install the required adapters:
```bash
npm install -D @sveltejs/adapter-vercel @sveltejs/adapter-static
```
### 2.2 `svelte.config.js`
We dynamically switch the adapter based on the `BUILD_TARGET` environment variable.
```javascript
import adapterVercel from '@sveltejs/adapter-vercel';
import adapterStatic from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const isMobile = process.env.BUILD_TARGET === 'mobile';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    preprocess: vitePreprocess(),
    kit: {
        // Switch adapters based on the build target
        adapter: isMobile 
            ? adapterStatic({
                fallback: 'index.html', // Essential for SPA routing in Capacitor
                strict: false
            }) 
            : adapterVercel(),
        
        // Map aliases to cleanly separate logic if needed
        alias: {
            $mobile: 'src/lib/mobile',
            $web: 'src/lib/web'
        }
    }
};

export default config;
```

### 2.3 `package.json` Scripts
Use these scripts to build for the specific platform:

```json
"scripts": {
    "dev": "vite dev",
    "build:web": "vite build",
    "build:mobile": "BUILD_TARGET=mobile vite build && npx cap sync"
}
```

---

## 3. Authentication (Supabase)

This is the most critical logic to separate. Web uses Cookies (safe, works with SSR). Mobile uses Tokens (persistent, works without server hooks).

### 3.1 The Universal Client Factory (`src/lib/supabase.ts`)
Do not import `supabase` directly from a single file. Use a factory that detects the platform.

```typescript
import { createBrowserClient } from '@supabase/ssr';
import { createClient } from '@supabase/supabase-js';
import { Capacitor } from '@capacitor/core';
import { Preferences } from '@capacitor/preferences'; // Install @capacitor/preferences
import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY } from '$env/static/public';

// Custom storage adapter for Capacitor to ensure auth persists on restart
const CapacitorStorage = {
    getItem: async (key: string) => (await Preferences.get({ key })).value,
    setItem: async (key: string, value: string) => await Preferences.set({ key, value }),
    removeItem: async (key: string) => await Preferences.remove({ key })
};

export const getSupabaseClient = () => {
    if (Capacitor.isNativePlatform()) {
        // Mobile: Standard client with native storage
        return createClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY, {
            auth: {
                storage: CapacitorStorage,
                autoRefreshToken: true,
                persistSession: true,
                detectSessionInUrl: false
            }
        });
    } else {
        // Web: SSR-ready client (cookies handled by browser automatically)
        return createBrowserClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_ANON_KEY);
    }
};
```

### 3.2 Protecting Routes
* **Web:** Use `src/hooks.server.ts` to check cookies and protect routes server-side.
* **Mobile:** Since `hooks.server.ts` **does not run** on the mobile app, you must implement a client-side guard in `src/routes/+layout.ts`.

**Client-Side Guard (Mobile & Client Nav):**

```typescript
// src/routes/+layout.ts
import { redirect } from '@sveltejs/kit';
import { getSupabaseClient } from '$lib/supabase';

export const load = async ({ url }) => {
    const supabase = getSupabaseClient();
    const { data: { session } } = await supabase.auth.getSession();

    // If mobile and no session, force login (simulate middleware)
    if (!session && url.pathname.startsWith('/protected')) {
        throw redirect(303, '/login');
    }

    return { session, user: session?.user };
};
```

---

## 4. Data Fetching Strategy

**Rule:** Never use `+page.server.ts` for data that must appear in the Mobile App.
**Reason:** `+page.server.ts` runs *only* on the server. The mobile app has no server; it is a static file bundle.

### The "Universal Load" Pattern
Use `+page.ts` for all page data loading. It runs on the server (for Web/SEO) and on the device (for Mobile).

**Example: `src/routes/dashboard/+page.ts`**

```typescript
import { PUBLIC_BASE_URL } from '$env/static/public';
import { Capacitor } from '@capacitor/core';

export const load = async ({ fetch, parent }) => {
    // 1. Get the session (from parent layout)
    const { session } = await parent();
    
    // 2. Determine the correct API URL
    // Web: "/api/dashboard"
    // Mobile: "[https://myapp.com/api/dashboard](https://myapp.com/api/dashboard)"
    const apiBase = Capacitor.isNativePlatform() ? PUBLIC_BASE_URL : '';
    
    // 3. Set Auth Headers manually for Mobile (Web cookies are automatic)
    const headers: Record<string, string> = {};
    
    if (Capacitor.isNativePlatform() && session?.access_token) {
        headers['Authorization'] = `Bearer ${session.access_token}`;
    }

    const res = await fetch(`${apiBase}/api/dashboard`, { headers });
    const data = await res.json();

    return { stats: data };
};
```

---

## 5. Deployment & Environment Variables

### 5.1 Vercel (Web)
* **Build Command:** `npm run build:web`
* **Environment:** standard `.env` variables.
* **Output:** Serverless functions + Static assets.

### 5.2 Capacitor (Mobile)
* **Build Command:** `npm run build:mobile`
* **Environment:** Variables must be prefixed with `PUBLIC_` to be bundled into the JavaScript, as there is no runtime environment to read secrets from.
* **Note:** **NEVER** put private API keys (Service Role) in code that runs in `+page.ts`.

### 5.3 Handling "Private" Environment Variables
If you need to access a database directly (bypassing an API), you must do it in `+server.ts` endpoints.
1. **Web:** The browser calls `/api/data`. The Server Endpoint talks to the DB using private keys.
2. **Mobile:** The App calls `https://myapp.com/api/data`. The Vercel Server Endpoint talks to the DB.
3. **Result:** The Mobile App **never** touches the database directly, ensuring security.
