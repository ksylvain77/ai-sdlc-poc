# AI SDLC Inception Template

Transform ideas into implementable software projects through structured AI conversations and automated scaffolding generation.

## What This Is

An **AI-powered project inception system** that uses structured contracts to systematically:

- Extract requirements from user conversations
- Make informed technology stack decisions
- Generate complete project scaffolds with starter code

**Think of it as**: A template you copy to start any new software project, then run two AI contracts to go from "I have an idea" to "I'm ready to build."

## How It Works

### 1. Discovery Contract (`discovery_contract_full.md`)

**8-step systematic requirements gathering:**

- Detects user technical sophistication automatically
- Adapts conversation depth accordingly
- Captures functional requirements, constraints, and success criteria
- Outputs structured JSON requirements document

### 2. Framework Contract (`framework_contract_full.md`)

**7-step architecture selection and scaffolding:**

- Analyzes requirements to recommend technology stack
- Makes opinionated architectural decisions with reasoning
- Generates complete project scaffold with directory structure
- Provides starter code examples and setup instructions

### 3. Ready-to-Build Project

You receive a complete project foundation ready for development.

## Proven At Multiple Complexity Levels

✅ **Simple PWA** (Plant watering reminder)  
✅ **Mobile App** (Medication tracker - React Native)  
✅ **API Service** (Bill reminder system - Node.js/Twilio)  
✅ **Enterprise Platform** (Customer-360 data fabric - Kafka/Java/K8s)

## Repository Structure

```
├── discovery_contract_full.md     # Requirements gathering contract
├── framework_contract_full.md     # Architecture selection contract
├── requirements/                  # Generated JSON requirements
├── scaffolding/                   # Generated project scaffolds
├── copilot-instructions.md        # AI agent guidelines
└── AI_PROJECT_INCEPTION_ROADMAP.md # Development phases
```

## Quick Start

1. **Copy this template** to start your new project
2. **Run Discovery Contract** with an AI assistant:

   - Load `discovery_contract_full.md`
   - Execute the 8-step requirements conversation
   - Save output as `requirements/requirements-[project-name].json`

3. **Run Framework Contract** with the requirements:

   - Load `framework_contract_full.md`
   - Execute the 7-step architecture selection
   - Receive complete project scaffold

4. **Start building** with your generated foundation

## What You Get

### Requirements Output

- Structured JSON with problem statement, solution summary, technical requirements
- User interface patterns and interaction flows
- Processing requirements and complexity assessment
- Success criteria and constraints

### Project Scaffold Output

- Complete directory structure for chosen technology stack
- Starter code files with implementation examples
- Configuration files (package.json, Dockerfile, etc.)
- Setup and deployment instructions
- Architecture documentation

## Example Outputs

**Simple Bill Reminder System:**

- Node.js/Express API structure
- Twilio integration setup
- SQLite database schema
- Cron job scheduling
- Basic HTML frontend

**Enterprise Customer-360 Platform:**

- Event-driven microservices architecture
- Apache Kafka + Debezium CDC setup
- Kubernetes deployment manifests
- Java domain aggregates
- Compliance and governance frameworks

## Key Features

- **Adaptive Conversations**: Automatically adjusts technical depth based on user sophistication
- **Opinionated Decisions**: Makes concrete technology choices rather than presenting endless options
- **Complete Scaffolding**: Generates working project structure, not just documentation
- **Multi-Stack Support**: Handles web apps, mobile apps, APIs, and enterprise platforms
- **Production-Ready Patterns**: Includes proper architecture, testing, and deployment considerations

## Development Philosophy

- **Template-Driven**: Reusable patterns over custom solutions
- **AI-First Decision Making**: Structured contracts guide technology choices
- **MVP Focus**: Gets projects started quickly with solid foundations
- **Simple & Focused**: Two contracts, get a scaffold, start building

## Current Status

**Phase 1 & 2 Complete**: Core contracts validated across multiple project types  
**Phase 3**: Contract refinement based on AI feedback analysis

This template is ready for use in its current form, with ongoing improvements planned for stakeholder prioritization, architectural decision records, business metrics integration, and governance considerations.

## Requirements

- AI assistant capable of following structured conversation contracts
- Basic understanding of software development concepts
- Ability to execute generated project setup instructions

## License

Open source template - copy, modify, and use for any project inception needs.
