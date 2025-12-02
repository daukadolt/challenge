# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| COV-UNIT-01 | RuleType.Blocking | PASS | Validated via evidence |
| COV-CRIT-PAYMENT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-CRIT-AUTH-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-CRIT-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-BRANCH-01 | RuleType.Blocking | PASS | Validated via evidence |
| COV-FUNC-01 | RuleType.Blocking | PASS | Validated via evidence |
| CR-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| CR-02 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| COV-INTEG-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| REPORT-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-UNIT-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-INTEG-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-E2E-RUN-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-PERF-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TST-SEC-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| ENV-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
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

### Evidence [1]: Screenshot 2025-11-14 at 14-27-50 Coverage Report.png
```json
[
  {
    "rule_id": "COV-UNIT-01",
    "status": "PASS",
    "reasoning": "Overall line coverage is 95.96%, which is above the required 80% for unit tests when code changes are present."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "NA",
    "reasoning": "There is no indication that the changes affect the 'payment' feature, and no file paths related to payment have been identified."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "NA",
    "reasoning": "There is no indication that the changes affect the 'auth' feature, and no file paths related to authentication have been identified."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "NA",
    "reasoning": "There is no indication that the changes affect the 'security' feature, and no file paths related to security have been identified."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "PASS",
    "reasoning": "Branch coverage is 89.48%, which is above the required 70% when code changes are present."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "PASS",
    "reasoning": "Function coverage is 94.79%, which is above the required 80% when code changes are present."
  }
]
```

### Evidence [2]: Screenshot 2025-11-14 at 14-28-31 Shrink relationComplexityError test size by jakebailey · Pull Request #62754 · microsoft_TypeScript.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "CR-02",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR contains code changes or the coverage percentage."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR affects integration or the coverage percentage."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR affects the 'payment' feature or includes 'payment' in its file path."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR affects the 'auth' feature or includes 'auth' in its file path."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR affects the 'security' feature or includes 'security' in its file path."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR contains code changes or the branch coverage percentage."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about whether the PR contains code changes or the function coverage percentage."
  },
  {
    "rule_id": "REPORT-01",
    "status": "NA",
    "reasoning": "The PR is closed (merged), so the requirement to have a coverage report reviewed while open does not apply."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether the PR affects critical user journeys or the status of E2E tests."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "NA",
    "reasoning": "There is no information indicating that performance tests were required."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information about CI pipeline status and environment."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "NA",
    "reasoning": "The PR is closed (merged), so visibility of status checks while open does not apply."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding the presence of any flaky tests in the PR."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "NA",
    "reasoning": "There is no information indicating any obsolete tests included."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on the presence and quality of tests within the PR."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information regarding policy review frequency and the last reviewed date."
  },
  {
    "rule_id": "BUG-01",
    "status": "NA",
    "reasoning": "The target branch is 'master' not 'main'. Rule does not apply."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on whether the PR affects critical features or the status of manual smoke tests."
  }
]
```

### Evidence [3]: Screenshot 2025-11-14 at 14-29-21 Shrink relationComplexityError test size · microsoft_TypeScript@9e76dd2.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch or CodeReview.performed in the provided facts."
  },
  {
    "rule_id": "CR-02",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch, CodeReview.approver, PR.author, or CodeReview.approval_status in the provided facts."
  },
  {
    "rule_id": "COV-UNIT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.changes or Coverage.unit in the provided facts."
  },
  {
    "rule_id": "COV-INTEG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.affects_integration or Coverage.integration in the provided facts."
  },
  {
    "rule_id": "COV-CRIT-PAYMENT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.affected_feature or Coverage.line in the provided facts."
  },
  {
    "rule_id": "COV-CRIT-AUTH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.affected_feature or Coverage.line in the provided facts."
  },
  {
    "rule_id": "COV-CRIT-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.affected_feature or Coverage.line in the provided facts."
  },
  {
    "rule_id": "COV-BRANCH-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.changes or Coverage.branch in the provided facts."
  },
  {
    "rule_id": "COV-FUNC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.changes or Coverage.function in the provided facts."
  },
  {
    "rule_id": "REPORT-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.open, Coverage.report.generated, PR.attachments, or CodeReview in the provided facts."
  },
  {
    "rule_id": "TST-UNIT-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch, UnitTest.status, or UnitTest.failures in the provided facts."
  },
  {
    "rule_id": "TST-INTEG-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch or IntegrationTest.status in the provided facts."
  },
  {
    "rule_id": "TST-E2E-RUN-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.affects_critical_user_journeys or E2ETests.critical_journeys.status in the provided facts."
  },
  {
    "rule_id": "TST-PERF-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.requires_performance or PerformanceTest.benchmarks_met in the provided facts."
  },
  {
    "rule_id": "TST-SEC-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch or SecurityScan.review_status in the provided facts."
  },
  {
    "rule_id": "ENV-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.merge_attempt, CI.pipeline.run, or CI.environment in the provided facts."
  },
  {
    "rule_id": "PR-STATUS-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.open, PR.status_checks.tests.visible, or PR.status_checks.coverage.visible in the provided facts."
  },
  {
    "rule_id": "FLAKY-BLOCK-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch or FlakyTests.count in the provided facts."
  },
  {
    "rule_id": "FLAKY-AUD-01",
    "status": "NA",
    "reasoning": "There is no information on the existence of FlakyTest in the provided facts."
  },
  {
    "rule_id": "TEST-FAIL-FIX-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch or Test.failure_count in the provided facts."
  },
  {
    "rule_id": "TEST-MAINT-OBSO-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on Test.obsolete or Test.status in the provided facts."
  },
  {
    "rule_id": "TEST-MAINT-QA-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on Test.code.exists or Test.code_quality in the provided facts."
  },
  {
    "rule_id": "POLICY-REVIEW-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on Policy.review_frequency, Policy.last_reviewed, or months_since() in the provided facts."
  },
  {
    "rule_id": "BUG-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.target_branch or IssueTracker.open_issues.count in the provided facts."
  },
  {
    "rule_id": "SMOKE-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is no information on PR.affects_critical_features or ManualSmoke.tests_completed in the provided facts."
  }
]
```