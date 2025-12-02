# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | Validated via evidence... |
| CR-02 | RuleType.Blocking | PASS | Validated via evidence... |
| COV-UNIT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-INTEG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-CRIT-PAYMENT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-CRIT-AUTH-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-CRIT-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-BRANCH-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-FUNC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| REPORT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-UNIT-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-INTEG-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-E2E-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-PERF-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| ENV-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| PR-STATUS-01 | RuleType.Blocking | PASS | Validated via evidence... |
| FLAKY-BLOCK-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| FLAKY-AUD-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TEST-FAIL-FIX-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TEST-MAINT-OBSO-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TEST-MAINT-QA-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| POLICY-REVIEW-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| BUG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| SMOKE-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |

## Detailed Evidence Logs

### Evidence [1]: Screenshot 2025-11-14 at 14-31-38 feat use Node.js timers by default · denoland_deno@12cde71.png
[
  {
    "rule_id": "CR-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information about the target branch or whether an independent code review was performed."
  },
  {
    "rule_id": "CR-02",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information about the target branch, approvers, or their independence from the author."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information about whether the changes contain code or the unit test coverage percentage."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not indicate if the PR affects integration points or the level of integration coverage."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not mention if the affected feature is related to payment or the line coverage percentage."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context lacks information on whether authentication flows are affected or the line coverage percentage."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no indication from the context if security-sensitive flows are involved or the line coverage percentage."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "No information is provided on code changes or branch coverage percentage."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "No details are available on code changes or function coverage percentage."
  },
  {
    "rule_id": "REPORT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether coverage reports were generated, attached, or reviewed."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context lacks unit test results or the target branch information."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "Integration test results and the target branch information are not provided in the context."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if critical user journeys are affected or the status of end-to-end tests."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no indication from the context of performance test requirements or benchmark compliance."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information on security scans review status or the target branch."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "Details about the merge attempt and whether tests ran in a clean CI environment are absent."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the visibility of status checks and test results."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the presence or absence of flaky tests for the main branch."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not indicate the presence or status of flaky tests."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context lacks information on test failures and the target branch."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "No information is provided on obsolete tests or their statuses."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no insight into test code existence or its quality metrics."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "No information is available on policy review frequencies or their last review dates."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not mention the target branch or the presence of critical or high-severity bugs."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "No information is provided on whether critical features are affected or if smoke tests are completed."
  }
]

### Evidence [2]: Screenshot 2025-11-14 at 14-32-05 feat use Node.js timers by default by bartlomieju · Pull Request #31272 · denoland_deno.png
[
  {
    "rule_id": "CR-01",
    "status": "PASS",
    "reasoning": "The PR targeting the 'main' branch had an independent code review performed by 'dsharlet', who is different from the author 'bartlomieju'."
  },
  {
    "rule_id": "CR-02",
    "status": "PASS",
    "reasoning": "An approval was provided by 'dsharlet', who is independent of the author 'bartlomieju'."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information provided about unit test code coverage percentages."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding whether the PR affects integration or the integration coverage percentage."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "NA",
    "reasoning": "No information suggests that the changes affect payment flows."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "NA",
    "reasoning": "No information suggests that the changes affect authentication flows."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "NA",
    "reasoning": "No information suggests that the changes affect security-sensitive flows."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information provided about branch coverage percentage for the code changes."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information provided about function coverage percentage for the code changes."
  },
  {
    "rule_id": "REPORT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There are no details provided about whether coverage reports have been generated and reviewed."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the unit test results or failure counts."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the integration test results."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR affects critical user journeys or the status of end-to-end tests."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether performance tests were applicable and their benchmarks met."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There are no details provided about a security scan review status."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether tests ran in a clean CI/CD environment before merging."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "PASS",
    "reasoning": "The status checks for tests and other checks are passing as the PR has been successfully merged."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the presence of flaky tests."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the existence or age of any flaky tests."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There are no details about any failing tests for the PR targeting the 'main' branch."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about obsolete tests and their statuses."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the quality of test code."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding when the testing policy was last reviewed."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about open issues, especially critical or high-severity bugs."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about critical features being affected or whether smoke tests were completed."
  }
]