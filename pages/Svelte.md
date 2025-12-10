---
tags:
  - type/note
created: 2025-12-02 15:02
up:
  - "[[Web development]]"
related:
  - 
lang: en
---
# Svelte
## What is Svelte?
Svelte is a radical approach to building user interfaces. Unlike frameworks like [[React]] or [[Vue]], which do the bulk of their work in the _browser_ (runtime), Svelte shifts that work into a **compile step** that happens when you build your app.
Instead of using techniques like a Virtual DOM diffing, Svelte writes code that surgically updates the DOM when the state of your application changes.
## Key Differentiators
- **It's a Compiler, not a Library:** Svelte compiles your code into tiny, framework-less vanilla JavaScript.4 This results in incredibly small bundle sizes and fast load times.
- **No Virtual DOM:** Because Svelte resolves how the app should update at _build time_, it doesn't need the overhead of a Virtual DOM at _runtime_. It updates variables directly.
- **Truly Reactive:** Reactivity is baked into the language. To update the state, you simply assign a new value to a variable (e.g., `count = count + 1`), rather than using complex state management hooks or proxies.
- **Less Boilerplate:** Svelte is designed to let you write significantly less code to achieve the same result as other frameworks.
## Structure
Svelte components are written in `.svelte` files, which contain HTML, logic (JavaScript), and styles (CSS) all in one place.
> **Note:** Svelte automatically scopes CSS to the component by default, meaning your styles won't accidentally leak and affect other parts of your application.
## Summary

Svelte is ideal for developers who want **high performance**, **low overhead**, and a syntax that feels very close to standard HTML and JavaScript.

---
## 📚 References

- [Svelte 5 Basics - Complete Svelte 5 Course for Beginners](https://www.youtube.com/watch?v=8DQailPy3q8&list=PLLnpHn493BHHfbsxiWvG7-0bLAuPomvei)
- [The Complete Svelte 5 Course](https://joyofcode.xyz/learn-svelte)
- [Learn SvelteKit Hooks Through Example](https://joyofcode.xyz/sveltekit-hooks)
