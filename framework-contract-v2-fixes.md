# Framework Contract v2 - Fix Priority Checklist

## **Priority Order for Fixes**

### **1. Scale Detection Happens Too Late (FOUNDATIONAL)**

- **Why First**: This affects the complexity and depth of EVERY other step
- **Impact**: If we know it's a personal project, we shouldn't do enterprise-level constraint mapping or architecture scoring
- **Fix**: Move scale detection to Step 1, use it to adjust process depth throughout
- **Status**: [ ] Not Started

### **2. Implementation Patterns Lost in Translation (CRITICAL MISSING LINK)**

- **Why Second**: Step 1 Part B creates behavioral insights that should drive everything else, but they vanish
- **Impact**: We lose the human-centered design patterns that should eliminate inappropriate architectures
- **Fix**: Make implementation patterns explicit inputs to Step 3 architecture generation
- **Status**: [ ] Not Started

### **3. Constraint Filtering Isn't Actually Filtering (PROCESS ENFORCEMENT)**

- **Why Third**: Once we have scale and behavioral patterns, we need real constraint enforcement
- **Impact**: Without systematic elimination, we generate options that violate known deal-breakers
- **Fix**: Add explicit constraint validation gates in Step 3 - "Option X eliminated because..."
- **Status**: [ ] Not Started

### **4. Tech Stack Decision Timing (DECISION SEQUENCE)**

- **Why Fourth**: After fixing the filtering, we can address when specific technologies get chosen
- **Impact**: Currently locks in tech choices before validating they deliver business value
- **Fix**: Either move business validation before tech selection, or make them iterative
- **Status**: [ ] Not Started

### **5. Architecture vs Technology Boundary Blur (CLARITY)**

- **Why Fifth**: Once decision timing is fixed, we can clarify what happens when
- **Impact**: Prevents tech decisions from sneaking into architecture step disguised as patterns
- **Fix**: Define clear boundaries - Step 3 is pure patterns, Step 5 is specific technologies
- **Status**: [ ] Not Started

### **6. Business Value Validation Is Superficial (VALIDATION DEPTH)**

- **Why Last**: After all the systematic issues are fixed, improve the quality of validation
- **Impact**: Currently validates individual tech choices instead of overall solution approach
- **Fix**: Focus validation on architecture patterns and implementation approaches, not individual tools
- **Status**: [ ] Not Started

## **Why This Order Matters**

- **Scale Detection** affects every other step's complexity
- **Implementation Patterns** provide the missing bridge between human insights and technical decisions
- **Constraint Enforcement** makes the systematic filtering actually work
- **Decision Timing** ensures we validate before committing
- **Boundary Clarity** prevents premature technology lock-in
- **Validation Depth** improves quality after structure is fixed

## **Fix Strategy**

Starting with scale detection will immediately make the process more appropriate for different project types, then we can build proper systematic filtering on top of that foundation.

Each fix should be completed and tested before moving to the next one to avoid compounding issues.

## **Testing Approach**

After each fix:

1. Test with External Brain requirements (personal project)
2. Test with a team project example
3. Test with an enterprise project example
4. Validate that the fix doesn't break existing functionality

## **Original Issues Analysis**

### **The Core Meta-Problem:**

The contract tries to be systematic but doesn't actually enforce the system. We have great constraint mapping and behavioral analysis, but then we don't systematically use them to eliminate options. It's more like "documentation of decisions" than "systematic decision-making process."

**What feels wrong**: The process generates a lot of analysis but doesn't create forcing functions that actually constrain choices based on that analysis.
