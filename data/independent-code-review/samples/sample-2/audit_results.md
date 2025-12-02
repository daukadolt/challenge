# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | Validated via evidence |
| CR-02 | RuleType.Blocking | PASS | Validated via evidence |
| COV-UNIT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-INTEG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-CRIT-PAYMENT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-CRIT-AUTH-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-CRIT-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-BRANCH-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-FUNC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| REPORT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-UNIT-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-INTEG-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-E2E-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-PERF-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| ENV-01 | RuleType.Blocking | PASS | Validated via evidence |
| PR-STATUS-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| FLAKY-BLOCK-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| FLAKY-AUD-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TEST-FAIL-FIX-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-MAINT-OBSO-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TEST-MAINT-QA-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| POLICY-REVIEW-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| BUG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| SMOKE-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |

## Detailed Evidence Logs

### Evidence [1]: Screenshot 2025-11-14 at 14-31-38 feat use Node.js timers by default · denoland_deno@12cde71.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the target branch or if a code review was performed."
  },
  {
    "rule_id": "CR-02",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the target branch or the code review approval status."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about code changes or unit test coverage."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about integration test coverage or if integration is affected."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "NA",
    "reasoning": "There is no information about payment feature being affected."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "NA",
    "reasoning": "There is no information about auth feature being affected."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "NA",
    "reasoning": "There is no information about security feature being affected."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about branch coverage."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about function coverage."
  },
  {
    "rule_id": "REPORT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about coverage report generation, attachment, or review."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the target branch or unit test results."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about integration test results or the target branch."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether critical user journeys are affected and end-to-end test results."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about performance requirements or test results."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the target branch or security scan review status."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about a merge attempt or the CI environment."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the PR status checks or if the PR is open."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about flaky tests or the target branch."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about existing flaky tests or their age/status."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the target branch or test failure count."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about obsolete tests or their status."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about test code or its quality."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about policy review frequency or the last reviewed date."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the target branch or open issues in the issue tracker."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether critical features are affected or if smoke tests are completed."
  }
]
```

### Evidence [2]: Screenshot 2025-11-14 at 14-32-05 feat use Node.js timers by default by bartlomieju · Pull Request #31272 · denoland_deno.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "PASS",
    "reasoning": "The PR targets the 'main' branch and a code review was performed since it has a reviewer assigned."
  },
  {
    "rule_id": "CR-02",
    "status": "PASS",
    "reasoning": "The PR targets the 'main' branch and has an approver (dsherret) who is not the author (bartlomieju) and presumably, the changes were approved as the PR was merged."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether code changes were made or the unit test coverage percentage."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether the PR affects integration or the integration test coverage percentage."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "NA",
    "reasoning": "No indication that the affected feature is 'payment' or the files related to 'payment' are changed."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "NA",
    "reasoning": "No indication that the affected feature is 'auth' or the files related to 'auth' are changed."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "NA",
    "reasoning": "No indication that the affected feature is 'security' or the files related to 'security' are changed."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether code changes were made or the branch test coverage percentage."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether code changes were made or the function test coverage percentage."
  },
  {
    "rule_id": "REPORT-01",
    "status": "NA",
    "reasoning": "PR is merged and not open, therefore this rule is not applicable."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the status of unit tests or the number of failures."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the status of integration tests."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether the PR affects critical user journeys or the status of E2E tests for critical journeys."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether the PR requires performance tests or if the performance benchmarks were met."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the approval status of the security scan."
  },
  {
    "rule_id": "ENV-01",
    "status": "PASS",
    "reasoning": "The PR was merged, indicating a merge attempt was likely successful. This implies the CI pipeline was run with a clean environment."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "NA",
    "reasoning": "PR is merged and not open, therefore this rule is not applicable."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the count of flaky tests."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "NA",
    "reasoning": "No information on the existence of flaky tests is provided."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the count of test failures."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the presence of obsolete tests and their status."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the quality of the test code."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "NA",
    "reasoning": "Irrelevant in the context of a pull request."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about open issues in the issue tracker with severity 'critical' or 'high'."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether the PR affects critical features or if manual smoke testing was completed."
  }
]
```