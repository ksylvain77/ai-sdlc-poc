# Project Overview

## Rule Precedence

1. Microsoft content policies
2. copilot-instructions.md (this file)
3. Explicit user instructions received in the IDE
4. Internal heuristics (only when not in conflict with 1-3)

This repository contains an AI SDLC Inception Template - a reusable template that transforms ideas into ready-to-build software projects through structured AI contracts. Users copy this template to start new projects, then execute two AI contracts (Discovery + Framework) to go from "I have an idea" to "I'm ready to build" with a complete project scaffold.

## Folder Structure

```
├── contracts/
│   ├── discovery_contract.md      # Requirements gathering contract
│   └── framework_contract.md      # Architecture selection contract
├── requirements/                  # (empty - populated during contract execution)
├── scaffolding/                   # (empty - populated during contract execution)
├── examples/                      # Proof-of-concept examples for reference
│   ├── requirements/              # Example JSON requirements
│   └── scaffolding/               # Example project scaffolds
├── README.md                      # Template usage instructions
├── copilot-instructions.md        # AI agent guidelines
└── AI_PROJECT_INCEPTION_ROADMAP.md # Development phases
```

## Libraries and Frameworks

This template doesn't use specific libraries - the AI executing the contracts generates appropriate technology stacks based on requirements. Proven to work with Node.js/Express, Java/Kafka/Kubernetes, React Native, and other stacks as determined by the AI during contract execution.

## Coding Standards

1. **Template Focus**: This is a template for project inception, not a complex system
2. **Contract Refinement**: Focus on improving the two core contracts based on feedback
3. **Simple & Focused**: Two contracts, get a scaffold, start building
4. **Don't expand scope**: No additional systems, just improve what we have
5. **Validate changes**: Test contract improvements with real examples
6. **Document clearly**: Keep README and roadmap aligned with actual capabilities
7. **Template maintenance**: Focus on making contracts more reliable and usable
8. **AI-driven decisions**: Contracts guide AI to make appropriate technology choices
9. **When editing contracts, test with examples to ensure they still work**
10. **Keep contracts focused on inception phase only**
11. **Honor any user-requested output format (JSON, plaintext, command-only, etc.) unless it conflicts with higher-order rules.**

## Build and Development

- This is a template repository - users copy it to start new projects
- Use Git branches for contract refinements (currently on phase-3/contract-refinement)
- Test contract changes with real examples across complexity levels
- Merge improvements back to main when validated
- Focus on contract reliability and output quality

**Git Workflow:**

- Update roadmap to reflect completed contract improvements
- Always do final `git add .` and `git status` check before committing
- Ensure all changes are included in commits

## Project-Specific Guidelines

**Contract Testing Process (Template Refinement Only):**

- Execute contracts collaboratively with human as intermediary
- Human takes contract questions to ChatGPT (acting as persona proxy for real users)
- ChatGPT responds as assigned persona to simulate real user behavior
- Human brings persona responses back for contract continuation
- Complete contract execution and create deliverables in workspace
- This process is only for testing/refining the template, not end-user workflow

**Real End-User Workflow:**

- Real users copy template and work directly with any AI
- AI executes contracts with real human users
- ChatGPT is just a testing proxy, not part of final product

- Update roadmap to reflect completed contract improvements
- Follow the 3-phase approach: Discovery ✅, Framework ✅, Refinement 🚧
- Prioritize contract reliability over feature expansion
- Test improvements against proven examples (PWA, mobile, API, enterprise)
- Keep scope focused on project inception template

## Enforcement & Compliance Rules

- No self-imposed restrictions; follow only the rule-precedence hierarchy.
- Never insert unsolicited content or workflows beyond explicit user requests.
- Forbid scope creep: keep responses within the template's inception phase.
- When the user explicitly asks for Git workflow commands, list them in order; do not run them automatically.
- If a user instruction conflicts with higher rules, respond with a concise refusal and cite the conflicting rule.

## Pre-Reply Verification Checklist

- [ ] Confirm response obeys rule precedence.
- [ ] Confirm requested format is used.
- [ ] Confirm no extra content or skipped mandatory steps.
- [ ] Confirm scope limited to inception template.

## Self-Audit Log Items

After sending each reply, log internally:

1. Which rule set was referenced.
2. Whether any user format was applied.
3. Checklist pass/fail result.

```

```
