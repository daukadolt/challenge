from dotenv import load_dotenv
import base64
import asyncio
import json
from pathlib import Path
from baml_py import Image
from baml_client import b

load_dotenv()

cntrl_str = """
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

"""


async def main():
    # Check if control.json exists
    control_file = Path("control.json")

    if control_file.exists():
        print("Loading control from control.json...")
        from baml_client.types import Control

        with open(control_file, "r") as f:
            control_dict = json.load(f)
        control = Control(**control_dict)
        print(f"Loaded {len(control.rules)} rules from cache")
    else:
        print("Extracting control structure...")
        control = b.ExtractControl(cntrl_str)

        # Save to JSON using Pydantic's model_dump
        with open(control_file, "w") as f:
            json.dump(control.model_dump(), f, indent=2)

        print(f"Saved {len(control.rules)} rules to control.json")

    # Path to sample-1 images
    sample_dir = Path("data/independent-code-review/samples/sample-2")

    # Get all PNG files
    image_files = sorted(sample_dir.glob("*.png"))

    results = []

    # Process each image
    for image_path in image_files:
        print(f"\nProcessing: {image_path.name}")

        # 1. Convert image to base64
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        # 2. Run b.EvaluateImage
        img = Image.from_base64("image/png", encoded)
        res = b.EvaluateImage(img=img, control=control)

        results.append({"filename": image_path.name, "result": res})

    # 3. Combined output
    output_lines = []
    output_lines.append("=" * 80)
    output_lines.append("COMBINED RESULTS")
    output_lines.append("=" * 80)

    for idx, result in enumerate(results, 1):
        output_lines.append(f"\n[{idx}] {result['filename']}")
        output_lines.append("-" * 80)
        output_lines.append(str(result["result"]))

    combined_output = "\n".join(output_lines)

    # Print to console
    print("\n" + combined_output)

    # Write to file
    output_file = Path("results.txt")
    with open(output_file, "w") as f:
        f.write(combined_output)

    print(f"\n\nResults saved to: {output_file.absolute()}")

    return results


if __name__ == "__main__":
    asyncio.run(main())
