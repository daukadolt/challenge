# Bead Audit Agent Challenge Solution

This repository contains the solution for the Bead Audit Agent Challenge. The solution implements an automated control auditor that verifies evidence against control requirements using BAML (Better Architecture for ML).

## Setup

### Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- OpenAI API Key (or other BAML-compatible provider)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Environment Setup:**
   Duplicate the `env.template` file to `.env` and fill in your API keys:
   ```bash
   cp env.template .env
   # Edit .env to add your OPENAI_API_KEY
   ```

## Requirements & Assumptions

The system expects the input directory (control directory) to follow this structure:

1. **Control Definitions**: The directory must contain one or more Markdown (`.md`) files describing the control. These files are used as the source to extract audit rules.
2. **Samples Directory**: The directory must contain a `samples` subdirectory.
3. **Sample Structure**: Each subdirectory within `samples/` is treated as an individual audit sample.
   - *Note:* Currently, only image files (evidence screenshots) are supported for analysis within these sample directories.
4. **Output**: For each processed sample, the audit results (reconciliation of rules and evidence) will be written into an `audit_results.md` file within that sample's directory.

## Usage

### Running the Auditor
To run the auditor against the provided samples, use the following command:

```bash
# Default path (data/independent-code-review)
python src/main.py

# Custom path
python src/main.py path/to/your/control/directory
```

### Output
The tool processes each sample in the target directory and generates an assessment. The results are printed to the console, and detailed report is saved to `audit_results.md` in each sample folder.

## Project Structure

- `src/main.py`: Entry point for the CLI.
- `src/services/`: Business logic for control and sample processing.
- `baml_src/`: BAML definitions for the AI logic (extraction, classification, reasoning).
- `data/`: Sample data and control definitions.

## How it works
1. **Control Parsing**: The system reads the `control.json` or `control.md` to understand the audit requirements.
2. **Evidence Analysis**: It iterates through sample folders, analyzing evidence (screenshots).
3. **Verification**: Using LLMs defined via BAML, it compares the evidence against the control rules to determine compliance (SUCCESS, FAIL, or FURTHER_EVIDENCE_REQUIRED).
4. **Reconciliation**: It aggregates results across all evidence for a sample and generates a final report.
