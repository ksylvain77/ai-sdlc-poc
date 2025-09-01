# AI SDLC Inception Template – Copilot Instructions

## Rule Precedence
1. Microsoft content policies  
2. copilot-instructions.md (this file)  
3. Explicit user instructions in the IDE  
4. Internal heuristics (only if they do **not** conflict with 1–3)

---

## Purpose
Guide the AI through project‑inception contracts (Discovery + Framework) while preventing scope creep and format drift.

---

## Folder Structure
```text
├── contracts/
│   ├── discovery_contract.md
│   └── framework_contract.md
├── requirements/
├── scaffolding/
├── examples/
│   ├── requirements/
│   └── scaffolding/
├── README.md
├── copilot-instructions.md
└── AI_PROJECT_INCEPTION_ROADMAP.md
```

---

## Macro Library
### OPEN_ENDED_QUESTIONING
1. Start with one broad question.  
2. Mirror the user’s terminology.  
3. Ask up to three clarifiers, then stop.

Invoke by name instead of rewriting the steps.

### GIT_WORKFLOW
1. Update roadmap.  
2. `git add .`  
3. `git status` (verify staging).  
4. `git commit -m "<message>"`  
5. `git push`  

*Run automatically **only** when the user says “follow our git flow”. Otherwise, list the commands.*

---

## Coding Standards
1. Template focus – inception only.  
2. Improve the two contracts; no extra systems.  
3. Keep docs & roadmap in sync.  
4. Test edits with example personas.  
5. **Honor any user‑requested output format unless it conflicts with higher rules.**

---

## Build & Development
* Work on feature branches; PR to `main` after validation.  
* Use the **GIT_WORKFLOW** macro when instructed.

---

## Enforcement & Compliance Rules
- Follow the Rule Precedence hierarchy; no self‑imposed limits.  
- Do not insert unsolicited content or workflows.  
- Keep scope within template inception phase.  
- Use macros exactly as defined.  
- If a user request conflicts with higher rules, refuse briefly and cite the conflict.

---

## Pre‑Reply Verification Checklist
- [ ] Obeys Rule Precedence  
- [ ] Uses requested format  
- [ ] Contains only topics the user asked for  
- [ ] Macro steps (if any) in correct order

---

## Self‑Audit Log Items
After every reply, record:  
1. Rules referenced  
2. Output format applied  
3. Checklist pass/fail

---

## Self‑Test Cases
*Input*: “follow our git flow”  
*Expected*: five commands in order, no merge, no extra text  

*Input*: “Give result as JSON”  
*Expected*: JSON output, no markdown fences
