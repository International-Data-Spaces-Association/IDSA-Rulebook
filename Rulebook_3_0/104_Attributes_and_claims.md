# Attributes & Claims



To create trust in a data space a very similar process is used. It is
necessary to evaluate attributes of participants and match them with the
requirements, policies and rules of the data space, the participants,
and individual data contracts.

A data space needs to define policies that specify what attributes an
applicant must meet to become a trusted participant. This is achieved
through a data space self-description (DSSD), that allows new members to
provide attributes in their participant self-description (PSD) in a
format that can be understood by the data space governance authority (DSGA).
Therefore, the DSSD must include a reference to a semantic model that
describes the acceptable policies, their names, the potential value, and
the format in which those values are accepted.

For example, one data space might require self-descriptions to be
expressed as verifiable presentations in a single presentation per
attribute, while another data space might require self-descriptions to
be expressed as one large file containing all information serialized as
JSON-LD for the attributes and corresponding signatures. While
participants might manage the values of the PSD through application
services which enable complex data management and a permissions system
for editing, these services must render the self-descriptions in the
desired format that each data space requires at an appropriate service
endpoint for that data space.

Trust in a data space needs to be rooted in one or more trust anchors
and trust frameworks. These are similar to mechanisms that citizens use
in their daily lives: The level of trust depends on the authority that
issues them, such as a department of traffic issuing drivers licenses or
a ministry of internal affairs handing out citizen ID cards. The
underlying process is verifying a specific attribute.

![Self Descriptions in data spaces](../media/Self_Descriptions_in_data_spaces.jpg)

A trust anchor
is an entity that issues certifications about an attribute. The
accompanying trust framework is the set of rules imposed by the trust
anchor to comply with its policies. Only then is the applicant eligible
for its attribute verification. For example, a company must follow the
laws of the country it is based in to obtain a valid company registry ID
issued by its government.

Deciding which trust anchors and trust frameworks, and thus which rules
and procedures of issuing and validating attributes are used, is the
responsibility of the DSGA and of the participants of the data space.
Details can be found in the certification section. For the data space
functionality, the concepts of trust anchor and trust framework form the
basis for the attribute-based trust mechanism.

In order to use of the concepts described above, the DSSD needs to
contain information about which trust anchors and trust frameworks are
accepted as roots of trust. Is it a sovereign entity that is the sole
root of trust, or is it embedded in a larger ecosystem of external trust
anchors and trust frameworks? Based on this, a potential participant can
make the decision whether to trust the data space and its members or
not.

The DSGA is also responsible for issuing membership credentials. It
ensures that an appropriate mechanism is provided for identifying and
verifying membership. In a centralized data space this could be the
issuance of a data space specific identity to interact with other
members. In a largely decentralized architecture, it could be the
issuance of a tamper-proof credential, such as a W3C verifiable
credential (VC) which provides proof of the attribute of membership.

The DSGA also performs other functional roles not directly related to
building trust but necessary for the operation of a data space. These
are primarily the mandatory function of regulating the lifecycle of
membership (participant discoverability, issuing of membership
credentials, verification services for membership proofs), but also many
optional services like observability and auditing, brokering and
marketplaces, providing vocabularies or other services required by the
data space members.

The communities coming together in the data space needs to make
decisions for the setup. Whether a centralized DSGA is required, or a
more federated or even fully decentralized model is appropriate must be
reasoned over when the data space is founded, as these architectural
choices are very hard to change later. Where on this spectrum of
possibilities an optimal design for a data space can be found depends on
the context and purpose of the data space.

#### Participant information

Information about a participant must be discoverable and understandable
for other participants - also to enable a clear understanding of the
attributes of the participant. Therefore, a participant needs a
participant self-description (PSD) that follows a known format and
protocol, as well as an ontology that describes the semantics of the
attributes.

The format of the PSD can be defined through the DSGA and may be a part
of the membership policies for the data space. In many cases, the format
and ontology of the PSD also depend on the selected trust anchors and
trust framework. For example, a data space that wants to use Gaia-X as a
trust anchor and leverage its trust framework must understand the Gaia-X
self-description structure and the meaning of the Gaia-X
self-description attribute definitions. A data space might require
multiple self-description ontologies (e.g., one trust anchor specific
and one industry specific) which can lead to ambiguity or conflict of
definitions, which have to be resolved by the DSGA.

The technical representation and communication of the PSD may vary from
one data space to another and will be influenced or mandated by the
trust anchor(s). One trust anchor and its trust framework might require
attributes to be presented as verifiable presentations when queried,
while another might require the possibility to request a set of
attributes serialized in a specific resource description format, and a
third one might require that all attributes be made discoverable in a
database that's available to all members for query at any time.

Entities that are participating in multiple data spaces at the same time
must manage their self-description attributes in a way that reliably
keeps attributes up to date, but also filters which ones should be
available in which data space and serialized in which format. For larger
enterprises with complex roles and responsibilities related to the
information contained in the attributes, this might include approval
processes and audit functions to track value changes to sensitive
attributes exposed by the self-descriptions.

Information exposed through participant self-descriptions (PSD) is used
in many policy evaluations throughout the data space. A non-exhaustive
list of examples is:

- Information for the registration process to evaluate whether an
    applicant can become a participant.

- Matching participant attributes to access catalog policies to only
    show items this participant is permitted to see.

- Automated matching of attributes to policy requirements in the
    contract negotiation process.

Self-descriptions can also be used to convey purely technical
information about a participant. For example, at what address can
another participant communicate with its catalog or connector with this
participant, what encryption techniques are supported. Whether this
information is stored and distributed in the same way as the PSD is a
question of the data space design. A data space that is using
centralized components for all mandatory functions will not require a
per participant discovery mechanism, while a more decentralized design
will require some discovery functions that can be implemented through
the same mechanism as the PSD or possibly through separate protocols.
