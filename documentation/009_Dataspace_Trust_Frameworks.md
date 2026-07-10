# Dataspace Trust Frameworks

## Definition

A **Dataspace Trust Framework (DTF)** is the binding set of rules that tells data space participants how trust evidence is created, checked, accepted, rejected, and governed for data-sharing interactions. It combines policies, accepted claims, trust anchors, reconciliation rules, and business procedures into one operational framework.

The DTF sits between the general concept of [Trust](008_Trust.md) and the concrete mechanisms for [Establishing Trust](103_Establishing_Trust.md). Those sections explain what trust means in a data space and why attribute-based trust is the preferred model. The DTF makes that model executable: it states which evidence counts, which rules the evidence is checked against, who may issue that evidence, how disagreements are handled, and what happens when checks fail.

Trust in a DTF is not a permanent status. It is a local, purpose-specific, and time-bound assessment made by each participant for a concrete interaction. Certifications, membership credentials, and onboarding results may be accepted as evidence, but they do not create standing trust by themselves. They are claims whose issuer, validity, scope, holder binding, and revocation status must be checked according to the framework. This follows the zero-trust principle that access decisions depend on current evidence and explicit policy alignment, not on prior admission alone ([NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)).

A DTF therefore does not make participants trustworthy. It makes the grounds for trust explicit, verifiable, repeatable, revocable, and auditable.

Key terms:

- **Claim**: A machine-readable, cryptographically verifiable assertion about a participant, service, asset, or event, issued by an identifiable issuer. Claims can express identity attributes, membership, certifications, dataset provenance, compliance results, or operational facts. The relation between attributes, claims, and trust anchors is described in [Attributes & Claims](104_Attributes_and_claims.md).

- **Policy**: A machine-readable expression of rules that govern data discovery, access, contract negotiation, usage, obligations, and enforcement expectations. Policy design is covered in [Policies](105_Policies.md).

- **Trust anchor**: An issuer, or a defined set of issuers, whose claims a verifier accepts as evidence for specified claim types. A trust anchor is not a general authority over the data space. Its role is scoped by the DTF: which claims it may issue, how its keys are discovered, how status is checked, and which accountability obligations it accepts.

- **Trust-anchor register**: The governance artefact that lists accepted trust anchors and the claim types for which each anchor is accepted. Each entry must state identity and key discovery, authorised claim types, status mechanism, accountability terms, admission and removal rules, and update propagation.

- **Reconciliation**: The process of determining whether a proposed interaction satisfies the applicable policies of the parties involved, given the claims presented. Within a shared policy profile, reconciliation can be deterministic. Across different profiles, vocabularies, or legal interpretations, reconciliation becomes negotiation or escalation. Automatic mapping between heterogeneous policy vocabularies must not be assumed unless the DTF defines it explicitly.

- **Autonomy and agency (sovereignty)**: The capability of a participant to control its data, make independent policy choices, select preferred service providers, and unilaterally suspend or revoke access to shared assets according to its own governance and legal constraints. How autonomy and agency are achieved architecturally is covered in [Achieving Participant Autonomy and Agency](101_Achieving_Autonomy_and_Agency.md).

- **Dataspace Governance Authority (DSGA)**: The governance-plane role that defines and maintains the governance framework of a data space. This includes participant admission rules, accepted DTFs, policy profiles, trust-anchor registers, escalation procedures, and dispute procedures. The DSGA is described in [DSGA](006_DSGA.md); creating a data space is covered in [Creating a data space](114_Creating_a_data_space.md).

- **Failure mode**: A class of situations in which trust cannot be established, maintained, or relied on. A DTF must define how these situations are detected, handled, escalated, and recorded.

### Core Principles

Trust frameworks assume that data spaces are decentralized socio-technical systems in their control and data planes, where technical protocols are coupled with governance mechanisms. Full decentralization of the governance plane is not assumed: operating data spaces retain central or federated governance elements such as credential issuers and participant-resolution services. A trust framework must make these residual central dependencies explicit rather than define them away. The rationale for decentralized architectures is developed in [Decentralization](007_Decentralization.md).

**Trust decisions are local.** Each participant evaluates evidence and policies for its own interaction. A DTF can define common evidence, policy profiles, and procedures, but it does not create a global trust state that all participants must share.

**Trust is evidence-based.** Identity, membership, certification, and prior successful interactions are inputs to trust evaluation. None of them is sufficient on its own unless the DTF explicitly defines it as sufficient for a particular interaction class.

**Trust is runtime-bounded.** Long-running interactions need re-evaluation rules, validity windows, status checks, and revocation handling. Cached decisions may be used only within documented scope and time limits.

**Technical and governance mechanisms are coupled.** Signature validation, policy evaluation, claim exchange, and status checks require governance decisions about issuers, liability, escalation, and conformance. A DTF must make these dependencies visible instead of describing the data space as fully decentralized without qualification.

**Control-plane trust logic is separated from data-plane transfer.** Policy negotiation, claim verification, agreement creation, and revocation checks belong to the control plane. Data transfer or resource access happens in the data plane. This separation matches the architecture of the [Dataspace Protocol](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/) and is introduced in [Planes](010_Planes.md).

**Interoperability depends on minimal shared semantics.** A DTF should define a small shared core vocabulary for claims and policies, then allow domain-specific extensions through profiles, following the pattern established by [DCAT](https://www.w3.org/TR/vocab-dcat-3/) application profiles and the [Data Models building block of the DSSC Blueprint](https://archive.dssc.eu/space/BVE2/1071255252/Data+Models). Domain-specific extensions should be governed where the domain expertise sits. The smaller the shared core, the more important explicit reconciliation and escalation rules become. Two parties can only be deterministically reconciled over the vocabulary they share; everything outside it requires negotiation or human escalation. Semantic models for policies and shared data assets are covered in [Vocabularies](122_Vocabularies.md).

### What a DTF Must Define

A DTF is operational only if it answers the following questions:

- **Evidence model**: Which claims are accepted, what they mean, which formats and schemas they use, and which metadata they must carry, including issuer provenance, validity, revocation or status mechanism, and holder binding.
- **Policy profile**: Which policy language or profile is used, which constraints are valid, and how constraints map to claims.
- **Trust anchors**: Who may issue which claims, how their keys and status information are found, and how the trust-anchor register is updated.
- **Verification**: How signatures, holder binding, issuer authority, validity periods, and revocation or status information are checked.
- **Reconciliation**: How parties determine whether presented claims satisfy applicable policies, including what happens when policies conflict.
- **Lifecycle**: How claims, schemas, policy profiles, trust anchors, and framework versions are introduced, deprecated, migrated, revoked, or retired.
- **Failure handling**: Which failure modes are recognised, which response is required, which information may be disclosed, and when escalation is triggered.
- **Accountability**: What issuers, participants, service providers, auditors, and the DSGA are responsible for.
- **Conformance**: How implementations prove that they follow the framework, and how conformance evidence is published or verified.

Without these definitions, a DTF remains a conceptual trust model rather than an operating framework.

This list defines the framework content. A concrete data space still has to bind those choices to specific protocol versions, interaction types, credential schemas, and governance procedures; that operational binding is described in [From Framework to Operating Data Space](#from-framework-to-operating-data-space).

### Trust Establishment and Maintenance

Trust is established through iterative claim exchange, verification, policy alignment, and agreement creation.

**Claim issuance and presentation starts the evidence flow.** Participants obtain claims from accepted issuers and present them when an interaction requires evidence. A concrete exchange protocol for issuance and presentation is the [Decentralized Claims Protocol (DCP)](https://eclipse-dataspace-dcp.github.io/decentralized-claims-protocol/), an Eclipse Dataspace Working Group specification.

**Claim verification is performed by the verifier.** It includes checking the issuer, signature or equivalent proof, holder binding, validity period, status or revocation information, and whether the issuer is authorised to issue that claim type. Verification does not require an interactive issuer session at decision time. It relies on published and cacheable artefacts with bounded staleness.

**External facts enter the evaluation as claims.** Facts from registries, measurement systems, compliance checks, catalogues, or other services must carry provenance and an explicit trust model. They must not appear as unattributed oracle input. If runtime integrity of such services matters, remote attestation such as the model described in [IETF RFC 9334](https://www.rfc-editor.org/rfc/rfc9334) can be used.

**Policy alignment determines whether the interaction can proceed.** Policies express the constraints that must be satisfied before data is discovered, negotiated, accessed, transferred, or used. Agreement is reached through a defined negotiation process. In DSP-based data spaces, contract negotiation provides a state machine for offers, counter-offers, and agreements. Policy alignment is not optional: an interaction without stated constraints is itself a policy — allow-all — and still passes through the agreement state machine.

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

**Governance rules must preserve participant sovereignty.** This includes independent policy choices, provider selection where the framework allows it, and withdrawal of future access according to the participant's own governance and legal constraints.

**Policies, claims, schemas, and trust-anchor registers change over time.** A DTF must define versioning, deprecation windows, migration procedures, compatibility rules, and the expected cost of schema churn.

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

Trust frameworks should use common standards and profiles where possible:

- **Identity**: [W3C Decentralized Identifiers (DIDs)](https://www.w3.org/TR/did-core/), including method choices suitable for organisational participants.
- **Claim format**: [W3C Verifiable Credentials](https://www.w3.org/TR/vc-overview/), with holder binding through verifiable presentations and selective-disclosure formats such as [IETF SD-JWT VC](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) where individual attributes must be disclosed independently.
- **Claim exchange**: DCP for data space participant interactions; the [OpenID for Verifiable Credentials](https://openid.net/sg/openid4vc/) family where wallet-ecosystem interoperability is required, including interaction with the [EUDI Wallet](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) under [eIDAS](https://eur-lex.europa.eu/eli/reg/2024/1183/oj), which offers legal entities in the EU an attestation path independent of any single data space's membership.
- **Revocation and status**: [W3C status-list mechanisms](https://www.w3.org/TR/vc-bitstring-status-list/) or equivalent status mechanisms with documented outage behaviour.
- **Policy**: [ODRL](https://www.w3.org/TR/odrl-model/) with a domain profile; the [Data Privacy Vocabulary (DPV)](https://w3id.org/dpv), a W3C Community Group vocabulary, where personal-data and consent semantics are involved.
- **Negotiation and transfer**: [Dataspace Protocol (DSP)](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/) for catalogue, contract-negotiation, and transfer-process state machines.
- **Trust-anchor publication**: Signed trust lists or equivalent registers, with [ETSI trusted lists (TS 119 612)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/) as prior art. Where claims must remain verifiable beyond issuer lifetime, long-term signature profiles such as [ETSI AdES/LTA](https://www.etsi.org/deliver/etsi_en/319100_319199/31910201/) may apply.
- **Provenance**: [W3C PROV](https://www.w3.org/TR/prov-o/) or equivalent provenance models for claim and evidence metadata.

Design constraints:

- Avoid assumptions of global information or synchronous communication.
- Keep verification robust under partial outage through bounded caching, status validity windows, and explicit fail-open or fail-closed rules.
- Keep the claim layer transport-independent so that trust evidence can work across full data space connectors, domain APIs, and simpler REST-based exchanges, for example the [PACT Technical Specification](https://wbcsd.github.io/data-exchange-protocol/) for product-carbon-footprint exchange.
- Do not assume the availability of centralized runtime services or components, such as member registries, on the control or data plane. Where a governance-plane registry exists — trust lists, DSGA directories, or verified self-description catalogues such as the [Federated Catalogue](https://github.com/eclipse-xfsc/federated-catalogue) of the Eclipse Cross Federation Services Components (XFSC) — design verification to degrade gracefully when it is unreachable: cached lists and bounded validity windows rather than hard runtime dependencies.

#### Verified Self-Description Catalogues

A verified self-description catalogue can operationalise the trust framework. The framework is supplied to the catalogue as a configurable bundle: trust anchors, compliance checks, schemas, and the rules for interpreting verification results. Entries are verified against that bundle at listing time or on demand. Each verification produces a report — a conformance attestation in the sense of Governance Coupling — recording which checks ran, against which framework configuration, and when. The report is produced by the verification machinery, not by the submitting participant, and is retained with the entry it assesses.

Three parties consult this report:

- the registry operator when enforcing the listing policy,
- relying parties when deciding what weight an entry carries, and
- the governance authority or an auditor when a listing decision must be reconstructed after the fact.

Catalogue content therefore remains evidence verified under a stated configuration, not ground truth that relieves participants of their own verification.

Certification- and broker-based models are not invalidated by this definition. They are subsumed into it. A certification becomes one claim among others, and a broker or catalogue becomes a service whose outputs require provenance, trust-anchor governance, and status handling.

### What a Trust Framework Cannot Guarantee

A DTF defines the mechanics of evidence and evaluation. It does not solve every trust problem.

- **Recognition between data spaces**: Whether one data space accepts another data space's trust anchors is a governance decision involving liability, semantics, risk tolerance, and business incentives. No protocol can force recognition. Cross-data-space common agreements are discussed in [Interoperability in Data Spaces](115_Interoperability_in_data_spaces.md).

- **Participation**: A DTF lowers the cost and risk of trusting, but it does not create a business reason to share data. Adoption depends on demand, regulation, incentives, and implementation quality.

- **Post-transfer enforcement**: Once data has been delivered to another participant, technical control is limited. Deletion, non-onward-sharing, and usage limits are contractual or legal obligations unless the data is processed in a controlled technical environment.

- **Claim truth**: Verification proves that an accepted issuer signed a claim and that the claim satisfies technical checks. It does not prove that the issuer was correct. Truthfulness depends on issuer competence, accountability, audit, and liability.

- **Implementation quality**: A DTF does not build, operate, secure, or fund the software and processes required to execute it. The gap between framework and dependable operation is closed by engineering, governance, and investment.

A good DTF is therefore judged by whether it makes trust decisions explicit, checkable, limited, revocable, and accountable; not by whether it removes all central components or all residual risk.
