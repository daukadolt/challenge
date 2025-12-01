// 1. Define types to distinguish between Merge Gates and Process/Audit checks
enum RuleType {
    Blocking @description(#"
        Rules that must pass immediately before a merge or release.
        Example: "All tests passed", "Coverage > 80%"
    "#)
    Audit @description(#"
        Maintenance or process rules that are measured over time, not per PR.
        Example: "Flaky tests fixed within 2 days", "Quarterly policy review"
    "#)
}

class Rule {
    // Added ID for easier tracking in logs/UI
    id string @description("Short identifier, e.g. 'TEST-01'")
    
    // Added type to solve the "Process vs Gate" risk
    type RuleType
    
    description string
    
    // Updated description to solve "Ambiguity" and "Critical Path" risks
    logic string @description(#"
        Propositional Logic. Be explicit with variable values.
        BAD: "CriticalPaths -> 100% Coverage"
        GOOD: "FilePath.contains('security', 'payment') -> Coverage == 100%"
    "#)
    
    exceptions string[] @description(#"
        List of specific scenarios where this rule can be skipped.
    "#)
}

class Control {
    name string
    description string
    rules Rule[]
}

function ExtractControl(control: string) -> Control {
    client "openai-responses/gpt-5-mini" 
    prompt #"
        Extract the control logic from the following content into a structured format.

        Guidelines for Extraction:
        1. **Atomic Rules**: Do not combine multiple thresholds into one logic string. 
           - IF the text says "Unit coverage 80% and Integration coverage 60%"
           - THEN create TWO separate rules.
        2. **Explicit Logic**: If the text defines a term (e.g., "Critical Paths are payment and auth"), use the explicit values ('payment', 'auth') in the logic string, not the abstract term.
        3. **Process vs Blocking**: Distinguish between rules that stop a release (Blocking) and rules regarding team habits/maintenance (Audit).

        Content:
        {{ control }}

        {{ ctx.output_format }}
    "#
}

test code_review_control {
    functions [ExtractControl]
    args {
        control #"
            # Independent Code Review
Changes are reviewed by an independent code reviewer prior to code being merged and released to production. Independent code review restricts the ability for anyone individual from taking a change production without involving an independent party (4-eyes principle).

## Control Attributes
* Code Reviews are performed prior to committing a change to the main branch
* Code Review approvals are performed by independent code reviewers
* Testing is performed in accordance with the testing policy

# Testing Policy

## Overview

This policy establishes minimum testing requirements for all code changes to ensure quality, reliability, and maintainability of the codebase.

## Minimum Test Coverage Requirements

### Code Coverage Thresholds

- **Unit Tests**: Minimum 80% code coverage for all new code
- **Integration Tests**: Minimum 60% coverage for critical integration points
- **Critical Paths**: 100% coverage required for security-sensitive, payment, and authentication flows
- **Legacy Code**: Existing code must maintain or improve current coverage levels

### Coverage Metrics

Coverage is measured using:
- Line coverage (primary metric)
- Branch coverage (minimum 70%)
- Function coverage (minimum 80%)

Coverage reports must be generated and reviewed as part of the code review process.

## Pre-Release Test Requirements

### Mandatory Test Execution

All code must pass the following test suites before release:

1. **Unit Tests**: All unit tests must pass with zero failures
2. **Integration Tests**: All integration tests must pass
3. **End-to-End Tests**: Critical user journeys must pass
4. **Performance Tests**: Performance benchmarks must be met (if applicable)
5. **Security Tests**: Security scan results must be reviewed and approved

### Test Execution Environment

- Tests must run in CI/CD pipeline before merge
- All tests must pass in a clean environment (no cached dependencies)
- Test results must be visible in pull request status checks
- Flaky tests must be fixed or removed before release

### Pre-Release Checklist

Before any release, the following must be verified:

- [ ] All automated tests pass
- [ ] Test coverage meets minimum thresholds
- [ ] No known critical or high-severity bugs
- [ ] Performance tests pass (if applicable)
- [ ] Security tests pass
- [ ] Manual smoke tests completed for critical features

## Test Quality Standards

### Test Requirements

- Tests must be deterministic and repeatable
- Tests must be independent and not rely on execution order
- Tests must clean up after themselves (no side effects)
- Test names must clearly describe what is being tested
- Tests must include both positive and negative test cases

### Test Maintenance

- Flaky tests must be fixed within 2 business days or removed
- Tests that fail must be fixed before code merge
- Obsolete tests must be removed or updated
- Test code quality must meet the same standards as production code

## Exceptions and Waivers

### Exception Process

The following types of changes may be exempt from this policy:

1. **Legacy Code Integration**: Changes that integrate with legacy systems where adding test coverage is technically impractical or would require significant refactoring of untested legacy code
2. **Third-Party Dependencies**: Changes that only involve configuration or integration with third-party libraries, services, or APIs that cannot be directly tested or mocked
3. **Proof of Concept / Experimental Features**: Experimental code, prototypes, or proof-of-concept implementations that are explicitly marked as temporary and not intended for production use
4. **Documentation-Only Changes**: Changes that only modify documentation, comments, README files, or non-executable configuration files
5. **Build and Deployment Scripts**: Changes to CI/CD pipelines, build scripts, deployment configurations, or infrastructure-as-code that don't affect application logic
6. **Dependency Updates**: Updates to dependencies, package versions, or third-party libraries where the change is limited to version bumps without functional modifications
7. **Refactoring with No Behavioral Changes**: Code refactoring that maintains exact functional behavior and is verified through existing test coverage

## Review and Updates

This policy is reviewed quarterly and updated as needed based on:
- Team feedback
- Industry best practices
- Project requirements
- Tooling improvements

---

**Last Updated**: 25/09/2025
**Policy Owner**: Engineering Leadership
**Review Frequency**: Quarterly

        "#
    }
}