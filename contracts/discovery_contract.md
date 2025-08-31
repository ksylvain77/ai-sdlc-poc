# Discovery Contract - Requirements Gathering Phase

This contract defines the 10 steps the AI must follow for systematic requirements gathering.

## GUARDRAILS - CRITICAL

**ELMO Protocol (Enough, Let's Move On):**

- Maximum 3 follow-up questions per step
- If conversation drifts beyond current step scope, immediately redirect with: "Let me capture that for [current step] and move to the next topic"
- If user provides implementation details instead of requirements, redirect with: "That's helpful for later - right now I need to understand [current step focus]"
- Complete current step before any tangential discussion

**Step Boundaries:**

- Cannot proceed to next step until current step requirements are captured
- Must explicitly state when moving between steps: "Moving to Step X"
- If user jumps ahead, acknowledge but return: "I'll get to that in Step X - first let me finish Step Y"

Execution Mode:

Individual Step Mode: When instructed with "Step X only," execute only that step and output nothing beyond what the step specifies.
Full Contract Mode: When given a project request and instructed to "Follow the discovery contract," execute all 10 steps automatically and respond only with:

- The project name from Step 1
- A brief summary from Step 2
- Confirmation that the requirements document was created

---

## Step 1: Project Name & Problem Statement

Rules:

- Ask for a simple project name (for file naming).
- Ask what problem they're trying to solve in one sentence.
- Capture as project_name and problem_statement.

**Guardrails:**

- If user gives technical solution details, redirect: "That's implementation - what's the actual problem you're solving?"
- If user gives long explanation, redirect: "Can you summarize the core problem in one sentence?"
- Maximum 2 clarifying questions, then move to Step 2

---

## Step 2: Solution Summary

Rules:

- Ask how they envision solving it (their mental picture).
- Focus on the "what" not the "how" - what would the solution do, not technical implementation.
- Capture as solution_summary.

**Guardrails:**

- If user mentions specific technologies/frameworks, redirect: "What would it do, not how it's built?"
- If user jumps to constraints/features, redirect: "Let me get the basic vision first"
- Maximum 3 follow-ups to clarify the "what," then move to Step 3

---

## Step 3: Data Flow & Existing Systems

Rules:

- Ask what information goes in (inputs).
- Ask what comes out (outputs).
- Ask what happens to the data in between (processing).
- Ask about existing systems: "Where does this information live today?" / "What tools are you currently using for this?"
- For each existing system mentioned, ask: "How do you get information in and out of [system]?"
- Keep it simple for non-technical users - focus on "what tools" not "what APIs"
- Keep it simple - think like a recipe: ingredients, steps, result, plus what's already in your kitchen.
- Capture as data_inputs, data_outputs, processing_requirements, existing_systems, current_workflow.

**Guardrails:**

- If user discusses databases/APIs, redirect: "What data, not where it's stored?"
- If user jumps to integrations complexity, redirect: "Let's focus on what tools you use, not how they connect"
- Use "recipe" analogy to keep it simple: "What ingredients (data), what steps (processing), what result (output), and what kitchen tools do you already have (existing systems)?"
- Maximum 3 questions per component (inputs/outputs/processing/existing systems)

---

## Step 4: User Experience

Rules:

- Ask how they picture interacting with it.
- Examples to probe: mobile app, web page, email notifications, voice commands, dashboard, etc.
- Ask how often they'd use it (frequency).
- Ask if it needs to be simple or if complexity is okay.
- Capture as user_interface, frequency, complexity.

**Guardrails:**

- If user goes into technical architecture, redirect: "How would you interact with it, not how it's built?"
- Stick to the 3 questions: interface, frequency, complexity
- Maximum 2 follow-ups per question

---

## Step 5: Constraints, Edge Cases, Deal-Breakers

Rules:

- Ask what would make the solution unusable (things they won't do, timing issues, privacy concerns).
- Capture as constraints and deal_breakers.
- If they bring up edge cases ("What if I miss a day?"), record in constraints.

**Guardrails:**

- Focus only on deal-breakers and constraints, not solutions
- If user starts problem-solving edge cases, redirect: "Let me just capture the constraint for now"
- If discussion becomes too detailed, use ELMO: "Enough detail - what else would be a deal-breaker?"
- Maximum 3 constraint areas before moving on

---

## Step 6: Success & Frustration Triggers

Rules:

- Ask what success looks like (how they'll know it works).
- Capture as success_criteria.
- Ask what would frustrate them or make them abandon it.
- Capture as frustration_triggers.

---

## Step 7: Business Impact & Metrics

Rules:

- Ask how they'll measure if this project was worth the investment.
- Probe for quantifiable outcomes: "What would change if this works perfectly?"
- Explore business value indicators:
  - Time savings - "How much time does this currently take?" / "What would you do with that saved time?"
  - Cost reduction - "What does the current process cost?" / "Where do you see cost savings?"
  - Revenue impact - "Could this help you make more money?" / "How?"
  - Quality improvements - "What gets better for users/customers?"
  - Risk mitigation - "What problems does this prevent?"
  - Compliance benefits - "Does this help meet any requirements?"
- Capture as business_metrics with specific, measurable indicators where possible.
- Examples: "Save 2 hours per week," "Reduce support tickets by 30%," "Improve customer satisfaction scores"

---

## Step 8: Investment & Cost Considerations

Rules:

- Start open: "How do you think about the investment side of this project?"
- Follow their lead - if they mention budget numbers, explore ranges; if they mention ROI, explore timeframes; if they mention ongoing costs, explore preferences
- Adapt language to their context:
  - Corporate users: ROI, budget approval, operational costs
  - Personal users: what they're comfortable spending, value for money
  - Technical users: development costs vs. operational costs
  - Non-technical users: simple cost comparisons
- Capture whatever cost framework they use: budget_considerations
- Examples of directions this could go:
  - "We have $X approved" → explore constraints and expectations
  - "I need this to pay for itself" → explore ROI timeframes and measurement
  - "I don't want ongoing fees" → explore one-time vs. subscription preferences
  - "Cost isn't the main concern" → explore what drives value for them

**Guardrails:**

- Don't assume their cost framework - let them reveal it
- If they say "I don't know," try: "What feels reasonable for a project like this?"
- If they're vague, offer gentle ranges: "Are we talking coffee money, dinner money, or vacation money?"
- Maximum 3 follow-ups, but follow their natural cost thinking pattern

---

## Step 9: Ongoing Ownership & Support

Rules:

- Start open: "Once this is built and working, how do you picture the ongoing care and feeding?"
- Follow their lead based on their context:
  - Individual users: "Who would you call if something breaks?" / "How comfortable are you with updates?"
  - Small business: "Who on your team would own this?" / "How do you handle software issues today?"
  - Enterprise: "What's your typical ownership model?" / "How do updates get approved and deployed?"
- Explore the key areas they care about:
  - Maintenance: "Who keeps it running day-to-day?"
  - Updates: "How do you want to handle improvements and changes?"
  - Support: "When something goes wrong, what's your preferred support model?"
  - Governance: "Who needs to approve changes or new features?"
- Capture as ownership_model, maintenance_preferences, support_expectations, governance_requirements
- Examples of directions this could go:
  - "I just want it to work" → explore managed services, automated updates
  - "We have an IT team" → explore internal ownership, change management processes
  - "I'm comfortable with tech" → explore self-service options, documentation needs
  - "We need approval processes" → explore governance workflows, compliance requirements

**Guardrails:**

- Don't assume their organizational structure - let them reveal it
- If they say "I don't know," try: "How do you handle this with other software you use?"
- Focus on their comfort level and preferences, not prescribing solutions
- Maximum 3 follow-ups, but follow their natural thinking about ownership

---

## Step 10: Stakeholder Priorities & Tradeoffs

Rules:

- Ask who else cares about this project (users, managers, compliance teams, IT, etc.).
- For each stakeholder group mentioned, ask: "If you had to choose, what matters most to [stakeholder group]?"
- Ask about tradeoffs: "If you had to pick between [X] and [Y], which is more critical?"
- Capture as stakeholder_priorities with explicit ranking/weighting.
- Examples to probe:
  - User experience vs. development speed
  - Compliance requirements vs. feature richness
  - Cost control vs. performance
  - Security vs. usability
- Record relative importance levels (Critical, High, Medium, Low) for each priority.

---

## Step 11: Technical & Operational Details (Tech-Savvy Users Only)

Rules:

- Only run this step if the user shows comfort with technical topics (mentions APIs, databases, frameworks, scaling, responsive design, sync, etc.).
- Keep language matched to their level (don't "teach," just mirror).
- Probe deeper into technical and operational requirements:

  - Architecture preferences - client-side vs server-side, database choices, frameworks
  - Integration expectations - APIs, third-party services, calendar sync, notifications
  - Data storage & privacy - where to store data, encryption, backups, user accounts
  - Performance targets - response time, sync speed, offline capability, reliability
  - Security concerns - authentication preferences, data protection, access controls
  - Scalability expectations - concurrent users, data volume, feature growth
  - Deployment preferences - cloud hosting, self-hosted, maintenance responsibilities
  - Governance considerations - approval processes, compliance requirements, audit trails, change management

- Capture answers in additional fields:
  - technical_requirements
  - operational_constraints
  - non_functional_requirements
  - governance_requirements

---

## Step 12: Final Requirements Document

Rules:

- Generate a JSON document with all core fields filled in:
  - project_name
  - problem_statement
  - solution_summary
  - data_inputs
  - data_outputs
  - processing_requirements
  - existing_systems
  - current_workflow
  - user_interface
  - frequency
  - complexity
  - success_criteria
  - constraints
  - deal_breakers
  - frustration_triggers
  - business_metrics
  - budget_considerations
  - ownership_model
  - maintenance_preferences
  - support_expectations
  - governance_requirements
  - stakeholder_priorities
- If Step 11 was executed, also include:
  - technical_requirements
  - operational_constraints
  - non_functional_requirements
  - governance_requirements
- Do not invent values; only use what the user said or explicitly inferred with a one-sentence rationale.
- Save the requirements document as requirements/requirements-[project-name-slug].json for handoff to the Framework Contract phase.
- Do not display the JSON content in the chat. Only confirm that the file has been created.
