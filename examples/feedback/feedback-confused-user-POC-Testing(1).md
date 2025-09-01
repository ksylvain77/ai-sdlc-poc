# Feedback — Confused User — POC Testing

## Test Session Overview
- **Persona Used:** #4 Confused User (Unclear Requirements)
- **Project Scenario:** “External Brain” — a simple, low‑friction way to capture and retrieve personal info (notes, to‑dos, small commitments, phone numbers, dates) so things stop getting lost and the user’s “mental load” decreases.
- **Contracts Tested:** Discovery only

---

## Discovery Contract Feedback

### Question Quality
- **Appropriate for persona?** Yes. The questions stayed high‑level, invited stories, and didn’t force premature structure — well‑suited to a confused user who’s still forming the problem.
- **Clear and understandable?** Yes. Prompts used everyday language (e.g., “what moment makes you think ‘ugh’?”) which elicited rich, honest answers.
- **Logical flow?** Strong. You moved from symptoms → context → stakes → constraints → success signals in a natural arc.
- **Missing elements?**
  - A brief, concrete **walkthrough of a recent failure** (“minute‑by‑minute: where did the phone number go missing?”) would reveal root causes and environments (desk vs. phone, while driving, etc.).
  - **Habit/ritual probing** (“When during your day would you naturally check the External Brain?”) to anchor behavior change.
  - **Information lifecycle** questions (capture → find → review → archive/forget) to expose clutter risks.
  - **Privacy & security boundaries** (e.g., the user mentioned passwords – confirm scope boundaries and trust requirements).

### Process Experience
- **Pacing:** Good; the persona had space to wander and refine (“maybe it’s notes… or communication… maybe both”), which surfaced the umbrella problem.
- **Depth vs. breadth:** Mostly depth on pain/emotion; could add a short **environment scan** (phone OS, notifications tolerance, voice capture comfort, accessibility needs).
- **Evidence quality:** You elicited measurable signals (20–30 items/week; “less panic”; “people stop reminding me”) — useful for later metrics.

### Persona Fit
- **In‑character realism:** High. The persona vacillated, self‑corrected, and voiced meta‑concerns (“that might be two different problems”), which is textbook for #4.
- **Where it strained:** None materially; the one moment of tool talk (“should it be on my computer too?”) was handled gently and kept non‑technical.

### What Was Uncovered (Highlights)
- **Problem pattern:** Information scatter → retrieval failure → embarrassment → avoidance → more scatter.
- **Top pains:** Losing capture locations; not trusting existing notes/reminders; social friction (letting people down); ongoing mental load.
- **Frequency/volume:** ~20–30 info items/week; variable day‑to‑day.
- **Scope boundaries:** Primarily personal; family collaboration “maybe later”; work input likely out‑of‑scope initially.
- **Constraints:** Must be **frictionless** (2‑second capture), **simple**, **reliable**, **easy to check** (one place), and **natural** (habit‑friendly).
- **Anti‑goals / risks:** No heavy structure; avoid digital clutter; avoid another abandoned app; quick time‑to‑value required.
- **Budget:** Free preferred; small monthly OK if value obvious.
- **Definition of success (qual):** “My brain can finally relax”; fewer reminders from others; fewer sticky notes; less “oh no, I forgot” panic.

### Gaps / Risks Not Fully Explored
1. **Trigger‑action mapping:** When and how capture happens (lock‑screen widget, voice, SMS‑to‑self, inbox email, photo note, share sheet?).  
2. **Retrieval pathways:** How the user searches or browses later (unified inbox, smart recents, pinned “today,” fuzzy search, natural language?).  
3. **Review cadence:** Daily/weekly “sweep” necessary to prevent clutter; user tolerance for nudges or summaries.  
4. **Context & metadata:** Minimal tags vs. auto‑enrichment (timestamp, location, contact link, source app).  
5. **Trust & resilience:** Offline access, sync reliability, accidental deletion protection, export/backup expectations.  
6. **Privacy lines:** What is *never* stored (e.g., passwords) and how to signal that clearly.  
7. **Accessibility / ergonomics:** One‑hand capture, low‑vision options, voice‑only capture while driving.

### Strengths of the Discovery Run
- Translated a vague feeling into a **clear project name** (“External Brain”) and a **JTBD**: *remember and retrieve small commitments without anxiety*.
- Captured **adoption risks** (fiddly, too formal, slow to help) early — crucial for MVP design.
- Converted emotions into **operational signals** (panic ↓, reminders from others ↓, sticky notes ↓).

### Weaknesses / Opportunities
- Lacked a **single canonical workflow** to test in prototype 1 (e.g., “capture from lock screen in <2s → appears in ‘Today’ list by default”).
- Didn’t assign any **quant targets** yet (e.g., capture time ≤ 2s; retrieval ≤ 10s; daily review ≤ 2m; ≤ 5 taps per action).

### Suggested Improvements to the Discovery Contract
- Add a **“Last Bad Day Replay”**: “Recreate your most recent miss in detail (timeline, locations, tools used).”
- Insert **“Rituals & Cues”**: “What daily moments could we latch onto for an effortless check‑in?”
- Include **“Zero‑to‑Value in 1 Minute”**: “If you had 60 seconds to set this up, what would *have* to be there?”
- Add **“Boundaries & Red Flags”**: explicit “never store X”, “no more than Y notifications/day,” and a hard stop on complexity.
- Close with **“First Prototype Script”**: agree on one end‑to‑end task the MVP must nail (capture → retrieval → confirmation).

---

## Framework Contract Feedback (Not tested in this session)
- **Status:** N/A
- **Note:** When ready, the framework should lock in guardrails around capture surfaces, storage model, review loop, and failure modes (sync/offline), based on the Discovery outputs above.

---

## Output Quality (Artifacts from Discovery)
- **Persona‑aligned problem statement:** ✅ Clear (“a brain outside my brain”).
- **JTBD:** ✅ “When small bits of info appear during the day, help me capture and retrieve them later so I keep commitments without stress.”
- **Constraints/Anti‑goals:** ✅ (simple, fast, natural; avoid heavy structure/clutter).
- **Initial success metrics (qual):** ✅
- **Initial success metrics (quant):** ⚠️ Add targets (see below).

### Proposed Initial Metrics & Definitions of Done
- **Capture time:** ≤ **2 seconds** from unlock to saved (1 tap + dictation or 2 taps + text).  
- **Retrieval time:** ≤ **10 seconds** to find any item added in the last 7 days via a single “All” screen + search.  
- **Daily review burden:** ≤ **2 minutes** for today + overdue items.  
- **Stickiness:** ≥ **5 days/week** with at least one capture or review action during week 2 of trial.  
- **Failure rate:** < **1%** of captures lost/desynced over a 30‑day period.  
- **Social signals:** External reminders from others decrease by **50%** within 30 days.

### Risks & Mitigations
- **Abandonment risk (habit doesn’t stick):** Start with **one capture surface** (lock‑screen or share‑sheet); enable **automatic daily digest** at a time the user already checks phone.  
- **Digital clutter:** Default to a **single “Today” inbox**, add **one‑tap pin**, and auto‑archive items older than N days unless pinned.  
- **Over‑complexity:** Hide tags/folders by default; rely on **search + recency**; allow later structure only when needed.  
- **Trust failure:** Provide **local cache + offline**, visible **sync status**, and **undo** for the last action.  
- **Scope creep (passwords, work systems):** Clear **“Out of Scope v1”** section; suggest a dedicated password manager linkage later.

---

## Recommended Next Steps (Concrete)
1. **Proto 0.1 User Flow (text spec):**  
   - **Capture:** Lock‑screen widget → tap → microphone opens → speak → auto‑transcribe → saved to “Today.”  
   - **Retrieve:** Open app → “Today” shows last 24h captures → type 1–2 words in search → result surfaces → one‑tap copy or call.  
   - **Review:** 7pm daily digest notification → open → confirm/complete/pin three items → auto‑archive rest after 7 days.
2. **Quant Targets:** Adopt the **metrics** above as acceptance criteria for Proto 0.1.  
3. **Usability Test Script:** Give the user 4 tasks (capture a phone number, capture an idea, retrieve “call Sam,” clear today’s items) and time each.  
4. **Friction Audit:** After 48 hours, list every step >2 taps or >10s → remove or defer.  
5. **Scope Fence:** Publish “V1 won’t do” list (no work sharing, no tags/folders, no password storage).  
6. **Success Dashboard:** Tiny in‑app counters: captures/day, retrieval median, review streak — to provide confidence and habit momentum.

---

## Template Feedback (Meta)
- **Clarity & coverage:** Good, but add sections for **Trigger‑Action mapping**, **Lifecycle**, and **Prototype Script** to better bridge Discovery → MVP.  
- **Missing questions:** “Walk me through the last time this failed”; “Where are you physically and what are you doing when captures happen?”; “What would you delete from similar tools?”  
- **Redundant questions:** None problematic; some motivation questions could be consolidated.  
- **Time to complete:** Reasonable for Discovery. A detailed fill like this takes ~10–15 minutes.

---

## Overall Ratings
- **Discovery Contract:** ★★★★☆ — empathetic and outcome‑oriented; add a few operational questions to tighten MVP scope.  
- **Framework Contract:** N/A (not exercised).  
- **Would recommend to others:** **Yes**, especially for early, ambiguous problem spaces where emotion and habit matter.