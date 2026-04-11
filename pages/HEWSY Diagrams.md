---
tags:
  - type/note
created: 2026-02-05 14:48
up:
  - "[[HEWSY]]"
related:
  - "[[HEWSY Architecture]]"
  - "[[HEWSY Roadmap]]"
  - "[[HEWSY UI]]"
lang: en
---
# Diagrams

```mermaid
graph LR
  Start([App Launch]) --> Login{Logged In?}
  Login -- No --> Auth[Sign Up Screen]
  Login -- Yes --> Home[Dashboard]
  Auth --> Home
```

## Jorney
```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```