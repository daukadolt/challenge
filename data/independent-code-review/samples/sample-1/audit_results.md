# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | FAIL | The PR was merged to the 'master' branch, indicating a merge was requested. However, there is no inf... |
| CR-02 | RuleType.Blocking | FAIL | The PR was merged into the 'master' branch, and it is assumed a review exists, but there is no infor... |
| CR-03 | RuleType.Blocking | FAIL | No information is provided about the review records or if the required status checks for review exis... |
| TEST-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-02 | RuleType.Blocking | FAIL | Files contain 'service', implying integration, with no coverage percentage data provided. |
| TEST-03 | RuleType.Blocking | PASS | Validated via evidence |
| TEST-04 | RuleType.Blocking | FAIL | A merge was requested but there is no information on the presence of a coverage report artifact or a... |
| TEST-05 | RuleType.Blocking | PASS | Validated via evidence |
| TEST-06 | RuleType.Blocking | PASS | Validated via evidence |
| TEST-07 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-08 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-09 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-10 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-11 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-12 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-13 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-14 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TQ-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TQ-02 | RuleType.Audit | NOT_APPLICABLE | No Data |
| TM-01 | RuleType.Audit | NOT_APPLICABLE | No Data |
| POLICY-01 | RuleType.Audit | NOT_APPLICABLE | No Data |

## Detailed Evidence Logs

### Evidence [1]: Screenshot 2025-11-14 at 14-27-50 Coverage Report.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "NA",
    "reasoning": "There's no information on PR target branch or merge request."
  },
  {
    "rule_id": "CR-02",
    "status": "NA",
    "reasoning": "There's no information on PR target branch or review existence."
  },
  {
    "rule_id": "CR-03",
    "status": "NA",
    "reasoning": "There's no information on review existence or merge request."
  },
  {
    "rule_id": "TEST-01",
    "status": "NA",
    "reasoning": "There's no information on whether the PR includes new code."
  },
  {
    "rule_id": "TEST-02",
    "status": "FAIL",
    "reasoning": "Files contain 'service', implying integration, with no coverage percentage data provided."
  },
  {
    "rule_id": "TEST-03",
    "status": "PASS",
    "reasoning": "No files related to 'security', 'payment', 'auth', and no mention of critical paths. Rule does not apply."
  },
  {
    "rule_id": "TEST-04",
    "status": "NA",
    "reasoning": "There's no information on merge request status."
  },
  {
    "rule_id": "TEST-05",
    "status": "PASS",
    "reasoning": "Branch coverage is 89.48%, which is above the required 70%."
  },
  {
    "rule_id": "TEST-06",
    "status": "PASS",
    "reasoning": "Function coverage is 94.79%, which is above the required 80%."
  },
  {
    "rule_id": "TEST-07",
    "status": "NA",
    "reasoning": "There's no information on merge request status or CI status."
  },
  {
    "rule_id": "TEST-08",
    "status": "NA",
    "reasoning": "There's no information on whether there is a merge request including integration points."
  },
  {
    "rule_id": "TEST-09",
    "status": "NA",
    "reasoning": "There's no information on changes affecting critical user journeys."
  },
  {
    "rule_id": "TEST-10",
    "status": "NA",
    "reasoning": "There's no information on performance applicability."
  },
  {
    "rule_id": "TEST-11",
    "status": "NA",
    "reasoning": "There's no information on merge request status or CI status."
  },
  {
    "rule_id": "TEST-12",
    "status": "NA",
    "reasoning": "There's no information on merge request status or CI pipeline."
  },
  {
    "rule_id": "TEST-13",
    "status": "NA",
    "reasoning": "There's no information on merge request status."
  },
  {
    "rule_id": "TEST-14",
    "status": "NA",
    "reasoning": "No information on test flakiness or target branches."
  },
  {
    "rule_id": "TQ-01",
    "status": "NA",
    "reasoning": "No information on whether tests exist."
  },
  {
    "rule_id": "TQ-02",
    "status": "NA",
    "reasoning": "No information on whether tests exist."
  },
  {
    "rule_id": "TM-01",
    "status": "NA",
    "reasoning": "No information on test flakiness."
  },
  {
    "rule_id": "POLICY-01",
    "status": "NA",
    "reasoning": "No information on policy review date."
  }
]
```

### Evidence [2]: Screenshot 2025-11-14 at 14-28-31 Shrink relationComplexityError test size by jakebailey · Pull Request #62754 · microsoft_TypeScript.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "FAIL",
    "reasoning": "The PR was merged to the 'master' branch, indicating a merge was requested. However, there is no information provided on whether a review exists or if its status is completed."
  },
  {
    "rule_id": "CR-02",
    "status": "FAIL",
    "reasoning": "The PR was merged into the 'master' branch, and it is assumed a review exists, but there is no information regarding the presence or outcome of the reviews or if the author approved it."
  },
  {
    "rule_id": "CR-03",
    "status": "FAIL",
    "reasoning": "No information is provided about the review records or if the required status checks for review exist, despite a merge being indicated."
  },
  {
    "rule_id": "TEST-01",
    "status": "NA",
    "reasoning": "There is no information on the inclusion of new code or coverage percentage details provided in the input."
  },
  {
    "rule_id": "TEST-02",
    "status": "NA",
    "reasoning": "There is no information on integration points or coverage percentage details provided in the input."
  },
  {
    "rule_id": "TEST-03",
    "status": "NA",
    "reasoning": "There is no information on security, payment, authentication changes, or coverage percentage details provided in the input."
  },
  {
    "rule_id": "TEST-04",
    "status": "FAIL",
    "reasoning": "A merge was requested but there is no information on the presence of a coverage report artifact or attachment in the review."
  },
  {
    "rule_id": "TEST-05",
    "status": "NA",
    "reasoning": "There is no detail provided on the inclusion of code changes or coverage percentage details in the input."
  },
  {
    "rule_id": "TEST-06",
    "status": "NA",
    "reasoning": "There is no detail provided on the inclusion of code changes or coverage percentage details in the input."
  },
  {
    "rule_id": "TEST-08",
    "status": "NA",
    "reasoning": "There is no information on the inclusion of integration points, hence the CI status of integration tests is not applicable."
  },
  {
    "rule_id": "TEST-09",
    "status": "NA",
    "reasoning": "There is no information on whether critical user journeys are affected, hence the CI status for e2e tests is not applicable."
  },
  {
    "rule_id": "TEST-10",
    "status": "NA",
    "reasoning": "There is no indication in the input that performance affecting changes have been made."
  },
  {
    "rule_id": "TEST-14",
    "status": "NA",
    "reasoning": "There is no indication of flaky tests being mentioned; hence the requirements around fixing/dropping are not applicable."
  },
  {
    "rule_id": "TQ-01",
    "status": "NA",
    "reasoning": "No test details are provided in the input context, so the determinism and other characteristics are irrelevant."
  },
  {
    "rule_id": "TQ-02",
    "status": "NA",
    "reasoning": "No test details are provided in the input context, so test naming and case inclusion standards are irrelevant."
  },
  {
    "rule_id": "TM-01",
    "status": "NA",
    "reasoning": "There is no mention of flaky tests, tracking tickets, or timelines in the input."
  },
  {
    "rule_id": "POLICY-01",
    "status": "NA",
    "reasoning": "There is no date-related information or policy review date provided in the input."
  }
]
```

### Evidence [3]: Screenshot 2025-11-14 at 14-29-21 Shrink relationComplexityError test size · microsoft_TypeScript@9e76dd2.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "NA",
    "reasoning": "The provided facts do not include information related to PR target branch or merge request status."
  },
  {
    "rule_id": "CR-02",
    "status": "NA",
    "reasoning": "The provided facts do not provide details on targeted branches, review existence, or approvals, hence cannot evaluate this rule."
  },
  {
    "rule_id": "CR-03",
    "status": "NA",
    "reasoning": "Information about PR merges, review existence, and status checks is missing from the facts provided."
  },
  {
    "rule_id": "TEST-01",
    "status": "NA",
    "reasoning": "There is no information about whether the PR includes new code or coverage percentage."
  },
  {
    "rule_id": "TEST-02",
    "status": "NA",
    "reasoning": "Facts do not indicate if the PR changes include integration points or if the files contain paths related to integration, API, or service."
  },
  {
    "rule_id": "TEST-03",
    "status": "NA",
    "reasoning": "No information is provided on paths or critical paths that would trigger the rule requirement for 100% line coverage."
  },
  {
    "rule_id": "TEST-04",
    "status": "NA",
    "reasoning": "The presence of merge requests or attachment of coverage reports to reviews is not indicated in the facts."
  },
  {
    "rule_id": "TEST-05",
    "status": "NA",
    "reasoning": "Facts do not specify if the PR includes code changes or any associated branch coverage percentage."
  },
  {
    "rule_id": "TEST-06",
    "status": "NA",
    "reasoning": "There is no information about code changes in the PR or function coverage percentage."
  },
  {
    "rule_id": "TEST-07",
    "status": "NA",
    "reasoning": "Details about PR target branch requirements, merge request status, and CI unit tests status with failures are not available."
  },
  {
    "rule_id": "TEST-08",
    "status": "NA",
    "reasoning": "The facts provided do not include information about merge requests or integration point changes affecting CI integration tests."
  },
  {
    "rule_id": "TEST-09",
    "status": "NA",
    "reasoning": "The presence of changes affecting critical user journeys is not indicated."
  },
  {
    "rule_id": "TEST-10",
    "status": "NA",
    "reasoning": "No data is available to determine if performance-related changes or applicable flags are present."
  },
  {
    "rule_id": "TEST-11",
    "status": "NA",
    "reasoning": "No information is given about merge requests, code inclusions, security scan statuses or reviews."
  },
  {
    "rule_id": "TEST-12",
    "status": "NA",
    "reasoning": "The facts provided do not mention merge requests or CI pipeline details such as environment cleanliness."
  },
  {
    "rule_id": "TEST-13",
    "status": "NA",
    "reasoning": "There is no information about PR merge requests or status checks related to unit, integration, and security tests."
  },
  {
    "rule_id": "TEST-14",
    "status": "NA",
    "reasoning": "There is no information about flaky tests or the target branch that would trigger further checks."
  },
  {
    "rule_id": "TQ-01",
    "status": "NA",
    "reasoning": "The facts do not provide specific data on test existence or test attributes such as determinism, repeatability, independence, or cleanup."
  },
  {
    "rule_id": "TQ-02",
    "status": "NA",
    "reasoning": "There is no information about test existence, naming conventions, or included test cases."
  },
  {
    "rule_id": "TM-01",
    "status": "NA",
    "reasoning": "The provided facts do not mention flaky tests, associated tracking, or ticket timelines."
  },
  {
    "rule_id": "POLICY-01",
    "status": "NA",
    "reasoning": "No policy-related information is given, such as the last review date to assess compliance with the 90-day review requirement."
  }
]
```