# Attributes & Claims

As described in the section [Establishing Trust](103_Establishing_Trust.md) Attributes are expressed by Claims that contain Evidence about those Attributes. Matching them to [Policies](105_Policies.md) and verifying that the desired conditions have been met creates trust. 

>**Attributes** describe a participant and are presented to other participants as claims. A **claim** is a **credential**, which must be verified by cryptographic means that it has been issued by a specific party. This issuing party thus acts as a root of trust and is a **Trust Anchor** for this claim. 

>**If a verified claim and its trust anchor are accepted, evidence about the attribute has been established.**

Each credentials must be verifiable, which means it needs to be rooted in one (or more) trust anchor(s). This is a mechanisms that citizens of every country use in their daily lives: Trust depends on the authority that issues them, such as a department of traffic issuing drivers licenses or a government issueing citizen ID cards or passports. The driver license contains the information, like date of birth and name of the holder, but what makes this information trustworthy is the believe that it is not a fake id but one issued by a trusted organisation, the department of traffic. Digital credentials have a big advantage versus the analog examples used here: it can be cryptographically verified whether they are real or fake.

Using a trust anchor does not imply dependence on a single central authority. Participants, together with the DSGA and the applicable DTFs, define which trust anchors are acceptable. Multiple anchors may be accepted to preserve decentralization and choice; the DTF and DSGA should document acceptable anchors and any validation procedures.

A trust anchor is an entity that issues certifications about an attribute. dataspace trust frameworks often contain a list of credential issuers which are accepted as trust anchors for that DTF.

Trust anchors are well known by the DTF, DSGA or Participant accepting them for their capability to verify attributes and for being trustworthy that they enforce compliance with the party that they issued a credential for. For example, a company must follow the laws of the country it is based in to obtain a valid company registry ID issued by its government. Therefore the goverment of this country can act as the trust anchor for company registration information.

Deciding which trust anchors, and thus which rulesand procedures of issuing and validating attributes are used, is the responsibility of each participant and can be greatly simplified by the [DSGA](006_DSGA.md) and the DTFs.

In order to use of the concepts described above, every individual data sharing contract needs to provide information about which trust anchors are
accepted as roots of trust. This can be done by pointing to DTFs as a shortcut for multiple policies. See the section on [policies](105_Policies.md) for more details.


## Participant information

Information about a participant must be discoverable and understandable
for other participants - also to enable a clear understanding of the
attributes of the participant. Therefore, a participant needs to be able to provide a self-description that follows a known format and
protocol, as well as a semantic model that describes the meaning, naming and formt of the attributes.

The format of the self-description can be defined through the onboarding process for a specific data space and may be a part of the membership policies. In many cases, the format and semantic model of the self-description also depend on the selected trust anchors and DTF. 

A data space might even require multiple self-descriptions (e.g., one trust anchor specific and one industry specific) which can lead to ambiguity or conflict of definitions, which have to be resolved by rules provided by the DSGA.

The technical representation and communication of the self-description thus may vary from one data space to another and will be influenced or mandated by the
DSGA. 

Entities that are participating in multiple data spaces at the same time
must manage their self-description attributes in a way that reliably
keeps attributes up to date, but also filters which ones should be
available in which data space and serialized in which format. For larger
enterprises with complex roles and responsibilities related to the
information contained in the attributes, this might include approval
processes and audit functions to track value changes to sensitive
attributes exposed by the self-descriptions.

Information exposed through participant self-descriptions is used
in many policy evaluations throughout the data space. A non-exhaustive
list of examples is:

- Information for the onboarding process to evaluate whether an
    applicant can become a participant.

- Matching participant attributes to access catalog policies to only
    show items this participant is permitted to see.

- Automated matching of attributes to policy requirements in the
    contract negotiation process.

Self-descriptions can also be used to convey purely technical
information about a participant. For example, at what address can
another participant communicate with its catalog or software agent with this
participant, what encryption techniques are supported. Whether this
information is stored and distributed in the same way as claims about attributes is a question of the data space requirements and tools used. 