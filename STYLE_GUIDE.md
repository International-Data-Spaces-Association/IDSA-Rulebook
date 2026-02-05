IDSA Rulebook — Editorial Style Guide (draft)

Purpose
-------
This short style guide defines conventions for wording, normative language, punctuation and structure used across the Rulebook. Use this guide to keep text consistent, clear for novice readers, and aligned with a professional standards-style tone.

Core conventions
----------------
- Tone: Formal, neutral, instructional. Use present tense for definitions and requirements (e.g., "A DSGA defines ...").
- Sentences: Use complete sentences (subject + verb + predicate). Avoid noun fragments for definitions and guidance.
- Normative language: Follow the legend in `001_Introduction.md`. Use **must** for requirements, **should** for recommended practices that expect justification for exceptions, and **may** to indicate options.
- Vocabulary consistency: Prefer "participant" (technical role) and "organization" (legal entity) and use "DSGA" and "DTF" consistently for governance authorities and trust frameworks.
- Examples: When giving examples, prefix with "For example:" and keep them brief.
- Abbreviations & acronyms: Spell out on first occurrence with the acronym in parentheses (e.g., "Data Space Governance Authority (DSGA)").
- Bulleted lists: Expand terse bullets (<10 words) into at least one full sentence that explains the concept for novice readers.
- Headings: Use clear hierarchical headings and avoid ambiguous section names.
- Spelling: Use consistent British English.
- Punctuation: Use final-periods on all full-sentence bullets.

Documentation & process
-----------------------
- When editing, keep changes conservative and non-policy-making unless explicitly requested.
- Document any normative changes in `CHANGELOG.md` with a short description and rationale.
- Before committing editorial sweeps that affect many files, open a draft PR and request review from the editorial working group.

Examples
--------
- Bad: "- prohibitions"
- Good: "- **Prohibitions:** Explicit forbidden actions that must be enforced and may trigger remediation or sanctions (e.g., data export restrictions)."

Review checklist
----------------
- Are all bullets expanded into full sentences? (if they are intended as definitions)
- Do normative verbs follow the legend in `001_Introduction.md`?
- Are acronyms defined at first use?
- Are examples clearly delimited from normative text?
