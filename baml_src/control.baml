enum RuleType {
    Blocking @description(#"
        Rules that must pass immediately before a merge or release.
        Example: "All tests passed", "Coverage > 80%"
    "#)
    Audit @description(#"
        Maintenance or process rules that are measured over time, not per PR.
        Example: "Flaky tests fixed within 2 days", "Quarterly policy review"
    "#)
}

class Rule {
    id string @description("Short identifier, e.g. 'TEST-01'")
    
    type RuleType
    
    description string
    
    logic string @description(#"
        Propositional Logic. Be explicit with variable values.
        BAD: "CriticalPaths -> 100% Coverage"
        GOOD: "FilePath.contains('security', 'payment') -> Coverage == 100%"
    "#)
    
    exceptions string[] @description(#"
        List of specific scenarios where this rule can be skipped.
    "#)
}

class Control {
    name string
    description string
    rules Rule[]
}

enum RuleStatus {
    PASS
    FAIL
    MORE_INFOMATION_NEEDED
    NA @alias("N/A")
}

class RuleEvaluation {
    rule_id string 
    status RuleStatus
    reasoning string 
}
function EvaluateCompliance(facts_list: string[], control: Control) -> RuleEvaluation[] {
    client "openai/gpt-4o"
    prompt #"
        You are an AI Auditor evaluating a set of technical evidence for a Pull Request.

        ### The Control Policy
        {{ control }}

        ### The Evidence Facts
        Below is the aggregated data extracted from multiple files.

        {% for fact in facts_list %}
        --- Evidence Item {{ loop.index }} ---
        {{ fact }}
        {% endfor %}

        ### Instructions
        1. Evaluate the COMPOSITE state of the evidence. 
           (e.g. If Evidence 1 proves the PR is 'main', and Evidence 2 proves coverage is '80%', the rule PASSES).
        2. If a Blocking rule is not satisfied by the combined evidence, mark it FAIL.

        {{ ctx.output_format }}
    "#
}

function ExtractControl(control: string) -> Control {
    client "openai-responses/gpt-5-mini" 
    prompt #"
        Extract the control logic from the following policy document.
        
        ### Role
        You are a Compliance Architect defining rules for an AI Auditor. 
        Your output will be used to verify evidence (screenshots/logs) which may contain system-specific variations (e.g., "microsoft:main" vs "main").

        ### Extraction Guidelines
        1. **Robust Operators**: 
           - Avoid strict equality (`==`) for names, paths, or identifiers. Real-world data is messy.
           - Prefer **containment** or **matching** logic (e.g., `contains`, `matches`, `includes`) for text fields.
           - Use strict equality (`==`) ONLY for booleans (`true`/`false`) or fixed enums (`'approved'`, `'clean'`).

        2. **Atomic Granularity**: 
           - Break complex policies into the smallest possible testable units.
           - ONE rule = ONE concept. (e.g., Split "Review by independent peer" into "Review performed" AND "Reviewer is independent").

        3. **Contextual Gating**:
           - Explicitly define *when* a rule applies using the format: `Context -> Requirement`.
           - Example: `PR.changes.include_code -> Coverage.exists`

        ### Content to Extract
        {{ control }}

        {{ ctx.output_format }}
    "#
}