# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | The PR targets the 'main' branch and is marked as 'merged'. A code review was completed since the st... |
| CR-02 | RuleType.Blocking | PASS | The review was conducted by 'RyanCavanaugh' and 'Copilot', neither of whom is the author 'jakebailey... |
| CR-03 | RuleType.Blocking | PASS | Given the PR is merged and has status checks passing, it can be assumed that review approvals were r... |
| TEST-01 | RuleType.Blocking | NOT_APPLICABLE | There is no evidence provided that new code is included, therefore this rule is not applicable. |
| TEST-02 | RuleType.Blocking | NOT_APPLICABLE | There is no evidence provided of integration points changes or files requiring integration coverage. |
| TEST-03 | RuleType.Blocking | NOT_APPLICABLE | No specific mention or evidence of changes to critical security/payment/authentication paths. |
| TEST-04 | RuleType.Blocking | PASS | The evidence indicates coverage testing was performed and successful, implying that the coverage rep... |
| TEST-05 | RuleType.Blocking | PASS | Branch coverage is reported at 89.48%, exceeding the 70% minimum threshold. |
| TEST-06 | RuleType.Blocking | PASS | Function coverage is reported at 94.79%, exceeding the 80% minimum threshold. |
| TEST-07 | RuleType.Blocking | PASS | CI pipeline overall status is 'Success' and all status checks are passing, indicating unit tests pas... |
| TEST-08 | RuleType.Blocking | PASS | Integration tests are marked as 'Success' in the CI pipeline and all status checks are passing. |
| TEST-09 | RuleType.Blocking | NOT_APPLICABLE | There is no evidence or mention of changes affecting critical end-to-end user journeys. |
| TEST-10 | RuleType.Blocking | NOT_APPLICABLE | No evidence of performance impacts or performance test applicability in provided evidence. |
| TEST-11 | RuleType.Blocking | PASS | Security scans were part of the CI stages and marked as successful, indicating they have been review... |
| TEST-12 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-13 | RuleType.Blocking | PASS | Status checks passing imply visibility of test results as PR status checks. |
| TEST-14 | RuleType.Blocking | NOT_APPLICABLE | No indication of flaky tests in the provided evidence. |
| TQ-01 | RuleType.Audit | NOT_APPLICABLE | No evaluation generated |
| TQ-02 | RuleType.Audit | NOT_APPLICABLE | No evaluation generated |
| TM-01 | RuleType.Audit | NOT_APPLICABLE | No indication of flaky tests in the provided evidence. |
| POLICY-01 | RuleType.Audit | NOT_APPLICABLE | No evaluation generated |

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
    "src/compiler/_namespace_mono.ts",
    "src/compiler/_namespace_all.ts",
    "src/compiler/binder.ts",
    "src/compiler/builder.ts",
    "src/compiler/builderPublic.ts",
    "src/compiler/builderState.ts",
    "src/compiler/builderStatePublic.ts",
    "src/compiler/checker.ts",
    "src/compiler/commandLineParser.ts",
    "src/compiler/core.ts",
    "src/compiler/corePublic.ts",
    "src/compiler/debug.ts",
    "src/compiler/diagnosticInformationMap.generated.ts",
    "src/compiler/emitter.ts",
    "src/compiler/executeCommandLine.ts",
    "src/compiler/expressionTracer.ts",
    "src/compiler/factory/baseNodeFactory.ts",
    "src/compiler/factory/emitter.ts",
    "src/compiler/factory/emitterPublic.ts"
  ],
  "_source": "Screenshot 2025-11-14 at 14-27-50 Coverage Report.png"
}
```

### Evidence [2]: Screenshot 2025-11-14 at 14-28-31 Shrink relationComplexityError test size by jakebailey · Pull Request #62754 · microsoft_TypeScript.png
```json
{
  "platform": "GitHub",
  "pr_number": "62754",
  "author_username": "jakebailey",
  "reviewer_usernames": [
    "RyanCavanaugh",
    "Copilot"
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
  "pipeline_id": "#34653",
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
    "misc": "Success",
    "self-check": "Success",
    "baselines": "Success"
  },
  "environment": null,
  "has_warnings": false,
  "_source": "Screenshot 2025-11-14 at 14-29-21 Shrink relationComplexityError test size \u00b7 microsoft_TypeScript@9e76dd2.png"
}
```