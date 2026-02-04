# Trust in Data Spaces

## Definition
Trust in a decentralized data space is a situational, time-bound, and purpose-specific assessment of whether another participant can be relied upon to act within declared constraints for a specific interaction.

Trust is:

- **Not global**: each decision to trust is local to one specific data sharing contract.
- **Not transitive**: each decision to trust applies only to the two parties involved in the data sharing contract.
- **Not reciprocal**: if one participants A decides to trust another participant B it doesn't enforce that B also must trust A.  
- **Not permanent**: the trust decision can change if the pre-requisits change
- **Not equivalent to identity, certification, or prior membership**: those elements can be attributes used to create trust.

## Non‑Assumptions
A conforming decentralized data space must not assume:

- A central authority, broker, registry, or trust anchor.
- Pre-established federation membership.
- Static certification or onboarding events as sufficient for trust.
- Homogeneous policy languages or enforcement stacks.
- That trust can be inferred solely from cryptographic identity.

Any architecture relying on these assumptions is not representative of a data space.

## Separation of Concerns
Trust assessment must be confined to the control plane.

The data plane is agnostic to trust logic and trust state.
Trust decisions may influence if, when, and how data plane interactions are initiated or continued.


## Claims
Trust is derived by claim reconciliation at interaction time.
Valid claim inputs include:

- Verifiable claims (representing evidence about identity, attributes, roles, attestations).
- Declared policies and obligations.
- Observed runtime behavior from prior interactions.
- Third-party assertions with verifiable provenance (expressed as verifiable claims).
- Contextual factors (purpose, jurisdiction, risk class, data category).

Absence of an input must be interpreted as negative trust.

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


## Trust is a Runtime Property
Trust exists only while its assumptions hold.
Therefore:

Trust can be continuously re-evaluated for long-running interactions.
Material changes in claims, policies, context, or behavior should trigger re-evaluation.
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

**These invariants take precedence over compatibility with prior dataspaces models.**

