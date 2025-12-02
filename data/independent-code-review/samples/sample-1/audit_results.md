# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | The PR targets the 'main' branch and has a completed code review before being merged, according to E... |
| CR-02 | RuleType.Blocking | PASS | The code review included approvals from reviewers who are not the author, satisfying the independent... |
| CR-03 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-01 | RuleType.Blocking | NOT_APPLICABLE | There is no specific evidence regarding new code and its unit test coverage in the provided evidence... |
| TEST-02 | RuleType.Blocking | NOT_APPLICABLE | No indication that integration points were changed in the provided evidence. |
| TEST-03 | RuleType.Blocking | PASS | The overall line coverage of 95.96% exceeds the requirement for critical paths and no specific menti... |
| TEST-04 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-05 | RuleType.Blocking | PASS | The branch coverage of 89.48% exceeds the minimum threshold of 70%. |
| TEST-06 | RuleType.Blocking | PASS | The function coverage of 94.79% exceeds the minimum threshold of 80%. |
| TEST-07 | RuleType.Blocking | PASS | All CI pipeline tests including unit tests passed successfully, and the status checks indicate no fa... |
| TEST-08 | RuleType.Blocking | NOT_APPLICABLE | There is no evidence that changes include integration points. All integration tests in CI also passe... |
| TEST-09 | RuleType.Blocking | NOT_APPLICABLE | There is no evidence of critical user journeys being affected. |
| TEST-10 | RuleType.Blocking | NOT_APPLICABLE | No evidence or flags indicate that performance changes are applicable or have been impacted. |
| TEST-11 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-12 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-13 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-14 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TQ-01 | RuleType.Audit | NOT_APPLICABLE | Test quality requirements are not mentioned within the evidence provided. |
| TQ-02 | RuleType.Audit | NOT_APPLICABLE | There is no evidence regarding test names or the inclusion of positive and negative cases. |
| TM-01 | RuleType.Audit | NOT_APPLICABLE | No information regarding tracking or fixing flaky tests is provided. |
| POLICY-01 | RuleType.Audit | NOT_APPLICABLE | Policy review status is not relevant or mentioned within the context of the given PR. |

## Detailed Evidence Logs
Total Evidence Items Processed: 3

### Evidence [1]: Screenshot 2025-11-14 at 14-27-50 Coverage Report.png
```json
{
  "tool_name": null,
  "overall_line_coverage": 95.96,
  "new_code_line_coverage": null,
  "branch_coverage": 89.48,
  "function_coverage": 94.79,
  "visible_files_tested": [
    "src/compiler/_namespace.ts",
    "src/compiler/_namespace11.ts",
    "src/compiler/_namespace17.ts",
    "src/compiler/binder.ts",
    "src/compiler/builder.ts",
    "src/compiler/builderPublic.ts",
    "src/compiler/builderState.ts",
    "src/compiler/builderState11.ts",
    "src/compiler/checker.ts",
    "src/compiler/commandLineParser.ts",
    "src/compiler/core.ts",
    "src/compiler/corePublic.ts",
    "src/compiler/debug.ts",
    "src/compiler/diagnosticInformationMap.ts",
    "src/compiler/emitter.ts",
    "src/compiler/executeCommandLine.ts",
    "src/compiler/expressionTree.ts",
    "src/compiler/factory/baseNodeFactory.ts",
    "src/compiler/factory/emitter.ts",
    "src/compiler/factory/emitter4.ts"
  ],
  "_source": "Screenshot 2025-11-14 at 14-27-50 Coverage Report.png"
}
```

### Evidence [2]: Screenshot 2025-11-14 at 14-28-31 Shrink relationComplexityError test size by jakebailey · Pull Request #62754 · microsoft_TypeScript.png
```json
{
  "platform": "GitHub",
  "pr_number": "62754",
  "author_username": "JakeBury",
  "reviewer_usernames": [
    "Copilot",
    "RyanCavanaugh"
  ],
  "status": "Merged",
  "base_branch": "main",
  "status_checks_passing": true,
  "_source": "Screenshot 2025-11-14 at 14-28-31 Shrink relationComplexityError test size by jakebailey \u00b7 Pull Request #62754 \u00b7 microsoft_TypeScript.png"
}
```

### Evidence [3]: Screenshot 2025-11-14 at 14-29-21 Shrink relationComplexityError test size · microsoft_TypeScript@9e76dd2.png
```json
{
  "pipeline_id": "345653",
  "overall_status": "Success",
  "stage_statuses": {
    "coverage": "Success",
    "lint": "Success",
    "knip": "Success",
    "format": "Success",
    "browser-integration": "Success",
    "typescheck": "Success",
    "smoke": "Success",
    "package-size": "Success",
    "mic": "Success",
    "self-check": "Success",
    "baselines": "Success"
  },
  "environment": null,
  "has_warnings": false,
  "_source": "Screenshot 2025-11-14 at 14-29-21 Shrink relationComplexityError test size \u00b7 microsoft_TypeScript@9e76dd2.png"
}
```