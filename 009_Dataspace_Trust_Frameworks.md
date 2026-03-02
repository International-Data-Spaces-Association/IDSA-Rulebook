# Dataspace Trust Frameworks

## Definition

A **Dataspace Trust Framework (DTF)** consists of a set of policies and reconciliation mechanisms for claims, as well as business process definitions that enable data space participants to establish trust and maintain mutual assurance in data sharing interactions. Trust is treated as a dynamic runtime property, derived from verifiable claims and policy alignments, rather than static certifications or centralized attestations.

Key terms:
- **Claim:** A machine-readable, cryptographically verifiable assertion issued by a trusted authority about a participant or an asset (for example, an identity attribute, certification, or dataset provenance). Claims serve as primary evidence in trust evaluations and must include provenance and validity metadata.

- **Policy:** A formal expression of rules and constraints that govern data access, usage, and sharing. Policies must be expressed in machine-readable languages and define required attributes, permitted actions, obligations, and enforcement expectations.

- **Reconciliation:** The deterministic or negotiated process that aligns policies and claims between parties to determine whether a proposed interaction complies with both parties’ constraints. Reconciliation may involve policy transformation, attribute mapping, or escalation to manual review.

- **Autonomy & Agency (Sovereignty):** The capability of a participant to control its data, make independent policy choices, select preferred service providers, and unilaterally suspend or revoke access to shared assets according to its governance and legal constraints.

- **Failure mode:** A class of scenarios that prevent trust from being established or maintained—examples include irreconcilable policy conflicts, compromised or unverifiable claims, or material deviations from declared behaviour—which should be handled by well-defined escalation and termination procedures.

### Core Principles

DTFs operate on the assumption that dataspaces are fully decentralized socio-technical systems, where technical protocols are coupled with governance mechanisms. Control plane activities (e.g., policy negotiation, claim verification) are separated from data plane operations (e.g., actual data transfer or access to a protected resource) to minimise coupling and enhance scalability.

Interoperability is achieved through minimal shared semantics, such as a common vocabulary for claims, rather than heavy global schemas. This allows for evolutionary changes without breaking existing implementations and supports the implementation of domain specific data spaces and DTFs.

### Trust Establishment and Maintenance

Trust is established through iterative claim exchange and policy reconciliation as described in the [Trust](008_Trust.md) section. Summarisable by those important points:
1. **Claim Issuance and Verification**: Participants issue claims about themselves or their data. Verification occurs via cryptographic proofs (e.g., digital signatures) or decentralized oracles, without reliance on central authorities.
2. **Policy Alignment**: Policies are expressed as logical constraints. Reconciliation uses a negotiation protocol to find mutually acceptable terms.
3. **Runtime Monitoring**: Trust is maintained through continuous monitoring of invariants, such as data usage logs or revocation signals. Violations trigger automatic revocation or escalation to human oversight.

Failure modes may include:
- **Policy Incompatibility**: If reconciliation fails, interactions are aborted with clear error codes.
- **Claim Compromise**: Detected via integrity checks; compromised claims invalidate trust chains.

When multiple Dataspace Trust Frameworks (DTFs) apply to an interaction, the DSGA must define explicit reconciliation rules. Absent explicit guidance, a conservative default is to require the intersection of constraints (the most restrictive applicable constraints) to be satisfied. The DSGA should also define escalation paths (e.g., arbitration, human review, or a voting mechanism) for irreconcilable conflicts and document the expected outcomes and timelines in the governance material.

### Governance Coupling

DTFs integrate technical and governance layers:
- **Socio-Technical Invariants**: Rules must be enforceable either through technological means or business processes at both protocol and organisational levels (e.g., a policy requiring audit logs must have corresponding legal agreements and data sharing agreements for the audit log data).
- **Evolution Handling**: DTFs support versioned policies and claims.
- **Revocation Mechanisms**: Participants can revoke trust unilaterally.

Trade-offs:
- Decentralization increases resilience but complicates reconciliation.
- Minimal semantics reduce overhead but require a robust negotiation protocol.
- Dynamic trust enables adaptability but demands continuous verification resources.

### Implementation Considerations

DTFs should be designed with common base standards:
- Use standards like DID (Decentralized Identifiers), VCs (Verifiable Credentials).
- Avoid assumptions of global information, or synchronous communication.
- Not assume the availability of centralized services or components (e.g., member registries)

This DTF definition invalidates legacy models relying on static certifications or central brokers, as they do not scale to decentralized data spaces.