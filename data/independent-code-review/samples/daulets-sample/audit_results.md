# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | The PR is targeting the 'master' branch and the review status is marked as 'completed'. |
| CR-02 | RuleType.Blocking | PASS | An independent reviewer (p-e-w) has approved the PR; the author (red40maxxer) did not review their o... |
| CR-03 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-01 | RuleType.Blocking | NOT_APPLICABLE | Evidence does not explicitly state that the PR includes new code. The known line coverage reports do... |
| TEST-02 | RuleType.Blocking | NOT_APPLICABLE | No specific mention of integration points in the changes or any files indicating such in the path pr... |
| TEST-03 | RuleType.Blocking | FAIL | The rule requires 100% line coverage for critical paths (security/payment/auth). The overall line co... |
| TEST-04 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-05 | RuleType.Blocking | PASS | The branch coverage is 87.67%, surpassing the minimum threshold of 70%. |
| TEST-06 | RuleType.Blocking | PASS | The function coverage is 94.5%, surpassing the minimum threshold of 80%. |
| TEST-07 | RuleType.Blocking | NOT_APPLICABLE | The evidence does not provide information on the status of unit tests in the CI environment. |
| TEST-08 | RuleType.Blocking | NOT_APPLICABLE | There is no indication the PR includes changes to integration points. |
| TEST-09 | RuleType.Blocking | NOT_APPLICABLE | There is no information about changes affecting critical end-to-end user journeys. |
| TEST-10 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-11 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-12 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-13 | RuleType.Blocking | PASS | The status checks are reported as passing, indicating visibility of test results on the PR status. |
| TEST-14 | RuleType.Blocking | NOT_APPLICABLE | There is no information about flaky tests within the provided evidence. |
| TQ-01 | RuleType.Audit | NOT_APPLICABLE | No evaluation generated |
| TQ-02 | RuleType.Audit | NOT_APPLICABLE | No evaluation generated |
| TM-01 | RuleType.Audit | NOT_APPLICABLE | No information about flaky tests needing tracking or fixing. |
| POLICY-01 | RuleType.Audit | NOT_APPLICABLE | No evaluation generated |

## Detailed Evidence Logs
Total Evidence Items Processed: 2

### Evidence [1]: coverage_metrics.csv
```json
{
  "tool_name": null,
  "overall_line_coverage": 94.38,
  "new_code_line_coverage": null,
  "branch_coverage": 87.67,
  "function_coverage": 94.5,
  "visible_files_tested": [
    "src/auth/login_service.ts",
    "src/payment/processor.ts",
    "src/utils/date_formatter.ts",
    "src/components/button.tsx"
  ],
  "_source": "coverage_metrics.csv"
}
```

### Evidence [2]: perf_ optimize abliteration matrix op by red40maxxer · Pull Request #46 · p-e-w_heretic.pdf
```json
{
  "platform": "GitHub",
  "pr_number": "46",
  "author_username": "red40maxxer",
  "reviewer_usernames": [
    "p-e-w"
  ],
  "status": "Merged",
  "base_branch": "master",
  "status_checks_passing": true,
  "_source": "perf_ optimize abliteration matrix op by red40maxxer \u00b7 Pull Request #46 \u00b7 p-e-w_heretic.pdf"
}
```