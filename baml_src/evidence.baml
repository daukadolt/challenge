// -----------------------------------------------------------------------------
// 1. Shared Input Wrapper (Supports Multimodal)
// -----------------------------------------------------------------------------
class EvidenceInput {
    img image? @description("A screenshot or image of the evidence")
    text string? @description("Textual content of the evidence (logs, code, etc.)")
    // pdf, audio, and video are standard BAML types for multimodal inputs
    // also, they are reserved keywords ¯\_(ツ)_/¯
    pdf_file pdf? @description("A PDF document containing evidence")
    audio_file audio? @description("Audio recording of evidence")
    video_file video? @description("Video recording of evidence")
}

// -----------------------------------------------------------------------------
// 2. Expanded Enum
// -----------------------------------------------------------------------------
enum EvidenceType {
    PullRequest @description("GitHub/GitLab PR/MR interface showing status, reviewers, or conversation")
    CoverageReport @description("SonarQube, Codecov, terminal or interface output showing coverage %")
    CIPipeline @description("CI/CD interface showing build steps, jobs, and pass/fail status")
    TestResult @description("JUnit/TestNG/Pytest output, or UI showing specific test case pass/fail counts")
    SecurityScan @description("Snyk, SonarQube Security, or Trivy output showing vulnerability counts")
    IssueBoard @description("Jira, Linear, or GitHub Issues list showing active bugs/tickets")
    PerformanceReport @description("JMeter, K6, or Lighthouse report showing latency/throughput metrics")
    GitCommit @description("Git commit view showing hash, author, message, and signature status")
    Unknown @description("Content is unclear or unrelated to code/deployment")
}

// -----------------------------------------------------------------------------
// 3. Router Function
// -----------------------------------------------------------------------------
function IdentifyEvidenceType(input: EvidenceInput) -> EvidenceType {
    client "openai/gpt-4o"
    prompt #"
        Identify the type of technical interface, log, or media shown.
        {{ _.role("user") }}
        
        {% if input.text %}
        Here is the text content:
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// -----------------------------------------------------------------------------
// 4. Extraction Functions
// -----------------------------------------------------------------------------

// --- Pull Request ---
class PRFacts {
    platform string? @description("The hosting platform (e.g. GitHub, GitLab, BitBucket)")
    pr_number string? @description("The numerical ID or identifier of the Pull Request")
    author_username string? @description("Username of the person who opened the PR")
    reviewer_usernames string[] @description("List of usernames who reviewed the PR")
    status string? @description("Current state of the PR (Open, Merged, Closed, Draft)")
    base_branch string? @description("The target branch into which changes are being merged")
    status_checks_passing bool? @description("Whether all automated status checks (CI, analysis) are passing")
}

function ExtractPRFacts(input: EvidenceInput) -> PRFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract the objective metadata from this Pull Request evidence.
        Do not infer information that is not explicitly visible/audible.

        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- Git Commit ---
class CommitFacts {
    commit_hash string? @description("The full or abbreviated SHA-1 hash of the commit")
    author_username string? @description("The username or email of the commit author")
    commit_message string? @description("The text message describing the commit changes")
    is_verified_signature bool? @description("Whether the commit has a verified GPG/SSH signature")
    parent_pr_id string? @description("The ID of the Pull Request this commit belongs to, if visible")
}

function ExtractCommitFacts(input: EvidenceInput) -> CommitFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract metadata from this Git Commit view.
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- Code Coverage ---
class CoverageFacts {
    tool_name string? @description("The name of the coverage tool (e.g. JaCoCo, Istanbul, Coverage.py)")
    overall_line_coverage float? @description("The percentage of total lines covered by tests (0.0 to 100.0)")
    new_code_line_coverage float? @description("The percentage of new/modified lines covered by tests")
    branch_coverage float? @description("The percentage of control flow branches executed")
    function_coverage float? @description("The percentage of functions/methods executed")
    visible_files_tested string[] @description("List of filenames or paths explicitly shown in the report")
}

function ExtractCoverageFacts(input: EvidenceInput) -> CoverageFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract the test coverage metrics visible in this report.
        If a specific metric (e.g. Branch Coverage) is not visible, leave it null.
        
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- CI Pipeline ---
class CIFacts {
    pipeline_id string? @description("Unique identifier for the CI pipeline run")
    overall_status string? @description("The final aggregate status (Success, Failed, Canceled, Running)")
    // Key: Stage name (e.g. 'Build', 'Test'), Value: Status
    stage_statuses map<string, string> @description("Map of stage names to their individual status (e.g. 'Build': 'Success')")
    environment string? @description("The target deployment environment (e.g. 'clean', 'prod', 'staging')")
    has_warnings bool @description("Whether there are non-blocking warnings in the pipeline output")
}

function ExtractCIFacts(input: EvidenceInput) -> CIFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract the CI/CD pipeline status. 
        Note: Differentiate between a single job failing vs the whole pipeline failing.
        
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- Test Results ---
class TestResultFacts {
    framework string? @description("The testing framework used (e.g. JUnit, Pytest, Cypress)")
    total_tests int? @description("The total number of tests executed")
    passed int? @description("The count of tests that passed")
    failed int? @description("The count of tests that failed")
    skipped int? @description("The count of tests that were skipped or pending")
    duration_seconds float? @description("Total execution time in seconds")
    failed_test_names string[] @description("Names or identifiers of specific tests that failed")
}

function ExtractTestResultFacts(input: EvidenceInput) -> TestResultFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract testing metrics.
        
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- Security Scan ---
class SecurityFacts {
    scanner_name string? @description("Name of the security scanning tool (e.g. Snyk, Trivy)")
    severity_counts map<string, int> @description("Map of severity levels (Critical, High, Medium, Low) to issue counts")
    total_vulnerabilities int? @description("Total count of detected vulnerabilities")
    top_critical_issues string[] @description("List of the most severe vulnerability names or IDs detected")
    is_passing bool? @description("Whether the scan meets the configured passing criteria")
}

function ExtractSecurityFacts(input: EvidenceInput) -> SecurityFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract security vulnerability data.
        
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- Issue Board ---
class IssueBoardFacts {
    board_name string? @description("The name or title of the issue tracking board")
    sprint_name string? @description("The name of the current sprint or iteration")
    visible_columns string[] @description("List of column headers visible on the board (e.g. 'To Do', 'In Progress')")
    active_ticket_count int? @description("Count of tickets currently in active/non-terminal states")
    assignees_visible string[] @description("List of usernames or names of people assigned to tickets")
}

function ExtractIssueBoardFacts(input: EvidenceInput) -> IssueBoardFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract state from this issue tracking board.
        
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}

// --- Performance Report ---
class PerformanceFacts {
    tool_name string? @description("Name of the performance testing tool (e.g. JMeter, K6)")
    performance_score int? @description("Overall performance score if provided (e.g. Lighthouse score)")
    avg_response_time_ms float? @description("Average response time in milliseconds")
    p95_response_time_ms float? @description("95th percentile response time in milliseconds")
    throughput_rps float? @description("Requests per second processed")
    error_rate_percent float? @description("Percentage of requests that resulted in errors")
}

function ExtractPerformanceFacts(input: EvidenceInput) -> PerformanceFacts {
    client "openai/gpt-4o"
    prompt #"
        Extract performance benchmarks and metrics.
        
        {{ _.role("user") }}
        
        {% if input.text %}
        {{ input.text }}
        {% endif %}

        {% if input.img %}
        {{ input.img }}
        {% endif %}

        {% if input.pdf_file %}
        {{ input.pdf_file }}
        {% endif %}

        {% if input.audio_file %}
        {{ input.audio_file }}
        {% endif %}

        {% if input.video_file %}
        {{ input.video_file }}
        {% endif %}

        {{ ctx.output_format }}
    "#
}
