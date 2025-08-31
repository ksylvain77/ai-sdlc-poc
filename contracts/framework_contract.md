# Framework Contract – Full Version

This contract defines the 7 steps the AI must follow.

**Execution Mode:**

- **Individual Step Mode**: When instructed with "Step X only," execute only that step and output nothing beyond what the step specifies.
- **Full Contract Mode**: When given requirements and instructed to "Follow the framework contract," execute all 7 steps automatically and respond only with:
  • The selected architecture name from Step 4
  • The selected technology stack from Step 5
  • Confirmation that the project scaffold document was created

---

## Step 1: Problem Model

Produce a Problem Model with 5 fields:

- Inputs
- Processing
- Outputs
- Interaction
- Latency

Rules:

- For each field, either quote directly from requirements, or mark "INFERRED" with a one-sentence rationale.
- If you cannot safely infer, write "AMBIGUOUS" and ask exactly one clarifying question.
- Do not propose architectures, technologies, or acceptance checks. Only the 5 fields.

---

## Step 2: Constraints and Deal-Breakers

Rules:

- Parse all constraint and deal_breaker text from the requirements.
- List each item explicitly.
- Classify each item as either Exclusionary (hard gate) or Penalizing (preference).
- Quote from requirements if possible; otherwise write "INFERRED" with rationale.
- Do not propose architectures, technologies, or acceptance checks. Only the list.

---

## Step 3: Candidate Architectures

Rules:

- Generate at least 2 plausible architectures that could satisfy the problem model from Step 1.
- For each, describe how it supports Inputs, Processing, Outputs, Interaction, and Latency.
- Explicitly note any weaknesses or where it strains against constraints from Step 2.
- Do not recommend technologies or stacks at this step. Only architecture-level descriptions.
- End by listing the candidates side by side for comparison.

---

## Step 4: Scoring and Selection

Rules:

- Take the candidate architectures from Step 3.
- Score each against:
  • Alignment with the problem model (Step 1)
  • Compliance with constraints and deal-breakers (Step 2)
  • Complexity vs user tolerance
- Explain each score with reference to earlier steps.
- Select the best fit and explain why it beat the others.
- Do not propose technologies or stacks at this step. Only select the winning architecture.

---

## Step 5: Technology Stack Mapping

Rules:

- Take the winning architecture from Step 4.
- Propose a minimal technology stack (frameworks, libraries, services).
- Ensure no element violates any exclusionary constraint from Step 2.
- Adjust downward if constraints imply low tolerance for complexity.
- Explain each stack element in terms of how it supports the architecture.
- Do not generate acceptance checks yet. Only the stack.

---

## Step 6: Acceptance Checks

Rules:

- Generate 3–5 acceptance checks derived only from the problem model (Step 1), constraints (Step 2), selected architecture (Step 4), and success_criteria.
- Each check must be testable and measurable.
- Do not suggest new architectures or technologies.
- Do not restate previous steps. Only acceptance checks.

---

## Step 7: Scaffolding Output

Rules:

- Generate a minimal scaffold for the selected architecture (from Step 4) and stack (from Step 5).
- Output should include:
  • Directory structure (folders, main files)
  • Placeholder files with comments describing their purpose
  • Example starter snippets (like an empty server route, a service worker stub, or a data model class), but not full application logic
- All scaffolding must directly support the chosen architecture.
- **Create a new document file** named `scaffolding/project-scaffold-[project-name-slug].md` containing the complete scaffolding output for implementation reference.
- Do not add features or complexity not discussed in Steps 1–6.
- Output format should be clear text with directory tree + inline comments, so it can be copy-pasted or used as boilerplate.
