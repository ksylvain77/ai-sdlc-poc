# Initial Prompts for Contract Testing

## Discovery Contract Initial Prompt

```
I need to test the discovery contract with you acting as a specific persona.

First, please confirm you have access to:
- chatgpt-instructions.md (your testing instructions)
- persona-guide.md (the 15 personas and testing guidelines)
- feedback-template.md (for end-of-session feedback)

Once confirmed, I'll assign you a persona number (1-15) and we'll begin the discovery contract testing process.

Ready to start?
```

**First Question (Step 1):**

```
Let's start with Step 1: Project Name & Problem Statement

I need two things from you:
1. A simple project name (for file naming)
2. What problem you're trying to solve in one sentence

What would you like to call this project, and what's the core problem you're solving?
```

## Framework Contract Initial Prompt

```
I need to test the framework contract with you acting as a specific persona.

First, please confirm you have access to:
- chatgpt-instructions.md (your testing instructions)
- persona-guide.md (the 15 personas and testing guidelines)
- feedback-template.md (for end-of-session feedback)

Once confirmed, I'll assign you a persona number (1-15) and we'll begin the framework contract testing process.

Ready to start?
```

**First Question (Step 1):**

```
Let's start with Step 1: Problem Model

I need to create a Problem Model with 5 fields based on your requirements:
- Inputs (what goes into the system)
- Processing (what the system does)
- Outputs (what comes out)
- Interaction (how users interact with it)
- Latency (timing requirements)

Based on your requirements, I'll fill these out by either quoting directly from what you've told me, marking items as "INFERRED" with rationale, or marking as "AMBIGUOUS" if I need clarification.

Let me start building your Problem Model.
```

## Combined Testing Initial Prompt

```
I need to test both the discovery and framework contracts with you acting as a specific persona.

First, please confirm you have access to:
- chatgpt-instructions.md (your testing instructions)
- persona-guide.md (the 15 personas and testing guidelines)
- feedback-template.md (for end-of-session feedback)

Once confirmed, I'll assign you a persona number (1-15) and we'll run through both contracts sequentially.

Ready to start?
```

**First Question (Discovery Step 1):**

```
Let's start with Step 1: Project Name & Problem Statement

I need two things from you:
1. A simple project name (for file naming)
2. What problem you're trying to solve in one sentence

What would you like to call this project, and what's the core problem you're solving?
```

## Session Commands Reference

**During Testing:**

- `DEBUG` - Break character to discuss testing
- `PERSONA [number]` - Switch to different persona

**End Session:**

- `SESSION OVER - Discovery only`
- `SESSION OVER - Framework only`
- `SESSION OVER - Both contracts`

After session ends, request feedback with: "Please generate feedback using the template"
