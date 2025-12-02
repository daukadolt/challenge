enum EvidenceType {
    PullRequest @description("GitHub/GitLab PR/MR interface showing status, reviewers, or conversation")
    CoverageReport @description("SonarQube, Codecov, terminal or interface output showing coverage %")
    CIPipeline @description("CI/CD interface showing build steps, jobs, and pass/fail status")
    Unknown @description("Image content is unclear or unrelated to code/deployment")
}

function IdentifyEvidenceType(img: image) -> EvidenceType {
    client "openai/gpt-4o"
    prompt #"
        Identify the type of technical interface shown in this image.
        {{ _.role("user") }}
        {{ img }}
        {{ ctx.output_format }}
    "#
}

class PRFacts {
    platform string? @description("e.g. GitHub, GitLab, BitBucket")
    pr_number string?
    author_username string?
    reviewer_usernames string[] 
    status string? @description("Open, Merged, Closed, Draft")
    base_branch string? 
    status_checks_passing bool?
}

function ExtractPRFacts(img: image) -> PRFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract the objective metadata from this Pull Request image.
        Do not infer information that is not visible.
        {{ _.role("user") }}
        {{ img }}
        {{ ctx.output_format }}
    "#
}

class CoverageFacts {
    tool_name string?
    overall_line_coverage float?
    new_code_line_coverage float?
    branch_coverage float?
    function_coverage float?
    visible_files_tested string[]
}

function ExtractCoverageFacts(img: image) -> CoverageFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract the test coverage metrics visible in this report.
        If a specific metric (e.g. Branch Coverage) is not visible, leave it null.
        {{ _.role("user") }}
        {{ img }}
        {{ ctx.output_format }}
    "#
}

class CIFacts {
    pipeline_id string?
    overall_status string? @description("Success, Failed, Canceled, Running")
    // Key: Stage name (e.g. 'Build', 'Test'), Value: Status
    stage_statuses map<string, string>
    environment string? @description("e.g. 'clean', 'prod', 'staging'")
    has_warnings bool
}

function ExtractCIFacts(img: image) -> CIFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract the CI/CD pipeline status. 
        Note: Differentiate between a single job failing vs the whole pipeline failing.
        {{ _.role("user") }}
        {{ img }}
        {{ ctx.output_format }}
    "#
}