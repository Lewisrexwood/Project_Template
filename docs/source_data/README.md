# docs/source_data/

**Verbatim** reference documents from the data providers — data
dictionaries, methodology PDFs, definitions-of-terms, etc.

## Rules

- **Do not modify files in this directory.** They are the authoritative
  record of what the provider said, and editing them breaks the chain
  of trust.
- If a definition is ambiguous or outdated, capture the ambiguity in
  `outstanding_issues.md` — do not "fix" the source document.
- Reference these files from `docs/plan/00_summary.md` whenever a
  decision depends on a definition here (e.g. "the provider defines
  inflow as X — see `docs/source_data/inflow_methodology.pdf`").

## Index

Add one line per source document: filename, what it is, date obtained.

- {{`filename.pdf` — {{what it is}} — obtained {{YYYY-MM-DD}}}}
