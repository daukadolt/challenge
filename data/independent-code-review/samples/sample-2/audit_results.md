# Audit Sample Report
**Overall Status:** FAIL

## Rule Reconciliation Summary
| Rule ID | Type | Verdict | Reason |
| :--- | :--- | :--- | :--- |
| CR-01 | RuleType.Blocking | PASS | Validated via evidence |
| CR-02 | RuleType.Blocking | PASS | Validated via evidence |
| CR-03 | RuleType.Blocking | PASS | Validated via evidence |
| TEST-01 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-02 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-03 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-04 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-05 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-06 | RuleType.Blocking | MISSING_EVIDENCE | Blocking rule applied but no passing evidence found in sample. |
| TEST-07 | RuleType.Blocking | FAIL | Although the PR targets the 'main' branch, there's no explicit information provided about the status... |
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

### Evidence [1]: Screenshot 2025-11-14 at 14-31-38 feat use Node.js timers by default · denoland_deno@12cde71.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "NA",
    "reasoning": "There is no information provided regarding PR.target_branch or PR.merge_requested or Review. Hence, this rule is not applicable."
  },
  {
    "rule_id": "CR-02",
    "status": "NA",
    "reasoning": "There is no information regarding the existence of a PR or any associated review. Therefore, this rule is not applicable."
  },
  {
    "rule_id": "CR-03",
    "status": "NA",
    "reasoning": "There is no data about the existence of a PR or review requests. Thus, this rule is not applicable."
  },
  {
    "rule_id": "TEST-01",
    "status": "NA",
    "reasoning": "No data on PR changes or code coverage details provided. Hence, this rule is not applicable."
  },
  {
    "rule_id": "TEST-02",
    "status": "NA",
    "reasoning": "There is no mention of changes involving integration points or related file paths. Therefore, this rule is not applicable."
  },
  {
    "rule_id": "TEST-03",
    "status": "NA",
    "reasoning": "No information on file paths or PR changes related to security, payment, or critical paths. This rule is therefore not applicable."
  },
  {
    "rule_id": "TEST-04",
    "status": "NA",
    "reasoning": "There is no information on whether a PR was created or requested for merge, or on the existence of coverage reports. This rule is not applicable."
  },
  {
    "rule_id": "TEST-05",
    "status": "NA",
    "reasoning": "No data on whether PR changes included code or related coverage metrics. Thus, this rule is not applicable."
  },
  {
    "rule_id": "TEST-06",
    "status": "NA",
    "reasoning": "There is no information about PR changes involving code or function coverage percentage. Therefore, this rule is not applicable."
  },
  {
    "rule_id": "TEST-07",
    "status": "NA",
    "reasoning": "Both PR.merge_requested and PR.target_branch data is missing; hence, this rule is not applicable."
  },
  {
    "rule_id": "TEST-08",
    "status": "NA",
    "reasoning": "The context does not specify if a PR was created or if integration points were involved. Thus, not applicable."
  },
  {
    "rule_id": "TEST-09",
    "status": "NA",
    "reasoning": "No information on whether changes affected critical user journeys. Therefore, not applicable."
  },
  {
    "rule_id": "TEST-10",
    "status": "NA",
    "reasoning": "There is no mention of performance impact changes or if the changes were flagged for performance applicability. Hence, not applicable."
  },
  {
    "rule_id": "TEST-11",
    "status": "NA",
    "reasoning": "Missing information on PR merge requests or security scan statuses. Therefore, this rule is not applicable."
  },
  {
    "rule_id": "TEST-12",
    "status": "NA",
    "reasoning": "No details provided on whether a PR was requested for merging or about the CI pipeline specifics. Thus, not applicable."
  },
  {
    "rule_id": "TEST-13",
    "status": "NA",
    "reasoning": "Lack of information on whether a PR was requested for merging. Hence, this rule is not applicable."
  },
  {
    "rule_id": "TEST-14",
    "status": "NA",
    "reasoning": "No information about test flakiness or target branch detail making this rule not applicable."
  },
  {
    "rule_id": "TQ-01",
    "status": "NA",
    "reasoning": "No information on existing tests or their properties. This rule is not applicable."
  },
  {
    "rule_id": "TQ-02",
    "status": "NA",
    "reasoning": "There is no detail on test existence or naming conventions. Hence, not applicable."
  },
  {
    "rule_id": "TM-01",
    "status": "NA",
    "reasoning": "No mention of flaky tests exists here. Therefore, this rule is not applicable."
  },
  {
    "rule_id": "POLICY-01",
    "status": "MORE_INFOMATION_NEEDED",
    "reasoning": "There is insufficient data on the current date, or when the policy was last reviewed to determine compliance."
  }
]
```

### Evidence [2]: Screenshot 2025-11-14 at 14-32-05 feat use Node.js timers by default by bartlomieju · Pull Request #31272 · denoland_deno.png
```json
[
  {
    "rule_id": "CR-01",
    "status": "PASS",
    "reasoning": "The PR targets the 'main' branch and has been merged. Review exists and is completed by reviewer 'dsherret'."
  },
  {
    "rule_id": "CR-02",
    "status": "PASS",
    "reasoning": "The PR targets the 'main' branch and review exists. The approval was given by someone other than the author, ensuring compliance."
  },
  {
    "rule_id": "CR-03",
    "status": "PASS",
    "reasoning": "The PR has been merged and a review exists. Status checks are passing which likely includes 'review' and review records exist as it was merged."
  },
  {
    "rule_id": "TEST-01",
    "status": "NA",
    "reasoning": "No information on whether the PR includes new code or the code coverage percentage."
  },
  {
    "rule_id": "TEST-02",
    "status": "NA",
    "reasoning": "No information on whether the PR changes include integration points or affect specific file paths that require a minimum integration coverage percentage."
  },
  {
    "rule_id": "TEST-03",
    "status": "NA",
    "reasoning": "No information about changes to critical paths or specific file paths, hence compliance cannot be determined."
  },
  {
    "rule_id": "TEST-04",
    "status": "NA",
    "reasoning": "No information about whether artifacts contain a coverage report or attachments contain it in the review context."
  },
  {
    "rule_id": "TEST-05",
    "status": "NA",
    "reasoning": "No information on whether the PR changes include code or branch coverage percentage."
  },
  {
    "rule_id": "TEST-06",
    "status": "NA",
    "reasoning": "No information on whether the PR changes include code or function coverage percentage."
  },
  {
    "rule_id": "TEST-07",
    "status": "FAIL",
    "reasoning": "Although the PR targets the 'main' branch, there's no explicit information provided about the status of CI unit tests."
  },
  {
    "rule_id": "TEST-08",
    "status": "NA",
    "reasoning": "No information on whether the PR changes include integration points."
  },
  {
    "rule_id": "TEST-09",
    "status": "NA",
    "reasoning": "No information on whether the changes affect critical user journeys."
  },
  {
    "rule_id": "TEST-10",
    "status": "NA",
    "reasoning": "No information about any performance-affecting changes."
  },
  {
    "rule_id": "TEST-11",
    "status": "NA",
    "reasoning": "No information on whether the PR changes include code or the status of the security scan."
  },
  {
    "rule_id": "TEST-12",
    "status": "NA",
    "reasoning": "No information about the CI pipeline's existence or the environment in which tests are being run."
  },
  {
    "rule_id": "TEST-13",
    "status": "NA",
    "reasoning": "No detailed information about whether specific status checks ('unit', 'integration', 'security') are contained in the merge request."
  },
  {
    "rule_id": "TEST-14",
    "status": "NA",
    "reasoning": "No information regarding flaky tests."
  },
  {
    "rule_id": "TQ-01",
    "status": "NA",
    "reasoning": "No specific information about the existing tests' properties."
  },
  {
    "rule_id": "TQ-02",
    "status": "NA",
    "reasoning": "No specific information about the naming and cases of existing tests."
  },
  {
    "rule_id": "TM-01",
    "status": "NA",
    "reasoning": "No information regarding flaky tests or tracking tickets."
  },
  {
    "rule_id": "POLICY-01",
    "status": "NA",
    "reasoning": "No information about the last review date of applicable policies."
  }
]
```