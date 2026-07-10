# Changelog

## Unreleased

### Changed

- `documentation/009_Dataspace_Trust_Frameworks.md`: full revision of the page.

  Normative changes:

  - Claims must carry issuer provenance, validity, a revocation or status mechanism, and holder binding; verification includes issuer authority and holder binding and relies on published, cacheable artefacts instead of an interactive issuer session.
  - "Decentralized oracles" removed: external facts enter the evaluation as claims from attested services with an explicit trust model (for example remote attestation per IETF RFC 9334).
  - Automatic policy transformation and attribute mapping are no longer assumed reconciliation capabilities; across profiles or vocabularies, reconciliation is negotiation or escalation.
  - Policy alignment stated as non-optional: an interaction without stated constraints is itself a policy — allow-all — and still passes through the agreement state machine.
  - Runtime monitoring narrowed to signals a party legitimately observes; monitoring grants no visibility into a counterparty's systems unless contractually and technically defined; "automatic revocation" replaced by defined withdrawal and termination duties; revocation cannot undo completed transfers.
  - Failure modes extended from two to eleven, each with required handling ("must" instead of "may"); error responses must be disclosure-minimising instead of carrying "clear error codes".
  - New trust-anchor model: trust anchor and trust-anchor register defined as key terms; register entries must state identity and key discovery, authorised claim types, status mechanism, accountability terms, admission and removal rules, and update propagation; the anchor role is scoped per claim type; removal propagates with the urgency of a claim revocation.
  - New issuer-accountability obligations: attestation correctness, key publication and status infrastructure, compromise reporting, timely revocation, liability for false or negligent attestations.
  - New conformance requirement: the DSGA defines how conformance is assessed; conformance attestations are themselves claims within the framework.
  - "Fully decentralized" corrected: control and data planes are decentralized, residual governance-plane dependencies must be made explicit; when multiple DTFs yield an empty constraint intersection, the expected outcome is abort-and-escalate.
  - Closing position reversed from "invalidates legacy models" to subsumption: certifications and broker or catalogue outputs become claims and evidence within the framework.

  Structural and editorial changes:

  - New sections: "What a DTF Must Define" (nine definition areas), "From Framework to Operating Data Space" (eight binding questions a concrete data space must answer), "Verified Self-Description Catalogues" (the framework as a configurable bundle; verification reports as conformance attestations with defined producer and readers), and "What a Trust Framework Cannot Guarantee" (five limits).
  - Core principles named and expanded: local trust decisions without a global trust state, evidence-based and runtime-bounded trust, coupled governance, plane separation matching the Dataspace Protocol, and minimal shared semantics as core-plus-profiles (following DCAT application profiles and the DSSC Blueprint Data Models building block), with the reconciliation cost of minimal semantics stated.
  - Implementation considerations expanded from two bullets (DID, VC) into a linked standards catalogue — SD-JWT VC, DCP, OpenID4VC with EUDI Wallet and eIDAS, status lists, ODRL and DPV, DSP, ETSI trusted lists and AdES/LTA, PROV, with PACT and the Eclipse XFSC Federated Catalogue as examples — using version-free references only.
  - Cross-links to sibling pages added throughout (006, 007, 008, 010, 101, 103, 104, 105, 106, 107, 114, 115, 121, 122).
