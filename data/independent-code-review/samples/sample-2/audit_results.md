# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | The PR targets the 'main' branch and a review is completed before merge as shown by 'status: Merged'... |
| CR-02 | RuleType.Blocking | PASS | The reviewer '.ashernet' is independent and is not the author 'bartlomieju', fulfilling the four-eye... |
| CR-03 | RuleType.Blocking | PASS | The review is recorded in the system and status checks are passing as noted in Evidence Item 2. |
| TEST-01 | RuleType.Blocking | MISSING_EVIDENCE | There is no information regarding unit test coverage for new code. |
| TEST-02 | RuleType.Blocking | MISSING_EVIDENCE | There is no information about integration test coverage for critical integration points. |
| TEST-03 | RuleType.Blocking | MISSING_EVIDENCE | There is no information about line coverage for critical security/payment/authentication paths. |
| TEST-04 | RuleType.Blocking | MISSING_EVIDENCE | No information confirming that coverage reports are attached to the code review. |
| TEST-05 | RuleType.Blocking | MISSING_EVIDENCE | No evidence regarding branch coverage percentage provided. |
| TEST-06 | RuleType.Blocking | MISSING_EVIDENCE | No evidence regarding function coverage percentage provided. |
| TEST-07 | RuleType.Blocking | MISSING_EVIDENCE | No evidence provided about unit tests passing before release/merge. |
| TEST-08 | RuleType.Blocking | MISSING_EVIDENCE | No evidence provided regarding the passing status of integration tests. |
| TEST-09 | RuleType.Blocking | MISSING_EVIDENCE | No information on critical end-to-end user journeys related to the change. |
| TEST-10 | RuleType.Blocking | MISSING_EVIDENCE | No data on whether the change affects performance or performance tests are applicable. |
| TEST-11 | RuleType.Blocking | MISSING_EVIDENCE | No information about security scans being run and approved for this PR. |
| TEST-12 | RuleType.Blocking | MISSING_EVIDENCE | No evidence' about CI/CD pipeline being executed in a clean environment. |
| TEST-13 | RuleType.Blocking | PASS | All status checks are passing as indicated by the 'status_checks_passing: true' in Evidence Item 2. |
| TEST-14 | RuleType.Blocking | MISSING_EVIDENCE | No information on flaky tests or their resolution provided. |
| TQ-01 | RuleType.Audit | NOT_APPLICABLE | This is an audit rule and evidence provided does not address it directly. |
| TQ-02 | RuleType.Audit | NOT_APPLICABLE | This is an audit rule and evidence provided does not address it directly. |
| TM-01 | RuleType.Audit | NOT_APPLICABLE | This is an audit rule and evidence provided does not address it directly. |
| POLICY-01 | RuleType.Audit | NOT_APPLICABLE | This is an audit rule for policy review and not directly applicable to the PR or test evidence. |

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
  "author_username": "bartlomieju",
  "reviewer_usernames": [
    ".ashernet"
  ],
  "status": "Merged",
  "base_branch": "main",
  "status_checks_passing": true,
  "_source": "Screenshot 2025-11-14 at 14-32-05 feat use Node.js timers by default by bartlomieju \u00b7 Pull Request #31272 \u00b7 denoland_deno.png"
}
```