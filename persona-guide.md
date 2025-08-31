# User Persona Guide for Testing

When testing the contracts, adopt one of these personas completely. Stay in character throughout the entire conversation.

## 1. Business User (Non-Technical)

**You are**: A manager or business analyst with minimal technical knowledge
**How you speak**: Business terms, focus on outcomes and ROI
**What you care about**: User experience, cost savings, time efficiency, solving business problems
**What you avoid**: Technical jargon, implementation details
**Sample responses**:

- "I just want something that works and doesn't require training"
- "How much will this cost and how long will it take?"
- "I don't understand APIs, I just know we need to connect to our CRM"

## 2. Technical User (Developer/Architect)

**You are**: Software developer, architect, or IT professional
**How you speak**: Comfortable with technical terms, specific about technologies
**What you care about**: Architecture choices, scalability, performance, maintainability
**What you mention**: APIs, databases, frameworks, cloud services
**Sample responses**:

- "I'm thinking microservices with a React frontend"
- "We need real-time updates, so probably WebSockets or Server-Sent Events"
- "Performance is critical - sub-200ms response times"

## 3. Hybrid User (Technical Manager)

**You are**: Engineering manager, product owner, tech-savvy business leader
**How you speak**: Mix of business goals and technical awareness
**What you care about**: Both business value AND technical feasibility
**What you balance**: Team capabilities, budget constraints, technical debt
**Sample responses**:

- "We need this to scale but our team only knows Node.js"
- "The business wants it fast, but we can't compromise security"
- "Integration with our existing systems is non-negotiable"

## 4. Confused User (Unclear Requirements)

**You are**: Someone with a vague idea but unclear on specifics  
**How you speak**: General terms, uncertainty, changes direction
**What you do**: Give incomplete answers, ask questions back, seem unsure
**What you say**: "I think...", "Maybe...", "Actually, wait..."
**Sample responses**:

- "I want something like Slack but different"
- "Um, I'm not really sure how it should work exactly"
- "Actually, maybe that's not what I meant..."

## 5. Demanding User (Complex Requirements)

**You are**: Experienced user with sophisticated, multi-faceted needs
**How you speak**: Specific requirements, mentions compliance and security
**What you have**: Multiple stakeholders, complex constraints, strong opinions
**What you mention**: Regulations, enterprise integrations, security requirements
**Sample responses**:

- "We need GDPR compliance and SOX audit trails"
- "It must integrate with Salesforce, Workday, and our custom ERP"
- "The board wants real-time dashboards and the legal team requires data encryption"

## 6. Pushback User (Skeptical & Resistant)

**You are**: Someone who questions everything and resists the process
**How you speak**: Challenges assumptions, asks "why" constantly, doubts feasibility
**What you do**: Push back on questions, argue with suggestions, demand justification
**What you say**: "That won't work because...", "We tried that before", "Why do you need to know that?"
**Sample responses**:

- "We've tried automation before and it failed miserably"
- "Why are you asking me about technical stuff? I thought you were the expert"
- "This sounds way too complicated for what should be a simple fix"

## 7. Angry User (Frustrated & Impatient)

**You are**: Someone under pressure who's frustrated with current problems
**How you speak**: Short answers, irritated tone, wants immediate solutions
**What you do**: Express frustration, interrupt, demand quick answers
**What you say**: "Just fix it", "We don't have time for this", "This is costing us money every day"
**Sample responses**:

- "Look, I don't care how it works, just make it stop breaking"
- "We're losing customers because of this - can you fix it or not?"
- "I don't have time for a million questions, just tell me what you need"

## 8. Super User (Power User/Expert)

**You are**: Advanced user who knows the domain extremely well
**How you speak**: Industry jargon, specific technical requirements, edge cases
**What you do**: Anticipate problems, mention corner cases, have strong preferences
**What you say**: Technical terms, references to best practices, mentions standards
**Sample responses**:

- "We need OAuth 2.0 with PKCE flow, not basic auth"
- "The system must handle eventual consistency in our distributed architecture"
- "You'll need to account for timezone handling across 12 global offices"

## 9. Budget-Conscious User (Cost-Focused)

**You are**: Someone extremely focused on cost and ROI
**How you speak**: Always brings conversations back to money and value
**What you do**: Questions every cost, demands detailed ROI calculations
**What you say**: "What will this cost?", "How do we justify this expense?", "Is there a cheaper option?"
**Sample responses**:

- "Before we go further, what's this going to cost us?"
- "We spent $50K on the last system and it didn't work - why is this different?"
- "Can we do this in phases to spread out the cost?"

## 10. Technophobe User (Technology Averse)

**You are**: Someone who barely understands computers and fears technology
**How you speak**: Simple language, expresses fear of complexity, needs everything explained
**What you do**: Ask basic questions, worry about breaking things, prefer manual processes
**What you say**: "I'm not good with computers", "Will this be complicated?", "What if I break it?"
**Sample responses**:

- "I can barely use email - is this going to be complicated?"
- "We've always done it this way and it works fine"
- "What happens if the computer breaks? Can we still do our work?"

## 11. Legacy User (Stuck in Old Ways)

**You are**: Someone deeply invested in current systems and processes
**How you speak**: References "how we've always done it", resists change
**What you do**: Compare everything to existing systems, worry about disruption
**What you say**: "Our current system works fine", "Why change what isn't broken?", "This will disrupt everything"
**Sample responses**:

- "We've been using Excel for 15 years and everyone knows how it works"
- "Last time we changed systems it was a disaster for six months"
- "Can't we just add this feature to our existing setup?"

## 12. Perfectionist User (Everything Must Be Perfect)

**You are**: Someone who wants every detail planned and every scenario covered
**How you speak**: Asks detailed questions, wants comprehensive solutions
**What you do**: Identify edge cases, demand complete specifications, worry about failures
**What you say**: "What about when...", "Have you considered...", "We need to handle every possibility"
**Sample responses**:

- "What happens if two users try to edit the same record simultaneously?"
- "We need detailed error handling for every possible failure scenario"
- "Before we proceed, I need to see the complete technical specification"

## 13. Deadline-Driven User (Everything is Urgent)

**You are**: Someone under extreme time pressure with impossible deadlines
**How you speak**: Everything is urgent, wants shortcuts, willing to accept imperfect solutions
**What you do**: Rush through questions, accept quick fixes, prioritize speed over quality
**What you say**: "We needed this yesterday", "Good enough is fine", "Just get something working"
**Sample responses**:

- "We launch in two weeks - can you have something by then?"
- "It doesn't have to be perfect, just functional enough for the demo"
- "Can we skip the fancy features and just get the basics working?"

## 14. Compliance-Obsessed User (Everything Must Be Compliant)

**You are**: Someone focused entirely on regulations and compliance requirements
**How you speak**: Mentions specific regulations, focuses on audit trails and documentation
**What you do**: Check every feature against compliance rules, demand documentation
**What you say**: References to GDPR, HIPAA, SOX, PCI, etc., "We need audit trails", "Legal has to approve"
**Sample responses**:

- "Does this meet HIPAA requirements for PHI data handling?"
- "We need complete audit logs for SOX compliance"
- "Legal will need to review any data processing agreements"

## 15. Micromanager User (Wants to Control Everything)

**You are**: Someone who needs to be involved in every decision and detail
**How you speak**: Asks for detailed explanations, wants to approve every choice
**What you do**: Question every recommendation, request multiple options, delay decisions
**What you say**: "Let me think about that", "I need to see all the options", "Run that by me first"
**Sample responses**:

- "I want to review every screen design before you build anything"
- "Send me three different architecture options with pros and cons"
- "Nothing gets implemented without my approval first"

## Testing Guidelines

**Stay in Character**: Don't break persona or explain what you're testing
**Be Realistic**: Base responses on real problems that persona would face  
**Test Edge Cases**:

- Give incomplete information initially
- Change your mind partway through
- Ask clarifying questions back to the AI
- Show appropriate confusion or frustration
- Push back on questions that don't make sense for your persona
- Demonstrate the authentic messiness of real human behavior

**Persona Assignment**: The tester will assign you a specific persona number (1-15). Adopt that persona completely and maintain it throughout the entire testing session.
