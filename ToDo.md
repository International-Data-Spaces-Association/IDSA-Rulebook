# Open Issues — Documentation ToDo List

This document maps open GitHub issues to rulebook documentation and identifies work needed to satisfy closure requirements.

## Issue #57: Describe the concept of the Application Plane in the functional requirements

**Status:** ✅ RESOLVED (Peter Koen marked as resolved via 010_Planes.md)

**GitHub Issue:** https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/issues/57

**Current Coverage:**
- [010_Planes.md](010_Planes.md) — Comprehensive section added describing the Application Plane with key characteristics, data consumption patterns, service provision, user interaction, and example functions (analytics, visualization, reporting).
- Context planes clarified: Control Plane (negotiation), Data Plane (transmission), Data Management Plane (lifecycle/governance), and Application Plane (user-facing consumption).

**Remaining Work:**
- ✅ **NONE** — The document fully addresses the issue requirements. The Application Plane is now clearly defined with:
  - Clear separation from other planes (control, data, management)
  - Key characteristics and responsibilities
  - Example functions (analytics, visualization, reporting)
  - User interaction patterns and governance integration

**Next Step:** Close issue #57 once Rulebook-3.0 branch is merged to main.

---

## Issue #70: More details on responsibilities of Trust Frameworks

**Status:** 🟡 PARTIALLY ADDRESSED (needs review and potential expansion)

**GitHub Issue:** https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/issues/70

**Current Coverage:**
- [009_Dataspace_Trust_Frameworks.md](009_Dataspace_Trust_Frameworks.md) — Comprehensive new chapter covering:
  - Definition of DTF with key terms
  - Core principles (decentralized socio-technical systems, minimal shared semantics)
  - Trust establishment and maintenance mechanisms
  - Failure modes and reconciliation rules
  - Governance coupling across layers
  - Implementation considerations with standards (DID, VC)

- [008_Trust.md](008_Trust.md) — Foundational trust concepts and properties

**Remaining Work:**
- ⚠️ **Review and validate** — Community review needed on:
  - Clarity of relationship between DSGA and DTF
  - Practical examples of claim reconciliation workflows
  - Explicit guidance on plurality of Trust Frameworks (how multiple DTFs coexist)
  
- ⚠️ **Potential expansion needed** for:
  - Role responsibilities of governance bodies (who enforces, who audits, who escalates?)
  - Practical examples of DTF implementation in different regional/sectoral contexts
  - Relationship between DTF policies and data sharing contract enforcement

**Next Step:** Request community review of [009_Dataspace_Trust_Frameworks.md](009_Dataspace_Trust_Frameworks.md) and [008_Trust.md](008_Trust.md) via pull request comments. Potentially create supplementary document on "Governance Responsibilities" or "Multi-DTF Scenarios" if feedback indicates gaps.

---

## Issue #64: Provide a clear statement on Intermediaries

**Status:** 🟡 PARTIALLY ADDRESSED (needs dedicated document)

**GitHub Issue:** https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/issues/64

**Current Coverage:**
- [005_Roles.md](005_Roles.md) — Comprehensive section on "Service Provider (intermediary, value-adding services)" with:
  - Definition of intermediaries as services acting on behalf of participants
  - Regulatory context (EU Data Governance Act)
  - Intermediary usage guidance (optional vs. mandatory, impact mitigation)
  - Distinction between intermediaries and value-added service providers
  
- Mention in [008_Trust.md](008_Trust.md) and governance concepts

**Remaining Work:**
- ⚠️ **May need a dedicated document** — Issue comments indicate need for standalone "Intermediaries in IDSA Dataspaces" white paper/document:
  - Detailed treatment of intermediary roles and responsibilities
  - Sovereignty and governance implications
  - Legal framework alignment (DGA, GDPR)
  - Economic and trust implications of intermediation
  - How intermediaries interact with data contracts and DTF policies
  
- ⚠️ **Clarification needed:**
  - Why intermediaries are NOT core to IDSA Rulebook (but recognized as existing)
  - How PII/personal data handling through intermediaries differs from standard data sharing
  - Safeguards and audit mechanisms for intermediary activities
  - Revocation and exit strategies
  - Aggregator patterns

**Proposed Solution:** Create new document:
- **File:** `011_Intermediaries.md` (or `126_Intermediaries.md` in functional section)
- **Scope:** 
  - Intermediary definition, roles, and types
  - Technical representation in data spaces (as participant with delegation/agency capabilities)
  - Governance and policy implications
  - Regulatory considerations (DGA, GDPR)
  - Risk mitigation and audit approaches
  - Relationship to sovereignty and autonomy
  
**Next Step:** Assign @viivilahteenoja or additional community contributor to draft `011_Intermediaries.md`. Issue explicitly requested a separate document/white paper for this topic. Target for future iteration.

---

## Issue #91: Regional Perspectives annex documents

**Status:** 🟠 NOT ADDRESSED (new document structure needed)

**GitHub Issue:** https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/issues/91

**Current Coverage:**
- No regional perspective documents currently exist in the rulebook
- Core rulebook provides generic governance and technical framework applicable across regions
- Some documents reference regulatory contexts (EU, mention of DGA/GDPR)

**Remaining Work:**
- ⚠️ **CRITICAL** — Create regional perspective documents with following structure (as per issue #91):

**Proposed Documents:** Create new folder `regional_perspectives/` with documents for each region:

1. **Regional Perspective Template** `regional_perspectives/TEMPLATE_Regional_Perspective.md`:
   - Overview
   - Key Initiatives and Infrastructure
   - Legal and Regulatory Dimension
   - Data Sovereignty and Governance
   - Interoperability in Data Spaces (technical protocols + regional profiles)
   - Trust, Privacy, and Security
   - Public-Private Collaboration
   - Cross-Border Data Flows (if applicable)
   - Emerging Trends and Future Outlook

2. **Initial Priority Regions** (from issue comments, expanded list):
   - European Union (lead: Marko Turpeinen, 1001 Lakes) — **DRAFT ASSIGNED**
   - India
   - South-East Asia
   - Africa
   - UAE
   - USA/Canada/Mexico
   - China
   - Japan
   - Australia
   - Brazil

3. **Supra-national Perspectives:**
   - OECD
   - United Nations
   - Regional bodies (ASEAN, AU, etc.)

**Outstanding Questions** (from issue #91 discussion):
- How detailed should "Key Initiatives and Infrastructure" be? (avoid listing data centers)
- What specifically should "Legal and Regulatory Dimension" cover? (acts, regulatory organizations, compliance frameworks)
- What details for "Data Sovereignty and Governance"?
- How should "Interoperability in Data Spaces" distinguish between IDSA-wide technical standards (DSP/DCP) and regional profiles?
- What content expected for "Trust, Privacy, and Security" beyond pointing to IDSA concepts?
- Should "Public-Private Collaboration" list research programs and public investments?
- Should "Cross-Border Data Flows" be moved to separate governance white paper instead?
- What is scope of "Emerging Trends and Future Outlook" to avoid speculative/low-value content?

**Next Step:** 
1. Clarify scope and structure with stakeholders (Marko Turpeinen, Lars Mnagel, mspiekermann)
2. Create detailed template document (`regional_perspectives/TEMPLATE_Regional_Perspective.md`)
3. Assign lead authors for each region
4. Set timeline for initial draft completion (EU first, then others)
5. Establish review and update process (given regulatory/market volatility)

**Target:** Rulebook 3.1 (after core rulebook stabilizes).

---

## Summary of Actions Required

| Issue | Current Status | Action Needed | Owner | Priority | ETA |
|-------|---|---|---|---|---|
| #57 | ✅ Resolved | Close issue once merged | — | Low | Immediate (v3.0) |
| #70 | 🟡 Partial | Community review + expand if needed | PeterKoen, ssteinbuss, rajiv-ishare | High | v3.0 |
| #64 | 🟡 Partial | Draft dedicated document | viivilahteenoja (or assign) | High | v3.0.1 |
| #91 | 🟠 Not addressed | Create regional perspective structure | turpema, larsmnagle, community | Medium | v3.1 |

---

## Notes

- All issue discussion context preserved in GitHub issues for reference
- Current rulebook addresses foundational concepts; regional/supplementary content can follow in point releases
- Issue #64 explicitly requested a separate document (not just a section), so recommend `011_Intermediaries.md` or similar
- Issue #70 discussion references technical/governance layer interactions; ensure documentation integrates claims, policies, and reconciliation across layers
- Issue #91 noted "Cross-Border Data Flows" should possibly be a separate white paper due to maintenance burden and regulatory volatility
