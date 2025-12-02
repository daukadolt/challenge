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
function EvaluateCompliance(facts: string, control: Control) -> RuleEvaluation[] {
    client "openai/gpt-4o"
    prompt #"
        You are a Compliance Logic Engine. 
        Compare the provided FACTS against the RULES to determine compliance.

        INPUT CONTEXT (Extracted Facts):
        {{ facts }}

        ---
        RULES TO CHECK:
        {% for rule in control.rules %}
          {{ rule }}
        {% endfor %}
        ---

        {{ ctx.output_format }}
    "#
}

function ExtractControl(control: string) -> Control {
    client "openai-responses/gpt-5-mini" 
    prompt #"
        Extract the control logic from the following content into a structured format.
        
        Guidelines:
        1. Atomic Rules: Split compound thresholds (e.g. Unit 80% AND Integration 60%) into separate rules.
        2. Explicit Logic: Use exact values ('payment', 'auth') in logic strings.
        3. Type: Mark 'Blocking' for release gates, 'Audit' for maintenance.

        Content:
        {{ control }}

        {{ ctx.output_format }}
    "#
}