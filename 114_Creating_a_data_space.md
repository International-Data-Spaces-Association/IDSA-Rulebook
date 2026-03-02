### Creating a data space

After discussing how to join a data space the question is: How do you
create a data space? The answer depends again on the purpose of your
data space and the needs of its participants. Regardless of whether the
data space is organized in a centralized, decentralized, federated or
hybrid manner, common denominators and basic functionalities can be
found.

![Overview of Data Space entities](../media/DataSpace-withDSGovernanceAuthority.jpg)

A data space establishes trust within a community to share data with
each other. The definition of community can be very broad. It might be a
tight knit, small community of one company and its suppliers, or a large
community with many participants. Some data spaces are created for a
narrow use case and purpose others for many use cases that are relevant
for a group of participants.

Many decisions need to be made when designing the data space, here some
of the more common ones:

- Is the membership closed to a small, known group or open to a larger
    range of participants?

- Do you want a central party with additional privileges (e.g.,
    exclusion of participants for bad behavior) or is the independence
    of the participants and their autonomy the most important design
    factor?

- What level of technical maturity is expected from the participants?

- What type of data is shared and for what purpose?

Answering these questions helps you make the design choices between
architectures and deployment patterns of data spaces.

Once all design decisions are made, the following functional elements must be specified and documented:

- **Rules:** Define the expected behaviours, roles, and minimum technical and organizational capabilities required of participants (for example, required legal contracts, organizational certifications, staff skills, security practices, or operational governance targets).

- **Policies:** Specify the participation, access, contract, and usage policies that will be enforced by the data space participants and describe how these policies are verified and evolved.

- **Membership certification:** Describe the mechanism and evidence required to verify and certify membership (for example, identity documentation, audits, or third-party attestations), including issuance, renewal, and revocation processes.

- **Participant registry:** Establish if, where and how authorized participants and their self-descriptions are published or discoverable, and which attributes are visible to different query roles.

- **Identity system:** Decide whether identities will be managed via decentralized identifiers (DIDs), centralized identity services (not recommended), or a hybrid approach, and document the control, governance, and privacy implications of each option.

- **Catalog(s):** Specify the catalog model (single central catalog(note recommended), multiple federated catalogs, or per-participant catalogs), their APIs, metadata standards, and how catalog visibility and access controls will be applied.

Working through the above list of mandatory functional elements will
clarify the architecture pattern for the data space, which will also
mandate a specific design of the data space governance authority. Now the DSGA needs
to be implemented to create the data space:

1. Create an identity for the data space
2. Provide a self-description

    The self-description for the data space should include the following documented elements:

    - **Membership policies:** The eligibility criteria and evidence required for organizations to join, including any onboarding checks, audit requirements, and renewal conditions.

    - **Trust anchors and trust frameworks:** A list of accepted credential issuers, Dataspace Trust Frameworks (DTFs), and the rules by which claims and attestations are validated.

    - **Attributes used for trust decisions:** A clear listing of attributes, their meaning, and how they map to policy constraints so participants can determine how trust levels are calculated.

    - **Technical component requirements:** The required interfaces, protocols, and implementations (for example, software agent capabilities) necessary to interact with the data space.

    - **Participant registry:** If a participant registry is required; the location and format of the participant registry or discovery endpoints, and which attributes are published for discovery versus private ones accessible only to existing members.

    - **Registration service and related workflows:** The documented workflow to request membership, the validation procedures used to determine compliance with membership requirements, the process for issuance of membership credentials, and the rules and procedures to revoke credentials when necessary.

3. Provide a discovery mechanism for the data space (website, contact
    form, etc.)

Once at least one Onboarding Service implementing the DSGA is instantiated, organizations can apply for membership.
The functional elements listed above are mandatory capabilities for a functioning data space, but they may be implemented in decentralized or centralized ways. When a centralized or federated implementation is chosen, the DSGA must document the reasons for that choice and describe mitigating measures to protect participant autonomy and agency.
After a participant joins, there are two main activities that all
participants are interested in: discovering data shared by others and
sharing their own data in a controlled manner to ensure autonomy and
agency over the data. This is the core functionality that any data space
provides. Additional functions and services such as marketplaces, data
escrow services, processing services and applications might be provided
as optional elements.

![Variants for data space governance authorities](../media/Variants_for_dsga.jpg)