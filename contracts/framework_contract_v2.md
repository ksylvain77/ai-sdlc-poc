# Framework Contract v2 - Architecture Selection & Scaffolding Phase

**CORE OPERATING PRINCIPLE**: In Full Contract Mode, this contract produces documents as files, NOT as chat output. Only provide the specified summary response format.

This contract defines the 8 steps the AI must follow for systematic technology stack selection and project scaffolding, designed to work with the enhanced Discovery Contract outputs.

## Contract Design Philosophy

This contract uses the **Constraint-Driven Architecture Pattern** - systematically eliminating options based on real-world constraints before making technology choices, ensuring practical and implementable solutions.

### The Constraint-Driven Architecture Pattern

1. **Start with the Problem Reality** - Parse the rich requirements from Discovery Contract comprehensively
2. **Apply Progressive Constraints** - Use budget, existing systems, governance, and stakeholder priorities to narrow options
3. **Generate Viable Architectures** - Only propose architectures that survive constraint filtering
4. **Make Opinionated Choices** - Select specific technologies with clear reasoning
5. **Validate Against Success Criteria** - Ensure architecture delivers on discovered business value
6. **Plan for Real-World Ownership** - Consider maintenance, support, and governance from Day 1
7. **Generate Implementation-Ready Scaffold** - Complete project structure ready for development

## Execution Modes

**Individual Step Mode**: When instructed with "Step X only," execute only that step and output nothing beyond what the step specifies.

**Full Contract Mode**: When given requirements and instructed to "Follow the framework contract," execute all 8 steps automatically, then:

1. **Generate Technical Design Document**: Create docs/technical-design-document-[project-name-slug].md containing:

   - Complete architecture selection process and scoring rationale
   - Technology stack justification with constraint mapping
   - Business value analysis and ROI validation
   - Implementation planning and risk assessment
   - All architectural decisions and tradeoffs

2. **Generate Project Scaffold**: Create scaffolding/project-scaffold-[project-name-slug].md with implementation structure

3. **Provide ONLY Summary Response** (DO NOT OUTPUT DOCUMENT CONTENTS TO CHAT):

   ```
   ## **Following Framework Contract v2 - Full Contract Mode**

   **Selected Architecture**: [Architecture name from Step 4]
   **Selected Technology Stack**: [Technology stack from Step 5]
   **Business Value Validation**: [One-sentence summary from Step 6]
   **Confirmation**: Technical design document and project scaffold created successfully

   - Technical Design Document: docs/technical-design-document-[project-name-slug].md
   - Project Scaffold: scaffolding/project-scaffold-[project-name-slug].md
   ```

**CRITICAL CONTRACT RULE**: In Full Contract Mode, never output the contents of the Technical Design Document or Project Scaffold to the chat. Only create the files and provide the summary response above.

---

## Step 1: Requirements Analysis & Problem Model

**Purpose**: Detect project scale to guide process complexity, then parse the Discovery Contract JSON into a structured problem model and extract behavioral patterns that drive architecture decisions.

### Part A: Project Scale Detection

**CRITICAL: This determines the complexity of ALL subsequent steps**

**Scale Detection Rules**:

Analyze requirements JSON for scale indicators:

**Personal/Individual Indicators**:

- User volume: "personal use", "individual", "help me", "just for me"
- Budget signals: "free", "small cost", "no budget", "personal time"
- Complexity preferences: "simple", "easy", "no fiddly", "minimal setup"
- Language patterns: First person ("I need", "my workflow")

**Small Team Indicators**:

- User volume: "department", "team", "small group", "5-20 people"
- Budget signals: "moderate budget", "departmental funding"
- Collaboration needs: "shared access", "team workflow"

**Enterprise Indicators**:

- User volume: "organization", "company-wide", "hundreds of users"
- Budget signals: "enterprise budget", "significant investment"
- Compliance needs: "governance", "audit", "compliance"
- Integration complexity: Multiple existing systems

**Scale Classification**: Count indicators and classify as Personal/Small Team/Enterprise

**Scale-Based Process Adjustments**:

- **Personal**: Simplified constraint analysis, 2 architecture options max, scaffold only
- **Small Team**: Moderate complexity, 2-3 options, scaffold with technical summary
- **Enterprise**: Full complexity, 3-4 options, complete technical design document

### Part B: Problem Dimension Analysis

**Rules**:

- Load and validate the complete requirements JSON from Discovery Contract
- Extract and organize information into 6 core problem dimensions:
  - **Business Context**: problem_statement, business_metrics, stakeholder_priorities
  - **Data & Processing**: data_inputs, data_outputs, processing_requirements, data_volume, performance_expectations
  - **User Experience**: user_interface, frequency, accessibility_preferences, usage_context
  - **Integration Reality**: existing_systems, current_workflow, integration constraints
  - **Operational Context**: ownership_model, maintenance_preferences, support_expectations, governance_requirements
  - **Growth & Sustainability**: growth_considerations, budget_considerations
- For each dimension, either quote directly from requirements or mark "INFERRED" with rationale
- If information is missing, make reasonable inferences based on project context and mark "INFERRED"

### Part B: Behavioral Pattern Analysis & Implementation Mapping

**Rules**:

- Analyze the Discovery JSON for behavioral insights that must shape solution design
- Extract patterns from these critical Discovery fields:
  - **failure_scenarios**: What causes user abandonment or system failure
  - **risks**: What concerns users about adoption or usage
  - **confidence_requirements**: What users need to trust and consistently use the system
  - **current_state**: What's currently broken or frustrating
  - **constraints**: User limitations and deal-breakers
- Translate behavioral insights into implementation patterns that address root causes
- Focus on HOW the solution should work, not WHAT technology to use

**Implementation Pattern Analysis**:

```
BEHAVIORAL INSIGHTS ANALYSIS:
- Adoption Barriers: [from failure_scenarios, risks - what prevents usage]
- Trust Requirements: [from confidence_requirements - what builds user confidence]
- Usage Constraints: [from constraints, current_state - what limits user capability]
- Failure Patterns: [from current_state, risks - what breaks down in current approach]

IMPLEMENTATION PATTERNS:
- Interaction Design: [how user should interact with solution based on constraints]
- Information Architecture: [how information should be organized based on usage patterns]
- Workflow Integration: [how solution fits into existing habits/processes]
- Adoption Strategy: [what implementation approach addresses adoption barriers]
```

**Output Format**:

```
BUSINESS CONTEXT:
- Core problem: [quoted from problem_statement]
- Success metrics: [from business_metrics]
- Key stakeholders: [from stakeholder_priorities with priority levels]

DATA & PROCESSING:
- Inputs: [from data_inputs]
- Processing: [from processing_requirements]
- Outputs: [from data_outputs]
- Volume/Performance: [from data_volume, performance_expectations]

USER EXPERIENCE:
- Interface preferences: [from user_interface, accessibility_preferences]
- Usage patterns: [from frequency, usage_context]

INTEGRATION REALITY:
- Existing systems: [from existing_systems]
- Current workflow: [from current_workflow]

OPERATIONAL CONTEXT:
- Ownership model: [from ownership_model]
- Support expectations: [from support_expectations]
- Governance needs: [from governance_requirements]

GROWTH & SUSTAINABILITY:
- Future considerations: [from growth_considerations]
- Budget framework: [from budget_considerations]

BEHAVIORAL INSIGHTS ANALYSIS:
- Adoption Barriers: [from failure_scenarios, risks - what prevents usage]
- Trust Requirements: [from confidence_requirements - what builds user confidence]
- Usage Constraints: [from constraints, current_state - what limits user capability]
- Failure Patterns: [from current_state, risks - what breaks down in current approach]

IMPLEMENTATION PATTERNS:
- Interaction Design: [how user should interact with solution based on constraints]
- Information Architecture: [how information should be organized based on usage patterns]
- Workflow Integration: [how solution fits into existing habits/processes]
- Adoption Strategy: [what implementation approach addresses adoption barriers]
```

**Guardrails**:

- Do not propose solutions or architectures in this step
- Focus on behavioral insights and implementation patterns, not specific technologies
- Make reasonable inferences when requirements are unclear, marking them as "INFERRED"
- Use project context to fill gaps rather than stopping execution
- Implementation patterns should address root behavioral causes, not just symptoms

---

## Step 2: Constraint Mapping & Deal-Breaker Analysis

**Purpose**: Systematically identify and categorize all constraints that will eliminate architecture options.

**Rules**:

- Parse all constraint sources from requirements:
  - **Hard Constraints**: deal_breakers, governance_requirements, existing_systems limitations
  - **Budget Constraints**: budget_considerations, cost sensitivity, ROI expectations
  - **Operational Constraints**: ownership_model, maintenance_preferences, support_expectations
  - **User Constraints**: accessibility_preferences, frustration_triggers, complexity tolerance
  - **Technical Constraints**: performance_expectations, data_volume, integration requirements
- Classify each constraint as:
  - **Exclusionary** (eliminates options entirely)
  - **Penalizing** (strong preference against)
  - **Preference** (mild steering influence)
- Create constraint hierarchy based on stakeholder_priorities
- Identify constraint conflicts and document tradeoff tensions

**Output Format**:

```
EXCLUSIONARY CONSTRAINTS (Architecture Eliminators):
- [constraint]: [quoted source] - [rationale]

PENALIZING CONSTRAINTS (Strong Preferences):
- [constraint]: [quoted source] - [impact on architecture choices]

PREFERENCE CONSTRAINTS (Mild Steering):
- [constraint]: [quoted source] - [influence direction]

CONSTRAINT CONFLICTS:
- [stakeholder A priority] vs [stakeholder B priority]: [tradeoff implications]

CONSTRAINT HIERARCHY:
1. [highest priority constraint source]
2. [second priority]
3. [etc.]
```

**Guardrails**:

- Quote from requirements whenever possible
- Don't dilute hard constraints into preferences
- Identify real conflicts rather than assuming they can all be satisfied
- Don't propose solutions yet - only map the constraint landscape

---

## Step 3: Architecture Option Generation

**Purpose**: Generate 2-4 viable architectures that could satisfy the problem model while respecting constraints.

**Rules**:

- Generate architectures that survive Step 2 constraint filtering
- For each architecture, describe:
  - **Core pattern** (monolith, microservices, serverless, client-server, etc.)
  - **Data flow approach** (how it handles inputs → processing → outputs from Step 1)
  - **Integration strategy** (how it works with existing_systems)
  - **User interaction model** (how it delivers the user_interface requirements)
  - **Operational characteristics** (deployment, maintenance, scaling)
- Explicitly note where each architecture strains against constraints
- Ensure architectural diversity - don't generate variations of the same pattern
- Connect each architecture back to the business context and success criteria

**Output Format**:

```
ARCHITECTURE OPTION A: [Name]
Core Pattern: [architectural pattern]
Data Flow: [how inputs → processing → outputs]
Integration: [how it works with existing systems]
User Interaction: [how users interact with it]
Operations: [deployment, maintenance approach]
Constraint Alignment: [how it satisfies major constraints]
Potential Weaknesses: [where it might struggle]

ARCHITECTURE OPTION B: [Name]
[same structure]

ARCHITECTURE OPTION C: [Name]
[same structure]

SUMMARY COMPARISON:
- Option A: [one-line strength/weakness]
- Option B: [one-line strength/weakness]
- Option C: [one-line strength/weakness]
```

**Guardrails**:

- Only generate architectures that could actually work given the constraints
- Don't recommend technologies yet - stay at architecture pattern level
- Be explicit about weaknesses and tradeoffs
- Ensure each option represents a genuinely different approach

---

## Step 4: Architecture Selection & Scoring

**Purpose**: Systematically evaluate architecture options and select the best fit using weighted criteria.

**Rules**:

- Score each architecture against weighted criteria derived from requirements:
  - **Constraint Compliance** (40% weight): How well does it respect exclusionary and penalizing constraints?
  - **Business Value Delivery** (25% weight): How effectively does it deliver on success_criteria and business_metrics?
  - **Operational Fit** (20% weight): How well does it match ownership_model and support_expectations?
  - **Stakeholder Satisfaction** (15% weight): How well does it serve stakeholder_priorities?
- Use 1-5 scoring scale with explicit rationale for each score
- Weight criteria based on stakeholder_priorities and business_metrics emphasis
- Calculate weighted scores and rank options
- Select winning architecture with clear reasoning about why it beat alternatives

**Output Format**:

```
SCORING CRITERIA (with weights):
1. Constraint Compliance (40%): [rationale for weight]
2. Business Value Delivery (25%): [rationale for weight]
3. Operational Fit (20%): [rationale for weight]
4. Stakeholder Satisfaction (15%): [rationale for weight]

ARCHITECTURE SCORING:

Option A - [Name]:
- Constraint Compliance: [score]/5 - [rationale]
- Business Value: [score]/5 - [rationale]
- Operational Fit: [score]/5 - [rationale]
- Stakeholder Satisfaction: [score]/5 - [rationale]
- Weighted Total: [calculated score]

Option B - [Name]:
[same scoring structure]

Option C - [Name]:
[same scoring structure]

SELECTED ARCHITECTURE: [winning option name]
SELECTION RATIONALE: [why this beat the others, referencing specific scores and requirements]
KEY TRADEOFFS ACCEPTED: [what we're giving up by choosing this option]
```

**Guardrails**:

- Use actual requirements data to justify scores, not generic reasoning
- Don't artificially inflate scores - be honest about weaknesses
- Clearly explain why weights were assigned as they were
- Address why lower-scoring options were rejected

---

## Step 5: Technology Stack Specification

**Purpose**: Map the selected architecture to specific technologies that respect all constraints and enable effective implementation.

**Rules**:

- Take the winning architecture from Step 4 and specify concrete technologies:
  - **Core Framework/Platform**: Primary development technology
  - **Data Layer**: Database, storage, caching solutions
  - **Integration Layer**: APIs, messaging, data connectors for existing_systems
  - **User Interface**: Frontend framework, mobile considerations, accessibility tools
  - **Infrastructure**: Hosting, deployment, monitoring based on operational_constraints
  - **Development Tools**: Build, test, deployment pipeline
- Ensure every technology choice respects exclusionary constraints from Step 2
- Justify each choice against budget_considerations and operational capabilities
- Prefer mature, well-supported technologies unless requirements demand cutting-edge
- Consider governance_requirements in technology selection (compliance, security, audit)

**Output Format**:

```
TECHNOLOGY STACK FOR: [selected architecture name]

CORE PLATFORM:
- Technology: [specific framework/platform]
- Rationale: [why this choice fits architecture + constraints]
- Budget Impact: [alignment with budget_considerations]

DATA LAYER:
- Database: [specific database technology]
- Storage: [file/object storage if needed]
- Caching: [caching solution if needed]
- Rationale: [why these choices support data requirements and constraints]

INTEGRATION LAYER:
- API Framework: [REST/GraphQL framework]
- Existing System Connectors: [specific integration approaches for existing_systems]
- Rationale: [how this enables required integrations]

USER INTERFACE:
- Frontend: [specific UI framework]
- Mobile: [mobile approach if needed]
- Accessibility: [specific accessibility considerations]
- Rationale: [how this delivers user_interface requirements]

INFRASTRUCTURE:
- Hosting: [specific hosting approach]
- Deployment: [CI/CD approach]
- Monitoring: [observability tools]
- Rationale: [how this matches operational_constraints and ownership_model]

DEVELOPMENT WORKFLOW:
- Build Tools: [build system]
- Testing: [testing framework]
- Code Quality: [linting, formatting tools]
- Rationale: [how this supports maintenance_preferences]
```

**Guardrails**:

- Every technology must have a clear rationale tied back to requirements
- No technology should violate exclusionary constraints from Step 2
- Consider total cost of ownership, not just development cost
- Specify versions/LTS considerations for stability

---

## Step 6: Business Value Validation

**Purpose**: Validate that the selected architecture and technology stack will actually deliver the business value identified in Discovery.

**Rules**:

- Map technology choices back to success_criteria and business_metrics
- Identify specific capabilities the stack provides to achieve each success criterion
- Validate against frustration_triggers - ensure stack won't create known problems
- Assess timeline to value delivery based on stack complexity and ownership_model
- Consider growth_considerations - will this stack scale with identified growth patterns?
- Validate cost-value alignment with budget_considerations

**Output Format**:

```
BUSINESS VALUE VALIDATION:

SUCCESS CRITERIA DELIVERY:
- "[success criterion 1]": How this stack delivers → [specific capability mapping]
- "[success criterion 2]": How this stack delivers → [specific capability mapping]
- "[success criterion 3]": How this stack delivers → [specific capability mapping]

FRUSTRATION PREVENTION:
- "[frustration trigger 1]": How this stack avoids → [specific mitigation]
- "[frustration trigger 2]": How this stack avoids → [specific mitigation]

VALUE TIMELINE:
- Time to first value: [estimate based on stack complexity]
- Time to full capabilities: [estimate for complete implementation]
- Rationale: [why these timelines are realistic given ownership_model and stack choice]

GROWTH ACCOMMODATION:
- "[growth consideration]": How stack scales → [specific scaling approach]

COST-VALUE ALIGNMENT:
- Development cost estimate: [rough order of magnitude]
- Operational cost estimate: [ongoing costs]
- Value justification: [how costs align with business_metrics and budget_considerations]
```

**Guardrails**:

- Base all validations on actual requirements data, not generic claims
- Be honest about timeline estimates - consider real-world implementation challenges
- Don't oversell capabilities - acknowledge limitations
- Consider total cost of ownership, not just initial development

---

## Step 7: Implementation Planning

**Purpose**: Define the development approach that respects operational constraints and ownership models.

**Rules**:

- Design implementation phases that deliver incremental value aligned with success_criteria
- Plan development approach based on ownership_model and technical capabilities
- Define deployment strategy that matches support_expectations and governance_requirements
- Plan for maintenance and evolution based on maintenance_preferences and growth_considerations
- Address integration with existing_systems in a phased, low-risk approach
- Define success measurements that align with business_metrics

**Output Format**:

```
IMPLEMENTATION APPROACH:

DEVELOPMENT PHASES:
Phase 1 - [name]: [deliverables] → [business value delivered]
Phase 2 - [name]: [deliverables] → [business value delivered]
Phase 3 - [name]: [deliverables] → [business value delivered]

DEPLOYMENT STRATEGY:
- Environment approach: [dev/staging/prod based on governance_requirements]
- Rollout method: [gradual/big-bang based on existing_systems integration]
- Rollback plan: [how to safely revert if issues arise]

INTEGRATION APPROACH:
- Phase 1: [minimal integration to validate concept]
- Phase 2: [expand integration based on existing_systems]
- Phase 3: [full integration ecosystem]

TEAM & SKILLS:
- Required capabilities: [what skills are needed]
- Ownership transition: [how ownership_model is established]
- Knowledge transfer: [documentation and training needs]

SUCCESS MEASUREMENT:
- Phase gates: [how to measure progress]
- Business metrics: [how to track business_metrics achievement]
- Technical metrics: [performance, reliability measures]
```

**Guardrails**:

- Phases must deliver genuine business value, not just technical milestones
- Integration approach must respect existing_systems constraints
- Don't assume unlimited technical capabilities - plan for actual ownership_model
- Success measurements must be actionable and tied to discovery requirements

---

## Step 8: Technical Design Document & Project Scaffold Generation

**Purpose**: Generate appropriate documentation and implementation-ready project scaffold based on project scale.

**CRITICAL: Apply Project Scale Classification from Step 1 scaling detection**

### Part A: Documentation Generation (Scale-Dependent)

**Documentation Rules Based on Project Scale**:

**Personal/Individual Projects**:

- **Skip Technical Design Document** - not needed for personal productivity tools
- **Generate Project Scaffold Only** - focus on setup and usage guide

**Small Team Projects**:

- **Generate Lightweight Technical Summary** - 1-2 page overview in project scaffold
- **Generate Project Scaffold** - includes technical summary section

**Enterprise Projects**:

- **Generate Full Technical Design Document** - complete architectural analysis
- **Generate Project Scaffold** - references Technical Design Document

**Technical Design Document Generation (Enterprise Projects Only)**:

**Rules**:

- Create docs/technical-design-document-[project-name-slug].md with complete architectural analysis
- Include all decision rationale, scoring, and tradeoffs from Steps 1-7
- Document technology stack justification against constraints and business value
- Provide implementation timeline and risk assessment
- Include architectural decision records (ADRs) with alternatives considered

**Technical Design Document Structure**:

```markdown
# Technical Design Document - [Project Name]

## Executive Summary

- Selected Architecture: [from Step 4]
- Technology Stack: [from Step 5]
- Business Value: [ROI and timeline from Step 6]
- Implementation Approach: [from Step 7]

## Requirements Analysis

[Complete Step 1 analysis]

## Constraint Analysis & Architecture Scoring

[Complete Steps 2-4 with scoring rationale]

## Technology Stack Selection

[Complete Step 5 with justification]

## Business Value & Implementation Planning

[Complete Steps 6-7 analysis]

## Architectural Decision Records

[Key ADRs with alternatives and rationale]

## Risk Assessment & Mitigation

[Implementation risks and mitigation strategies]

## Appendices

[Supporting analysis and references]
```

### Part B: Project Scaffold Generation

**Rules**:

- Generate minimal but complete scaffold for the selected stack from Step 5
- Include starter code that demonstrates the architecture pattern
- Include configuration for the complete technology stack
- Generate documentation that supports the ownership_model and maintenance_preferences
- Create deployment and operational scripts based on infrastructure choices
- Ensure scaffold addresses integration requirements with existing_systems
- Reference the Technical Design Document for architectural context

**Step 8 Deliverables (Scale-Dependent)**:

**Personal/Individual Projects**:

- **Project Scaffold Only**: Create scaffolding/project-scaffold-[project-name-slug].md
- **No Technical Design Document**: Skip enterprise documentation for personal tools

**Small Team Projects**:

- **Project Scaffold with Technical Summary**: Include lightweight technical overview section
- **No Separate Technical Design Document**: Integrate technical details into scaffold

**Enterprise Projects**:

- **Full Technical Design Document**: Create docs/technical-design-document-[project-name-slug].md containing:
  - Complete architectural analysis from Steps 1-7
  - Decision rationale with scoring and tradeoffs
  - Technology justification against constraints
  - Business value analysis and implementation timeline
  - Risk assessment and mitigation strategies
- **Project Scaffold**: Create scaffolding/project-scaffold-[project-name-slug].md with reference to Technical Design Document

**Project Scaffold Generation (All Scales)**:

- Complete project structure and starter code
- Step-by-step setup instructions
- Integration guidelines for existing systems
- Configuration reflecting discovered constraints

**CRITICAL: Implementation Scaling Rules**

Before generating the scaffold, determine the appropriate complexity level based on:

**Personal/Individual Projects** (1-5 users, personal productivity, learning):

- **Scaffold Size**: 1-2 pages maximum
- **Setup Complexity**: 5-10 minute setup, minimal configuration
- **File Structure**: Basic folder organization, avoid enterprise patterns
- **Documentation**: Quick start guide only, focus on immediate usage
- **Features**: Core functionality only, avoid "nice to have" features
- **Examples**: Simple scripts, basic templates, essential configs only

**Small Team Projects** (5-20 users, departmental tools, prototypes):

- **Scaffold Size**: 3-5 pages
- **Setup Complexity**: 15-30 minute setup, moderate configuration
- **File Structure**: Organized but not over-engineered, practical folders
- **Documentation**: Setup guide + basic usage, operational basics
- **Features**: Core functionality + 1-2 key productivity features
- **Examples**: Team workflows, basic automation, standard configs

**Enterprise Projects** (20+ users, business-critical, compliance needs):

- **Scaffold Size**: Comprehensive documentation
- **Setup Complexity**: Full enterprise setup with all considerations
- **File Structure**: Complete enterprise patterns and organization
- **Documentation**: Full technical documentation, operations guides
- **Features**: Full feature set, enterprise integrations, compliance
- **Examples**: Full application frameworks, comprehensive automation

**Scaling Determination**: Use these signals from requirements:

- **Personal Indicators**: "personal use", "individual", "help me", "just for me", small budget, simplicity emphasis
- **Team Indicators**: "department", "team", "collaborate", moderate budget, some operational needs
- **Enterprise Indicators**: "organization", "company-wide", "compliance", large budget, operational requirements

**MANDATORY SCALING DETECTION PROCESS**:

1. **Analyze Requirements for Scale Signals**:

   - Count user volume indicators: "personal", "individual", "me" vs "team", "department" vs "organization", "company"
   - Identify budget signals: "free", "small cost" vs "moderate budget" vs "large budget", "enterprise"
   - Check complexity tolerance: "simple", "easy", "no fiddly" vs "some complexity" vs "full features"
   - Assess operational capacity: "no dedicated ops", "minimal maintenance" vs "team support" vs "full operations"

2. **Apply Scaling Classification**:

   - **Personal/Individual**: If 3+ personal indicators OR budget is "free/small" OR explicit simplicity requirements
   - **Small Team**: If team indicators present AND moderate budget AND some operational capacity
   - **Enterprise**: If organization indicators OR compliance requirements OR large budget

3. **Generate Scaffold According to Classification**:
   - **Personal**: Maximum 2 pages, basic folder structure (3-4 folders max), 10-minute setup, essential features only
   - **Team**: 3-5 pages, organized structure (6-8 folders), 30-minute setup, core + productivity features
   - **Enterprise**: Full documentation, complete structure, comprehensive setup, all features

**SCALING ENFORCEMENT**: The scaffold MUST NOT exceed the complexity limits for the detected classification level.

**Project Scaffold Structure**:

```
/project-name/
├── docs/
│   ├── README.md (setup instructions, references Technical Design Document)
│   ├── ARCHITECTURE.md (technical overview summary)
│   └── BUSINESS_CONTEXT.md (success criteria, stakeholders)
├── src/ (application code structure)
├── config/ (configuration files)
├── deployment/ (infrastructure and deployment scripts)
├── tests/ (testing framework setup)
└── integration/ (existing system integration code)
```

**Guardrails**:

- Technical Design Document must capture complete decision rationale from all 8 steps
- Document must be enterprise-ready with clear tradeoff analysis and risk assessment
- Scaffold must be immediately implementable with the specified technology stack
- Don't include complex business logic in scaffold - focus on architecture demonstration
- Ensure all configuration reflects the constraints and requirements discovered
- Include clear documentation for the intended ownership_model
- Both documents must reference each other for complete project context

---

## Contract Testing Methodology

This contract should be tested using the same **Persona Simulation** approach used for Discovery Contract validation:

### Testing Process

1. **Load Requirements**: Use existing requirements JSON from Discovery Contract testing
2. **Execute Framework Contract**: Follow all 8 steps systematically
3. **Capture Decision Rationale**: Document why each architecture/technology choice was made
4. **Validate Business Alignment**: Confirm scaffold delivers on discovery success criteria
5. **Review with Personas**: Different personas evaluate if the technology choices make sense for their context

### Testing Focus Areas

- **Constraint Respect**: Does the process actually eliminate bad options based on constraints?
- **Business Value Delivery**: Will the scaffold deliver the discovered success criteria?
- **Operational Feasibility**: Can the proposed ownership model actually maintain this stack?
- **Integration Reality**: Does the integration approach work with existing systems?
- **Cost Alignment**: Do technology choices respect budget considerations?

### Success Criteria

- Architecture selection rationale clearly traces back to discovery requirements
- Technology stack respects all exclusionary constraints
- Scaffold is immediately implementable
- Business stakeholders would approve the technology choices
- Technical implementation delivers on success criteria

---

## Self-Validation Checklist

Before completing each step, verify:

- [ ] All decisions reference specific discovery requirements data
- [ ] Constraint compliance is explicitly validated
- [ ] Business value delivery is clearly mapped
- [ ] Operational feasibility is realistic
- [ ] Technology choices have clear rationale
- [ ] Integration approach respects existing systems
- [ ] Cost considerations are addressed
- [ ] Documentation supports intended ownership model
