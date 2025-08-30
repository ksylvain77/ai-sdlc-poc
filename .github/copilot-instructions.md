# AI SDLC POC - Copilot Instructions

## Project Architecture

This is an **AI Project Inception System** that transforms user problems into complete, deployable software projects through a 5-phase pipeline: AI Discovery → Technology Decision → Project Generation → SDLC Automation → AI Orchestration.

**Core Concept**: Templates + AI Decision Engine = Dynamic Project Generation

- `templates/` contains reusable project scaffolds
- AI systems use these templates to generate context-appropriate projects
- Focus is MVP validation, not production software

## Key Development Principles

### Template-Driven Development

- All project types start from templates in `templates/`
- Templates are **scaffolds**, not complete implementations
- Use placeholder syntax: `[Description]` for AI to fill in
- Each template represents a pattern, not a specific solution

### AI-First Decision Making

- **Never assume technology choices** - always ask user first
- **Never assume project scope** - confirm MVP boundaries
- **Always ask specific clarifying questions** instead of broad assumptions
- Build **one working piece at a time**, validate, then continue

### Iterative Validation Approach

```
1. Understand user problem through conversation
2. Propose technology decisions with rationale
3. Generate minimal working solution
4. Validate with user before expanding
5. Iterate based on feedback
```

## File Structure Patterns

```
templates/
├── [project-type]-template.md     # Project scaffolds
├── github-templates/              # CI/CD and GitHub workflows
└── copilot-instructions-template.md  # AI agent instructions

copilot-instructions.md             # Project-specific AI guidelines
AI_PROJECT_INCEPTION_ROADMAP.md     # 5-phase development plan
```

## Development Workflow

### Feature Development

- Create feature branches following roadmap phases: `phase-1/discovery-engine`, `phase-2/tech-decisions`
- Update roadmap checkboxes as features complete: `- [x] Discovery Interview System`
- Merge phases only when MVP functionality is proven working

### Git Practices

- Standard branching with automated workflows
- Focus on MVP features before advanced functionality
- Each phase should be independently testable

### Template Creation Guidelines

- Use descriptive placeholder syntax: `[Step-by-step installation commands]`
- Include architecture sections for system design decisions
- Add verification steps for setup validation
- Reference the roadmap phases when creating new templates

## Critical Commands & Workflows

### Long-Running Processes

For servers/watch processes: use `> /dev/null 2>&1 &` with `isBackground=false` to background without opening new terminals

### File Management

- Read existing content before editing to understand context
- Never create multiple files without explicit approval
- Only create deliverables that were explicitly decided upon

## Integration Points

### AI Decision Engine Integration

Templates serve as input to AI systems that make technology stack decisions based on:

- User requirements and constraints
- Project complexity assessment
- Integration needs with existing systems

### SDLC Automation

Generated projects include automated:

- Git workflow setup
- CI/CD pipeline configuration
- Testing framework selection
- Deployment automation

## Success Criteria

- Generated projects work out-of-the-box
- Technology choices match user requirements
- Templates are reusable across different project types
- AI agents can navigate templates without human intervention

Focus on **proving the concept works** rather than building production-ready software.
