# Discovery Contract - Requirements Gathering Phase

This contract defines the 13 steps the AI must follow for systematic requirements gathering.

## Contract Enhancement Methodology

This contract has been refined using a proven **Open-Ended Discovery Pattern** that successfully integrates new discovery areas without creating scope creep. When enhancing existing steps or adding new discovery dimensions, follow this methodology:

### The Open-Ended Discovery Pattern

1. **Start Open** - Begin with broad, approachable questions that don't assume user sophistication level

   - Example: "Help me understand the size of what we're dealing with" vs "What's your expected transaction volume?"

2. **Follow Their Lead** - Adapt questioning based on their responses and revealed context

   - If they mention specific numbers → explore daily vs. peak volumes
   - If they say "not much" → explore what that means to them
   - If they're uncertain → try relatable analogies

3. **Explore Naturally** - Use their language and mental framework to dig deeper

   - Mirror their terminology and sophistication level
   - Build on their examples and concerns
   - Let their priorities guide the direction

4. **Capture Systematically** - Map their natural responses to structured data fields

   - Transform conversational insights into JSON-ready requirements
   - Maintain the human context while creating machine-readable output

5. **Provide Examples** - Show different directions the conversation could go

   - Help other AIs understand the adaptive conversation patterns
   - Demonstrate various user types and response strategies

6. **Set Guardrails** - Prevent assumption-making and scope creep
   - Maximum follow-up limits per discovery area
   - Redirect techniques when conversations drift
   - Fallback questions for uncertain users

### Enhancement Strategy

- **Prefer Enhancement Over Addition** - When new discovery needs arise, first check if they can be naturally integrated into existing steps (see Steps 3, 4, 7 as examples)
- **Maintain Step Flow** - New discovery areas should feel like natural extensions of existing conversations, not abrupt topic changes
- **Test Across Personas** - Validate enhancements work for both technical and non-technical users
- **Document Patterns** - Update this methodology when new successful patterns emerge

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

**Execution Mode:**

Individual Step Mode: When instructed with "Step X only," execute only that step and output nothing beyond what the step specifies.
Full Contract Mode: When given a project request and instructed to "Follow the discovery contract," execute all applicable steps automatically (step-level conditional rules take priority) and respond only with:

- The project name from Step 1
- A brief summary from Step 2
- Confirmation that the requirements document was created

---

## Step 1: Problem & Project Identity

Rules:

- Start warm and conversational: "I'm excited to help you figure this out! What's the main thing that's bugging you that you'd like to solve?"
- Let them describe the problem naturally first
- As they talk, listen for natural project identifiers or suggest based on their language:
  - "It sounds like this is about [making invoices easier] - should we call it something like 'Invoice Helper' for now?"
  - "You keep mentioning [order tracking] - want to call this 'Order Tracker' or something like that?"
  - "What would you call this thing if you had to describe it to a friend?"
- If no name emerges naturally: "We'll need something to call this project - any ideas? Even something simple works."
- Adapt your tone to match theirs:
  - If they're casual: stay relaxed and friendly
  - If they're formal: be warm but professional
  - If they're excited: match their energy
  - If they're uncertain: be encouraging and patient
- Capture as problem_statement and project_name (in that order of priority)

**Guardrails:**

- Don't assume their communication style - let them set the tone
- If they give technical solutions, gently redirect: "I love that you're thinking about solutions! But first, what problem is that solving?"
- If they ramble, listen then guide: "I'm hearing a lot of good stuff - can you help me boil it down to the main thing?"
- Maximum 3 conversational exchanges to get the basics, then move naturally to Step 2

---

## Step 2: Current State & Context

Rules:

- Start open: "Help me understand how you're handling this today - what's your current reality?"
- Follow their lead to understand their world:
  - If they describe pain points: explore what's frustrating, what breaks, what takes too long
  - If they describe aspirations: explore what inspired this idea, what they've seen elsewhere
  - If they mention existing processes: explore what works, what doesn't, who's involved
  - If they're uncertain: try "Walk me through what a typical [day/week/situation] looks like with this stuff"
- Adapt language to their context:
  - Business users: current workflows, team processes, existing tools
  - Individual users: daily routines, current workarounds, personal frustrations
  - Technical users: current architecture, system limitations, integration challenges
- Explore their current state naturally:
  - Current process: "How do you handle this now?"
  - Inspiration sources: "What made you think about doing this project?"
  - Context clues: "Who else is involved?" / "When does this become important?"
- Capture as current_state, inspiration_context, stakeholders_involved
- Examples of directions this could go:
  - "I spend hours every week manually..." → explore time drains, repetitive tasks
  - "I saw this cool thing that..." → explore what attracted them, how it might apply
  - "Our team keeps running into..." → explore collaboration friction, communication gaps
  - "I've been thinking it would be nice if..." → explore the gap between current and desired state

**Guardrails:**

- Don't ask for solutions - focus purely on understanding their current reality and what brought them here
- If they jump to solution ideas, redirect: "That's interesting - what's happening now that makes you think about that?"
- If they describe technical implementations, redirect: "Help me understand the current situation that's driving this"
- Maximum 3 follow-ups to understand their current state and context

---

## Step 3: Data Flow, Volume & Existing Systems

Rules:

- Ask what information goes in (inputs).
- Ask what comes out (outputs).
- Ask what happens to the data in between (processing).
- Start open about scale: "Help me understand the size of what we're dealing with - is this a little bit of data or a lot?"
- Follow their lead on volume naturally:
  - If they mention specific numbers: explore daily vs. peak volumes
  - If they say "not much": explore what that means to them, seasonal changes
  - If they say "a lot": explore what feels overwhelming, when it gets busy
  - If they're uncertain: try "Think about your busiest day - how much would you be dealing with?"
- Ask about existing systems: "Where does this information live today?" / "What tools are you currently using for this?"
- For each existing system mentioned, ask: "How do you get information in and out of [system]?"
- Keep it simple for non-technical users - focus on "what tools" not "what APIs"
- Keep it simple - think like a recipe: ingredients, steps, result, plus what's already in your kitchen, and how much you're cooking for.
- Capture as data_inputs, data_outputs, processing_requirements, data_volume, performance_expectations, existing_systems, current_workflow.

**Guardrails:**

- Don't assume their scale - let them reveal their volume framework
- If they say "I don't know," try: "What's a busy day like for you with this stuff?"
- If user discusses databases/APIs, redirect: "What data, not where it's stored?"
- If user jumps to integrations complexity, redirect: "Let's focus on what tools you use, not how they connect"
- Use "recipe" analogy including scale: "What ingredients (data), what steps (processing), what result (output), how much are you cooking for (volume), and what kitchen tools do you already have (existing systems)?"
- Maximum 3 questions per component (inputs/outputs/processing/volume/existing systems)

---

## Step 4: User Experience & Accessibility

Rules:

- Start open: "How do you picture yourself using this day-to-day?"
- Follow their lead on interaction preferences, then explore accessibility needs naturally
- Adapt language to their context:
  - If they mention mobile: explore device preferences, screen size needs
  - If they mention desktop: explore workspace setup, multiple monitors
  - If they mention sharing: explore who else needs to use it
  - If they're uncertain: try "What's the easiest way for you to get things done usually?"
- Explore usage patterns naturally:
  - Frequency: "How often would you be using this?"
  - Context: "Where would you typically be when using this?"
  - Accessibility: "Are there any ways you prefer to interact with technology?" / "What makes software easy or hard for you to use?"
- Capture their natural interaction framework as user_interface, frequency, accessibility_preferences, usage_context
- Examples of directions this could go:
  - "I'm always on my phone" → explore mobile-first design, touch interfaces
  - "I need big buttons" → explore visual accessibility, simplicity preferences
  - "I share my computer" → explore multi-user scenarios, privacy needs
  - "I'm not great with technology" → explore simplicity requirements, help systems

**Guardrails:**

- Don't assume their accessibility needs - let them reveal what matters to them
- If they say "I don't know," try: "What's your favorite app or website to use? What makes it easy?"
- Maximum 3 follow-ups, but follow their natural thinking about how they like to interact with technology

---

## Step 5: Constraints, Edge Cases, Deal-Breakers

Rules:

- Start open: "What would make this solution completely unusable for you?"
- Follow their lead on what concerns them most:
  - If they mention time constraints: explore deadlines, availability windows
  - If they mention privacy concerns: explore what data feels sensitive, who can't see what
  - If they mention workflow disruption: explore what can't change, what must stay the same
  - If they're uncertain: try "What's absolutely non-negotiable in your world?"
- Adapt language to their context:
  - Individual users: personal preferences, lifestyle constraints, comfort zones
  - Business users: policy requirements, compliance needs, operational limits
  - Technical users: architectural constraints, integration limitations
- Capture as constraints, deal_breakers, edge_cases
- Examples of directions this could go:
  - "I can't share personal data" → explore privacy boundaries, data handling preferences
  - "We have compliance requirements" → explore regulatory constraints, audit needs
  - "I'm not available during work hours" → explore timing constraints, notification preferences
  - "It can't break our current process" → explore integration constraints, change limitations

**Guardrails:**

- Don't assume their risk tolerance - let them reveal what they're worried about
- If they say "I don't know," try: "What's gone wrong with similar projects before?"
- Focus only on constraints, not solutions - redirect problem-solving: "Let me just capture that concern for now"
- Maximum 3 constraint areas before moving on

---

## Step 6: Success & Frustration Triggers

Rules:

- Start open: "How will you know this project was a win for you?"
- Follow their lead on what success means to them:
  - If they mention specific outcomes: explore what those look like day-to-day
  - If they mention feelings: explore what creates those feelings
  - If they mention metrics: explore what numbers matter most
  - If they're uncertain: try "What would make you think 'this was totally worth it'?"
- Adapt language to their context:
  - Individual users: personal satisfaction, time saved, stress reduced
  - Business users: KPIs, team productivity, customer satisfaction
  - Technical users: performance metrics, system reliability, developer experience
- Explore their success framework naturally:
  - Success indicators: "What would you see happening that tells you it's working?"
  - Frustration triggers: "What would make you regret doing this project?"
  - Warning signs: "How would you know early if this was going off track?"
- Capture as success_criteria, frustration_triggers, warning_signs
- Examples of directions this could go:
  - "I'd have my evenings back" → explore time savings, work-life balance indicators
  - "Our customers would be happier" → explore satisfaction metrics, feedback signals
  - "No more emergency calls" → explore reliability indicators, peace of mind measures
  - "The team could focus on important stuff" → explore productivity indicators, strategic work time

**Guardrails:**

- Don't assume their success framework - let them reveal what matters
- If they say "I don't know," try: "Think about your best day with this working perfectly - what's different?"
- Focus on their outcomes, not prescribing metrics
- Maximum 3 follow-ups per area (success/frustration/warnings)

---

## Step 7: Growth & Future Considerations

Rules:

- Start open: "How do you think about the future of this project - will it stay the same or grow and change?"
- Follow their lead based on their response:
  - If they mention growth: explore what that looks like, what would need to change
  - If they say "just keep it simple": explore what would make them reconsider, what might force changes
  - If they mention other systems: explore future integration possibilities
  - If they're uncertain: try "What usually happens when something works well in your world?"
- Adapt language to their context:
  - Business users: growth, expansion, new locations, seasonal changes
  - Technical users: scaling, integration, technology evolution
  - Individual users: expanding use cases, sharing with others
- Capture their natural growth framework as growth_considerations
- Examples of directions this could go:
  - "We might expand to other departments" → explore what that would require
  - "I don't want it to get complicated" → explore what simplicity means to them
  - "Everything needs to integrate eventually" → explore future system landscape
  - "We're growing fast" → explore what breaks first, what needs to scale

**Guardrails:**

- Don't assume they want to scale - let them reveal their growth philosophy
- If they say "I don't know," try: "What's worked well for you when adopting new tools before?"
- Maximum 3 follow-ups, but follow their natural thinking about change and growth

---

## Step 8: Value & Impact Understanding

_Open-ended discovery approach:_
What value do you expect this to create?

_Follow-up areas (explore based on their response):_

- Success measurement (How will you know it's working?)
- Problem urgency (What happens without this?)
- Beneficiary impact (Who gets the most value?)

_Capture:_

- Core value proposition in their words
- Success indicators they care about
- Current pain points or opportunities
- Stakeholder benefit distribution

---

## Step 9: Investment & Cost Considerations

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

## Step 10: Ongoing Ownership & Support

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

## Step 11: Stakeholder Priorities & Tradeoffs

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

## Step 12: Technical & Operational Details (Tech-Savvy Users Only)

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

## Step 13: Final Requirements Document

Rules:

- Generate a JSON document with all core fields filled in:
  - project_name
  - problem_statement
  - solution_summary
  - data_inputs
  - data_outputs
  - processing_requirements
  - data_volume
  - performance_expectations
  - existing_systems
  - current_workflow
  - user_interface
  - frequency
  - accessibility_preferences
  - usage_context
  - success_criteria
  - constraints
  - deal_breakers
  - frustration_triggers
  - growth_considerations
  - business_metrics
  - budget_considerations
  - ownership_model
  - maintenance_preferences
  - support_expectations
  - governance_requirements
  - stakeholder_priorities
- If Step 12 was executed, also include:
  - technical_requirements
  - operational_constraints
  - non_functional_requirements
  - governance_requirements
- Do not invent values; only use what the user said or explicitly inferred with a one-sentence rationale.
- Save the requirements document as requirements/requirements-[project-name-slug].json for handoff to the Framework Contract phase.
- Do not display the JSON content in the chat. Only confirm that the file has been created.
