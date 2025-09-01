# AI SDLC Inception Template – Development Guide

## Development Standards

### Template Focus

1. This is a template for project inception, not a complex system
2. Focus on improving the two core contracts based on feedback
3. Simple & focused: Two contracts, get a scaffold, start building
4. Don't expand scope: No additional systems, just improve what we have

### Contract Refinement Process

1. Validate changes with real examples
2. Test contract improvements across complexity levels
3. Document clearly: Keep README and roadmap aligned with capabilities
4. When editing contracts, test with examples to ensure they still work
5. Keep contracts focused on inception phase only
6. Focus on making contracts more reliable and usable

### Git Workflow & Branching

- Use feature branches for contract refinements
- Current development on `phase-3/contract-refinement`
- Test contract changes with real examples before merging
- Merge improvements back to main when validated
- Update roadmap to reflect completed contract improvements
- Always do final `git add .` and `git status` check before committing

### Standard Git Commands

```bash
# Update roadmap first
# Then stage changes
git add .
git status  # verify staging
git commit -m "<descriptive message>"
git push
```

### Quality Assurance

- Execute contracts with example personas
- Validate output quality across different project types
- Test against proven examples:
  - PWA applications
  - Mobile applications
  - API-first architectures
  - Enterprise systems
  - Microservices implementations

### Testing Matrix

| Project Type  | Complexity | Personas        | Validation                   |
| ------------- | ---------- | --------------- | ---------------------------- |
| Task Manager  | Simple     | Business User   | Requirements JSON + Scaffold |
| Bill Reminder | Simple     | Technical User  | Complete Implementation      |
| Customer 360  | Complex    | Enterprise User | Architecture Decisions       |
| Mobile App    | Medium     | End User        | Technology Stack             |

### Code Review Guidelines

- Focus on contract reliability over feature expansion
- Ensure changes maintain template simplicity
- Validate that AI can execute contracts consistently
- Check that generated outputs meet quality standards
- Verify documentation stays aligned with capabilities

### Release Process

1. Complete contract improvements on feature branch
2. Test with multiple example scenarios
3. Update roadmap and documentation
4. Create PR to main with validation results
5. Merge after review and testing confirmation

### Technical Debt Management

- Prioritize contract consistency over new features
- Address feedback systematically through phases
- Keep scope within inception template boundaries
- Maintain clear separation between template and generated content

### Performance Considerations

- Optimize for AI execution efficiency
- Ensure contracts guide toward appropriate technology choices
- Maintain clear contract steps to prevent confusion
- Design for reliable reproduction across different AI systems

### Documentation Maintenance

- Keep README focused on user instructions
- Maintain roadmap alignment with actual progress
- Update examples when contract changes impact outputs
- Ensure copilot-instructions.md stays operational-focused
