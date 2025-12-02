# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| CR-02 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-UNIT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-INTEG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| COV-CRIT-PAYMENT-01 | RuleType.Blocking | PASS | Validated via evidence... |
| COV-CRIT-AUTH-01 | RuleType.Blocking | PASS | Validated via evidence... |
| COV-CRIT-SEC-01 | RuleType.Blocking | PASS | Validated via evidence... |
| COV-BRANCH-01 | RuleType.Blocking | PASS | Validated via evidence... |
| COV-FUNC-01 | RuleType.Blocking | PASS | Validated via evidence... |
| REPORT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-UNIT-RUN-01 | RuleType.Blocking | PASS | Validated via evidence... |
| TST-INTEG-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-E2E-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-PERF-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| TST-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| ENV-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| PR-STATUS-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| FLAKY-BLOCK-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| FLAKY-AUD-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TEST-FAIL-FIX-01 | RuleType.Blocking | PASS | Validated via evidence... |
| TEST-MAINT-OBSO-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TEST-MAINT-QA-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| POLICY-REVIEW-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| BUG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence foun... |
| SMOKE-01 | RuleType.Blocking | PASS | Validated via evidence... |

## Detailed Evidence Logs

### Evidence [1]: Screenshot 2025-11-14 at 14-27-50 Coverage Report.png
[
  {
    "rule_id": "CR-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether an independent code review was performed."
  },
  {
    "rule_id": "CR-02",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether at least one approval came from an approver independent of the author."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "Overall line coverage is provided, but no specific unit test coverage for the changed/new code is given."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "It is unclear if the PR affects integration points and what the integration coverage is."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "PASS",
    "reasoning": "There is no mention of being related to payment flows, and no payment files are visible in the tested list."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "PASS",
    "reasoning": "There is no mention of being related to authentication flows, and no authentication files are visible in the tested list."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "PASS",
    "reasoning": "There is no mention of being related to security-sensitive flows, and no security files are visible in the tested list."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "PASS",
    "reasoning": "The branch coverage is 89.48%, which meets the minimum requirement of 70%."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "PASS",
    "reasoning": "The function coverage is 94.79%, which meets the minimum requirement of 80%."
  },
  {
    "rule_id": "REPORT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether coverage reports have been generated, attached to the PR, or reviewed."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the pass status or failures of unit tests."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether integration tests have passed."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information indicating if the PR affects critical user journeys and the status of end-to-end tests for them."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the requirement or status of performance benchmarks."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on security scan review and approval status."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether tests were run in a CI/CD pipeline in a clean environment."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the visibility of test results and required status checks on the PR."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the presence of flaky tests."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about the existence, number, or status of flaky tests."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on failing tests requiring fixes."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on obsolete tests and their status."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "Details about the code quality of test code are missing."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information available regarding the review frequency or the last review date of the testing policy."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on open issues in the issue tracker."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether manual smoke tests were conducted for critical features."
  }
]

### Evidence [2]: Screenshot 2025-11-14 at 14-28-31 Shrink relationComplexityError test size by jakebailey · Pull Request #62754 · microsoft_TypeScript.png
[
  {
    "rule_id": "CR-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "CR-02",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  },
  {
    "rule_id": "BUG-01",
    "status": "NA",
    "reasoning": "The PR does not target the 'main' branch. Instead, it targets the 'microsct-limits' branch."
  }
]

### Evidence [3]: Screenshot 2025-11-14 at 14-29-21 Shrink relationComplexityError test size · microsoft_TypeScript@9e76dd2.png
[
  {
    "rule_id": "CR-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information about whether a code review was performed or if the target branch is 'main'."
  },
  {
    "rule_id": "CR-02",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information about the target branch, the code reviewer, or their approval status. Therefore, compliance cannot be determined for this rule."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context provides a 'coverage' status of 'Success', but does not specify the unit test coverage percentage or whether code changes contain new or changed code."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify whether integration points are affected or the specific integration test coverage percentage."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if the payment feature is affected or the specific line coverage percentage for payment flows."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if the authentication feature is affected or the specific line coverage percentage for authentication flows."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if security-sensitive flows are affected or the specific line coverage percentage required."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context provides a 'coverage' status of 'Success', but does not specify the branch coverage percentage."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context provides a 'coverage' status of 'Success', but does not specify the function coverage percentage."
  },
  {
    "rule_id": "REPORT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not indicate if the coverage report was generated, attached to the PR, or reviewed as part of the code review."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "PASS",
    "reasoning": "All unit test stages have a status of 'Success', and there are no failures reported in test results."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide specific details about integration test results, and whether they passed or failed."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if critical user journeys are affected or the status of end-to-end test executions."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if performance tests were required or their outcomes."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not contain details on any security scan reviews or approvals."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide information about whether the tests were run in a clean environment or if there was a merge attempt."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if the PR is open or if the status checks for tests and coverage are visible on the pull request."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if there are any flaky tests impacting the main branch."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide details on any existing flaky tests and their current status or age."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "PASS",
    "reasoning": "No failing tests are reported as the pipeline stage status indicates a 'Success' result across the board."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context lacks information on any obsolete tests and their current status."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not provide details about test code and its quality against production standards."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "No information is available regarding the policy review schedule and the last review date."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "The context does not specify if there are any open critical or high-severity bugs."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "PASS",
    "reasoning": "The 'smoke' stage's status is 'Success', indicating completion of required smoke tests for critical features."
  }
]