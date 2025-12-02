# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | The PR targets the 'main' branch and has a completed code review, satisfying the rule. |
| CR-02 | RuleType.Blocking | PASS | The code review was completed by an independent reviewer 'dsherret', different from the PR author 'b... |
| CR-03 | RuleType.Blocking | MISSING_EVIDENCE | While the review was completed, there's no specific evidence that approvals are recorded in the syst... |
| TEST-01 | RuleType.Blocking | MISSING_EVIDENCE | The evidence does not provide information about unit test coverage for new code. |
| TEST-02 | RuleType.Blocking | MISSING_EVIDENCE | There's no evidence of integration test coverage for critical integration points or applicable excep... |
| TEST-03 | RuleType.Blocking | MISSING_EVIDENCE | No information is provided regarding the file paths or if critical security/payment/authentication p... |
| TEST-04 | RuleType.Blocking | MISSING_EVIDENCE | There's no evidence showing that coverage reports are attached to the code review. |
| TEST-05 | RuleType.Blocking | MISSING_EVIDENCE | No data provided regarding the branch coverage percentage. |
| TEST-06 | RuleType.Blocking | MISSING_EVIDENCE | No data provided regarding the function coverage percentage. |
| TEST-07 | RuleType.Blocking | MISSING_EVIDENCE | The evidence does not include specific results about unit tests with zero failures. |
| TEST-08 | RuleType.Blocking | MISSING_EVIDENCE | There's no indication of integration test results concerning the change. |
| TEST-09 | RuleType.Blocking | MISSING_EVIDENCE | No evidence that critical end-to-end user journeys affected by changes have passed. |
| TEST-10 | RuleType.Blocking | MISSING_EVIDENCE | Performance test relevance and results are not assessed in the present evidence. |
| TEST-11 | RuleType.Blocking | MISSING_EVIDENCE | There's no evidence of a security scan run, reviewed, or approved recorded. |
| TEST-12 | RuleType.Blocking | MISSING_EVIDENCE | The information given doesn't detail the CI/CD pipeline environment regarding cached dependencies. |
| TEST-13 | RuleType.Blocking | MISSING_EVIDENCE | The evidence doesn't confirm the visibility of test results as PR status checks. |
| TEST-14 | RuleType.Blocking | MISSING_EVIDENCE | There's no information concerning flaky tests or rectification efforts provided in the evidence. |
| TQ-01 | RuleType.Audit | NOT_APPLICABLE | This rule is categorized as an audit and doesn't block the merging process. |
| TQ-02 | RuleType.Audit | NOT_APPLICABLE | This rule is categorized as an audit and doesn't block the merging process. |
| TM-01 | RuleType.Audit | NOT_APPLICABLE | This is an audit measure not readily applicable to the immediate PR evaluation. |
| POLICY-01 | RuleType.Audit | NOT_APPLICABLE | This is a policy audit rule unrelated to the PR and its merging status. |

## Detailed Evidence Logs
Total Evidence Items Processed: 2

### Evidence [1]: Screenshot 2025-11-14 at 14-31-38 feat use Node.js timers by default · denoland_deno@12cde71.png
```json
{
  "pipeline_id": "31722",
  "overall_status": "Success",
  "stage_statuses": {
    "pre-build": "Success",
    "build libs": "Success",
    "publish canary": "Success"
  },
  "environment": null,
  "has_warnings": true,
  "_source": "Screenshot 2025-11-14 at 14-31-38 feat use Node.js timers by default \u00b7 denoland_deno@12cde71.png"
}
```

### Evidence [2]: Screenshot 2025-11-14 at 14-32-05 feat use Node.js timers by default by bartlomieju · Pull Request #31272 · denoland_deno.png
```json
{
  "platform": "GitHub",
  "pr_number": "31272",
  "author_username": "bartlomiej",
  "reviewer_usernames": [
    "dsherret"
  ],
  "status": "Merged",
  "base_branch": "main",
  "status_checks_passing": true,
  "_source": "Screenshot 2025-11-14 at 14-32-05 feat use Node.js timers by default by bartlomieju \u00b7 Pull Request #31272 \u00b7 denoland_deno.png"
}
```