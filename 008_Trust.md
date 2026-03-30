# Trust in Data Spaces

## Definition
Trust in a decentralized data space is a situational, time-bound, and purpose-specific assessment of whether another participant can be relied upon to act within declared constraints for a specific interaction.

Trust is always created locally by each participant through its own evaluation of evidence, claims, and policies.

Trust is:

- **Not global:** Trust determinations are specific to a single data sharing contract and apply only to the parties that negotiate and execute that contract; they do not automatically extend to other contracts or to different counter-parties.

- **Not transitive:** A trust relationship established between two participants (for example, A trusts B) does not imply or create trust between either party and a third party (for example, B and C); each relationship requires its own independent assessment. Trust anchors can simplify evidence verification chains but do not create automatic trust transfer between participants.

- **Not reciprocal:** A unilateral decision by participant A to trust participant B does not compel B to trust A; mutual trust requires independent and explicit evaluations by each party.

- **Not permanent:** Trust assessments are time- and context-bound; changes in evidence, claims, policies, compliance status, or operational context may invalidate prior assessments and should trigger re-evaluation according to documented rules.

- **Not equivalent to identity, certification, or prior membership:** Identity credentials, certifications, and membership status can serve as evidence for trust but are not alone sufficient to establish trust without additional contextual evidence, policy alignment, and runtime verification.

## Non-Assumptions
A conforming decentralized data space must not assume the following as sufficient or universal substitutes for trust. Each item below explains why it is insufficient on its own:

- **A central authority, broker, registry, or trust anchor:** Centralized services may provide useful evidence or convenience, but reliance on them creates a single point of control and does not replace per-contract, evidence-based trust decisions.

- **Pre-established federation membership:** Membership in a federation (infrastructure, data space, business, etc...) may indicate a baseline of trustworthiness but does not guarantee that a specific participant satisfies the policy or technical requirements of any given contract or context.

- **Static certification or onboarding events as sufficient for trust:** One-off certifications or onboarding checks are useful provenance, but they do not capture runtime behaviour, compliance drift, or post-issuance changes and therefore cannot alone assure ongoing trust.

- **Homogeneous policy languages or enforcement stacks:** Shared policy languages may aid interoperability, yet different parties may implement or interpret policies differently; trust frameworks must tolerate heterogeneity and reconcile policy semantics.

- **That trust can be inferred solely from cryptographic identity:** Cryptographic identity proves control of keys, not adherence to policies or intent; trust requires additional attestations, claims, and evidentiary evaluation.

Any architecture that depends exclusively on the assumptions above is not representative of a fully decentralized data space and is likely to fail to provide robust, context-aware trust.

## Separation of Concerns
Trust assessment must be confined to the control plane. 

The transfer process defined by the [Dataspace Protocol (DSP)](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/) involves two logical constructs: a control plane and a data plane. Their characteristics are explained in detail in the [Planes](010_Planes.md) section.

The data plane is agnostic to trust logic and trust state.
Trust decisions may influence if, when, and how data plane interactions are initiated or continued.


## Claims
Trust is derived by claim reconciliation at interaction time.
Valid claim inputs include:

- Verifiable claims (representing evidence about identity, attributes, roles, attestations).
- Declared policies and obligations.
- Observed runtime behaviour from prior interactions.
- Third-party assertions with verifiable provenance (expressed as verifiable claims).
- Contextual factors (purpose, jurisdiction, risk class, data category).

By default, and unless a DSGA/DTF explicitly specifies an alternative, the absence of an input SHOULD be treated as negative (or unknown) for the purposes of trust evaluation; DSGAs and DTFs must document the chosen default and any exceptions.

## Trust establishment mechanisms
Trust establishment in data spaces relies on the exchange and verification of claims, dynamic policy negotiation, and evidence collection. 

Trust formation is an explicit, local process.

Each participant:

- Evaluates incoming claims and policies against its own constraints.
- Determines acceptability for a specific action and scope.
- Maintains its own trust state without global publication.

Trust formation must be repeatable and enable auditable by the evaluating participant. The audit logs might have to be shared through data space [observability](121_Observability.md)

Trust outcomes must be explainable in terms of accepted and rejected claims.

Trust mechanisms must support decentralized identities without mandatory reliance on a centralized or federated identity provider, gatekeeper, or broker. Participants and the DSGA may define and accept multiple trust anchors (credential issuers) as part of the Dataspace Trust Framework; reliance on an accepted anchor is a deliberate governance choice and does not imply implicit central control. Policy and claims exchange uses interoperable, machine-readable protocols and formats.
Centralized-only identity architectures are not aligned with the autonomy and agency objectives of decentralized data spaces.


## Trust is a Runtime Property
Trust exists only while its assumptions hold.
Therefore:

Trust can be continuously re-evaluated for long-running interactions.
Material changes in claims, policies, context, or behaviour should trigger re-evaluation.
Cached trust decisions should have explicit validity bounds. A participant MAY reuse a cached trust assessment for similar future interactions only if the scope, risk class, and validity period are explicit, conservatively limited, and documented; cached assessments must be re-evaluated on any material change to claims, policies, or context.

There is no concept of “once trusted, always trusted”. Participants should define verification frequency according to the sensitivity of the data and the risk of the interaction (for high-sensitivity assets require on-demand or per-execution revalidation; for lower-sensitivity assets periodic revalidation may be acceptable). Revocation signals must be handled promptly by participants; the DSGA or chosen DTFs should document expected propagation and verification intervals for different risk classes.

## Trust and Policy Interaction
Policies do not enforce trust; they express expectations.
Trust emerges from:

- Comparing declared policies with verifiable claims.
- Assessing whether obligations can realistically be met.
- Evaluating enforcement mechanisms offered by the counterparty.

Policy compliance must be treated as probabilistic unless directly observable.
Trust decisions should explicitly capture residual risk.

## Revocation and Trust Withdrawal
Trust can be revoked at any time.
Triggers for withdrawal include:

- Claim revocation or expiry.
- Policy violations or non-compliance signals.
- Context changes invalidating prior assumptions.
- Inability to re-validate critical assertions.

### Revocation:

- Propagates to ongoing interactions.
- Can require termination, degradation, or isolation of data access.
- Doesn't depend on centralized revocation services.

## Failure Modes
Architectures implementing Trust should explicitly handle:

- False-positive trust due to over-reliance on credentials.
- False-negative trust due to incomplete information.
- Asymmetric trust where only one side evaluates rigorously.
- Stale trust decisions in long-lived processes.
- Strategic misrepresentation of policies or capabilities.

Ignoring these failure modes renders trust claims non-credible.

## Interoperability Constraints
To remain interoperable:

- Trust mechanisms must rely on minimal shared and discoverable semantics.
- Claim formats must be extensible and schematically loose.
- Trust logic must not  assume shared policy languages, implementations or engines.

Interoperability emerges at the protocol boundary, not the trust model.

## Governance Implications
Trust is inseparable from governance.
Therefore:

- Dataspace Trust Frameworks (DTFs) must define acceptable trust evidence categories.
- Dispute resolution must acknowledge divergent trust assessments.
- Cross-domain interactions must tolerate incompatible trust conclusions.

Consensus on outcomes is optional; consistency of process is mandatory.

## Explicit Invariants
A decentralized dataspace conforming to this model therefore must uphold:

- Local autonomy of trust decisions.
- Explicit trust scope and duration.
- Continuous re-evaluation and revocation.
- No mandatory central trust services.
- No implicit trust via participation alone.

**These invariants take precedence over compatibility with prior data space models.**

