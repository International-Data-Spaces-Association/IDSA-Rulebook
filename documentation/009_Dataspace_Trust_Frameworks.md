# Dataspace Trust Frameworks

## Definition

A **Dataspace Trust Framework (DTF)** is the set of policies and claim definitions that state which trust evidence exists for data-sharing interactions and what it represents — it defines what must hold, not how it is implemented. It combines policies, accepted claims, trust anchors, and reconciliation rules; business processes are expressed as policies, not as mandatory procedures.

The DTF sits between the general concept of [Trust](008_Trust.md) and the concrete mechanisms for [Establishing Trust](103_Establishing_Trust.md). Those sections explain what trust means in a data space and why attribute-based trust is the preferred model. The DTF enables a concrete implementation of that model; it does not provide one. It states which evidence counts, which rules the evidence is checked against, who may issue that evidence, how disagreements are handled, and what happens when checks fail.

Trust in a DTF is not a permanent status. It is a local, purpose-specific, and time-bound assessment made by each participant for a concrete interaction. Certifications, membership credentials, and onboarding results may be accepted as evidence, but they do not create standing trust by themselves. They are claims whose issuer, validity, scope, holder binding, and revocation status must be checked according to the framework. This follows the zero-trust principle that access decisions depend on current evidence and explicit policy alignment, not on prior admission alone ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)).

A DTF therefore does not make participants trustworthy. It provides the semantic model and definitions against which an implementation can make trust explicit, verifiable, revocable, and auditable — the properties belong to the implementation.

Key terms:

- **Claim**: A machine-readable, cryptographically verifiable assertion about a participant, service, asset, or event, issued by an identifiable issuer. Claims can express identity attributes, membership, certifications, dataset provenance, compliance results, or operational facts. The relation between attributes, claims, and trust anchors is described in [Attributes & Claims](104_Attributes_and_claims.md).

- **Policy**: A machine-readable expression of rules that govern data discovery, negotiation, and sharing. The full policy definition is covered in [Policies](105_Policies.md).

- **Trust anchor**: An issuer, or a defined set of issuers, whose claims a verifier accepts as evidence for specified claim types. A trust anchor is not a general authority over the data space. Its role is scoped by the DTF: which claims it may issue, how its keys are discovered, how status is checked, and which accountability obligations it accepts.

- **Trust-anchor register**: The governance artefact that lists accepted trust anchors and the claim types for which each anchor is accepted. Each entry must state identity and key discovery, authorised claim types, status mechanism, accountability terms, admission and removal rules, and update propagation.

- **Reconciliation**: The process of determining whether a proposed interaction satisfies the applicable policies of the parties involved, given the claims presented. Within a shared policy profile, reconciliation can be deterministic. Across different profiles, vocabularies, or legal interpretations, reconciliation becomes negotiation or escalation. Automatic mapping between heterogeneous policy vocabularies must not be assumed unless the DTF defines it explicitly.

- **Autonomy and agency (sovereignty)**: The capability of a participant to control its data, make independent policy choices, select preferred service providers, and unilaterally suspend or revoke access to shared assets according to its own governance and legal constraints. How autonomy and agency are achieved architecturally is covered in [Achieving Participant Autonomy and Agency](101_Achieving_Autonomy_and_Agency.md).

- **Dataspace Governance Authority (DSGA)**: The governance-plane role that defines and maintains the governance framework of a data space. This includes participant admission rules, accepted DTFs, policy profiles, trust-anchor registers, escalation procedures, and dispute procedures. The DSGA is described in [DSGA](006_DSGA.md); creating a data space is covered in [Creating a data space](114_Creating_a_data_space.md).

- **Failure mode**: A class of situations in which trust cannot be established, maintained, or relied on. A DTF must define how these situations are detected, handled, escalated, and recorded.

### Core Principles

Trust frameworks assume that data spaces are decentralized socio-technical systems in their control and data planes, where technical protocols are coupled with governance mechanisms. Full decentralization of the governance plane is not assumed: operating data spaces retain central or federated governance elements such as credential issuers and participant-resolution services. A trust framework must make these residual central dependencies explicit rather than define them away. The rationale for decentralized architectures is developed in [Decentralization](007_Decentralization.md).

**Trust decisions are local.** Each participant evaluates evidence and policies for its own interaction. A DTF can define common evidence, policy profiles, and procedures, but it does not create a global trust state that all participants must share.

**Trust is evidence-based.** Identity, membership, certification, and prior successful interactions are inputs to trust evaluation. The DTF defines the vocabulary of evidence and what each item represents; whether presented evidence is sufficient for a given interaction is the participant's own decision.

**Trust is runtime-bounded.** Long-running interactions need re-evaluation rules, validity windows, status checks, and revocation handling. Cached decisions may be used only within documented scope and time limits.

**Technical and governance mechanisms are coupled.** Signature validation, policy evaluation, claim exchange, and status checks require governance decisions about issuers, liability, escalation, and conformance. A DTF must make these dependencies visible instead of describing the data space as fully decentralized without qualification.

### What a DTF Must Define

A DTF is operational only if it answers the following questions:

- **Evidence model**: Which claims are accepted, what they mean, which formats and schemas they use, and which metadata they must carry, including issuer provenance, validity, revocation or status mechanism, and holder binding.
- **Trust anchors**: Who may issue which claims, how their keys and status information are found, and how the trust-anchor register is updated.
- **Verification**: How signatures, holder binding, issuer authority, validity periods, and revocation or status information are checked.
- **Reconciliation**: How parties determine whether presented claims satisfy applicable policies, including what happens when policies conflict.
- **Lifecycle**: How claims, schemas, policy profiles, trust anchors, and framework versions are introduced, deprecated, migrated, revoked, or retired.
- **Failure handling**: Which failure modes are recognised, which response is required, which information may be disclosed, and when escalation is triggered.
- **Accountability**: What issuers, participants, service providers, auditors, and the DSGA are responsible for.

Binding these definitions to concrete protocols and schemas happens when a data space adopts the DTF, outside the DTF itself — see [From Framework to Operating Data Space](#from-framework-to-operating-data-space).

### Trust Establishment and Maintenance

Trust is established through iterative claim exchange, verification, policy alignment, and agreement creation.

**Claim verification is performed by the verifier.** It includes checking the issuer, signature or equivalent proof, holder binding, validity period, status or revocation information, and whether the issuer is authorised to issue that claim type. Verification does not require an interactive issuer session at decision time. It relies on published and cacheable artefacts with bounded staleness.

**Runtime maintenance is limited to legitimate signals.** Trust is maintained by observing status changes of relied-upon claims, revocation lists, protocol events, own access logs, agreed audit data, and conformance evidence. Monitoring does not grant visibility into a counterparty's internal systems unless that visibility is contractually and technically defined. Observer models and audit mechanisms are covered in [Observability](121_Observability.md).

**Withdrawal affects future interactions.** If a required assumption no longer holds, future access must be revoked, agreements may need to be terminated or degraded, and the incident may need escalation. Revocation governs future interactions. It cannot undo data transfers that have already completed.

### Failure Modes

A DTF must define how at least the following failure modes are handled:

- **Policy incompatibility**: Abort, negotiate, or escalate according to defined rules. Error responses must minimise disclosure so that a counterparty cannot enumerate the policy surface through probing.
- **Missing or insufficient claims**: Treat the requirement as unsatisfied unless the DTF defines a fallback, exception, or manual review path.
- **Claim compromise**: Invalidate affected trust chains, revoke or suspend affected claims, and define how relying parties are notified.
- **False attestation**: Use issuer accountability, dispute procedures, liability terms, and corrective revocation. Cryptographic verification cannot detect that a signed claim is false.
- **Issuer compromise**: Rotate anchors or keys, revoke affected claims, publish impact information, and define propagation deadlines.
- **Status-infrastructure unavailability**: Define fail-open or fail-closed behaviour, maximum cache age, validity windows, and risk-class-specific exceptions.
- **Verification/use gap**: Bound token, agreement, and decision lifetimes so that revocation between verification and use is not ignored.
- **Identifier-resolution failure**: Treat key-resolution failure as verification failure unless cached material is still valid under the framework.
- **Holder key compromise**: Define key rotation, incident reporting, credential re-issuance, and revocation duties.
- **Schema or vocabulary mismatch**: Define version negotiation, deprecation windows, migration rules, and fallback behaviour.
- **Monitoring or audit failure**: Define whether the interaction is suspended, degraded, escalated, or allowed to continue under additional conditions.

When multiple DTFs apply to one interaction, the DSGA must define explicit reconciliation rules. Absent explicit guidance, a conservative default is to require the most restrictive applicable constraints to be satisfied. If the intersection of constraints is empty, the expected outcome is abort-and-escalate, not silent weakening of one framework. Cross-framework alignment is discussed in [Interoperability in Data Spaces](115_Interoperability_in_data_spaces.md).

### Governance Coupling

Trust frameworks integrate technical rules with organisational and legal commitments.

**Rules must be enforceable by technology, business process, contract, or law.** A policy requiring audit logs, for example, also requires an agreement about audit-log creation, retention, disclosure, and use. Obligations that cannot be technically enforced after transfer, such as deletion or non-onward-sharing of delivered data, must be described as contractual or legal obligations.

**The trust-anchor register is a published governance artefact.** Any entity whose attestation capability the governance authority recognises — a public authority, a sectoral certifier, an industry body — can hold an entry. Each entry scopes the anchor to authorised claim types; it is not a general status. Admission, scoping, suspension, removal, and emergency updates must follow documented procedures. Removing a compromised anchor must propagate with urgency comparable to claim revocation. The role of trust anchors as roots of trust for claims is developed in [Attributes & Claims](104_Attributes_and_claims.md); the register is part of the governance framework the DSGA publishes when a data space is created (see [Creating a data space](114_Creating_a_data_space.md)).

**Trust anchors must accept issuer-accountability obligations.** These include correctness of attestations, secure key publication, status infrastructure, compromise reporting, timely revocation, and liability for false or negligent attestations.

**Governance rules must preserve participant sovereignty.** This includes independent policy choices, provider selection, and withdrawal of future access according to the participant's own governance and legal constraints.

**Policies, claims, and schemas change over time.** A DTF must define versioning, deprecation windows, migration procedures, compatibility rules, and the expected cost of schema churn for the policies and claims under its own purview.

**The DSGA defines how DTF conformance is assessed.** Options include self-assessment with published evidence, third-party audit, automated test suites, or a combination of these. Conformance attestations are themselves claims within the framework, keeping assessment inside the same trust model.

Trade-offs:

- Decentralization increases resilience but complicates reconciliation.
- Minimal semantics reduce overhead but require a robust negotiation protocol.
- Dynamic trust enables adaptability but demands continuous verification resources.
- Explicit trust anchors reduce verification ambiguity but reintroduce governance-plane centralization.

A DTF should state these trade-offs clearly. Decentralized verification means that participants can verify signatures and status without a central runtime decision service; it does not mean that the choice of trusted issuers is free of governance.

### From Framework to Operating Data Space

Base protocols for identity, claims, negotiation, and transfer are deliberately generic. A data space becomes operational when its governance material binds the open choices left by those protocols:

- **Protocol binding**: Which protocol versions, profiles, options, and interaction types are mandatory?
- **Interaction gating**: Which claims are required for onboarding, catalogue access, contract negotiation, transfer, usage control, audit, and dispute resolution?
- **Policy vocabulary**: Which policy constraints exist, what do they mean, and which claims satisfy them?
- **Credential schemas**: What does each claim look like on the wire, and how do issuers and verifiers interpret it?
- **Trusted issuers**: Who may issue which claims, and how do participants discover updates to that authority?
- **Identity method**: How are participants identified, and how is their key material resolved? Identity choices are discussed in [Identity](107_Identity.md).
- **Status and revocation**: How are expiry, suspension, revocation, status infrastructure outages, and caching handled?
- **Conformance and audit**: Which framework-defined evidence is required from implementations, participants, issuers, and services?

These answers bind only inside the data space's own governance perimeter. Between independently governed data spaces, there is no equivalent binding profile unless their governance authorities create one. How a data space organises these answers — admission rules, membership credentials, issuer governance — is covered in [Data space membership](106_Dataspace_Membership.md) and [Creating a data space](114_Creating_a_data_space.md); the same binding decisions, viewed as the basis of intra-data-space interoperability, are described in [Interoperability in Data Spaces](115_Interoperability_in_data_spaces.md).

### Implementation Considerations

Design constraints:

- Avoid assumptions of global information or synchronous communication.
- Keep the claim layer transport-independent so that trust evidence can work across full data space connectors, domain APIs, and simpler REST-based exchanges, for example the [PACT Technical Specification](https://wbcsd.github.io/data-exchange-protocol/) for product-carbon-footprint exchange.

### What a Trust Framework Cannot Guarantee

A DTF defines the vocabulary of evidence and evaluation. It does not solve every trust problem.

- **Recognition between data spaces**: Whether one data space accepts another data space's trust anchors is a governance decision involving liability, semantics, risk tolerance, and business incentives. No protocol can force recognition. Cross-data-space common agreements are discussed in [Interoperability in Data Spaces](115_Interoperability_in_data_spaces.md).

- **Post-transfer enforcement**: Once data has been delivered to another participant, technical control is limited. Deletion, non-onward-sharing, and usage limits are contractual or legal obligations unless the data is processed in a controlled technical environment.

- **Claim truth**: Verification proves that an issuer signed a claim — it authenticates the claim as the evidence presented. It makes no statement about the validity, truthfulness, completeness, or trustworthiness of the evidence, and whether the issuer is accepted is the participant's own evaluation. Truthfulness depends on issuer competence, accountability, audit, and liability.

- **Implementation quality**: A DTF does not build, operate, secure, or fund the software and processes required to execute it.
