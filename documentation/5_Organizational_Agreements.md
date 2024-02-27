# Organizational agreements

## Certification

Trust is *the* essential element in data spaces to overcome the
reluctance to share data for fear of misuse and security concerns.

Functional requirements are an element of trust and are investigated
from the functional perspective, clarifying responsibilities and
mechanisms in Chapter 3. This chapter discusses the operational
implications using IDS Certification as an example.

Chapter 3 mentions two important aspects: The first is the data space
authority (DSA), which ensures trust in a data space. The second is the
system enabling it, the attribute-based trust mechanism, which is based
on the fundamental concepts of trust anchor and trust framework. The
first term refers to the entity that issues certifications about an
attribute, the second to the rules imposed by the trust anchor to comply
with its policies in order to be eligible for its attribute
verification. Deciding which trust anchors and trust frameworks and,
therefore which rules and procedures to use for issuing and validating
attributes, is the task of the data space authority.

Based on the trust framework(s) selected, each data space specifies the
minimum set of attributes that a participant must meet to be considered
a trusted party (see also the data space self-description mentioned in
Chapter 3). Based on this, each new potential member has to provide
these attributes in its participant self-description to be accepted.

The DSSD must also contain clear information on which trust anchors and
trust frameworks are acceptable as roots of trust within the data space,
so a potential participant can decide whether to trust the data space
and its members.

### The example of IDS Certification

For the scenario described above, the IDS Certification Scheme developed
by the IDSA is one available trust framework.

The trust anchor of this framework is called certification body and is a
neutral party issuing certification for specific attributes. The
responsibility for the certification body is taken on by a part of the
IDSA head office and by additional experts hired specifically for this
purpose. There are two attributes in the IDS Certification trust
framework: component certification and operational environment
certification.

Component certification concerns all components described in the
IDS-RAM, both essential and non-essential, and ensures their required
functionality and security. Operational environment certification refers
to the trustworthiness of the physical environment in which the
components run, as well as the processes and organizational rules there.

Both types of certifications have different options to meet the data
sharing needs of companies. These options refer to the trust levels,
which reflect the extent of functionalities and requirements covered,
and to the assurance levels, which refers to the method to evaluate
compliance. The simplest assurance levels are based on a self-assessment
mechanism, while the more advanced assurance levels require a
third-party assessment of components or operational environments. This
third-party compliance check is performed by the evaluation facilities,
which are specifically approved to offer this service. The approval
process is defined by the IDSA certification working group.

All the details on the IDS Certification scheme, the trust and assurance
levels for component certification and operational certification, the
certification criteria, and the process to approve the evaluation
facilities are provided in Chapter 2.

## Running data space instances

### Intra- and inter data space instance governance

It must be recognized that the role of IDS and IDSA is to fulfill

1. within the broader landscape of existing data sharing initiatives and
2. the ambition of a federation of interoperable data spaces.

This implies that IDSA considers its development and deployment initiatives
in the broader context of these two areas:

The striving for interoperability within a data space (intra) so that
IDS can provide a gradual migration path within a data space instance or
data sharing initiative and preparing for interoperability between
multiple data space instances or data sharing initiatives (inter) to
pave the way for the federation of interoperable data spaces - as
pursued by the European data strategy.

The [Data Governance Act](https://digital-strategy.ec.europa.eu/en/policies/data-governance-act) also recommends both an intra data space
(domain) governance authority and an inter data space (central)
governance authority.

'The recently proposed [Data Governance Act](https://digital-strategy.ec.europa.eu/en/policies/data-governance-act) confirms the notion of
a governance structure constituted by multiple entities. For European
data spaces, it is recommended to have a (domain) governance authority
for each data space and a central governance authority overseeing all
aspects in connection with interoperability of data spaces, i.e., the
de-facto 'soft infrastructure'. This central authority will interact
with all data space specific authorities.'

As noted above, IDSA and the main IDS-stakeholders play an important
role by working together to ensure the development and deployment of
data space instances in the broader context of introducing new or
migrating/ developing existing data sharing initiatives, (intra data
space interoperability), and embedding them in the European ambition of
a federation of interoperable data spaces (inter data space
interoperability).

![Relationship of OpenDEI Building
Blocks and data space instances](media/media/image18.png)

This structure of a data space reflects the role of the IDS data space
framework in relation to the broadly used data sharing agreement
framework that is emerging as the cloud processing framework, as shown
on the right in Figure 1:

An approach to systematically address the interoperability challenges is
provided by the [new European interoperability framework](https://ec.europa.eu/isa2/eif_en/) developed by the
European Commission and shown in the figure below.

![Layered functional model as aligned
with the New European Interoperability Framework ](media/EuropeanInteroperabilityFramework.png)

As shown in the figure above, the framework distinguishes four functional levels
under an overarching integrated governance approach:

- *Technical level,* to provide software and hardware components for
    controlled, sovereign and secure sharing of data.

- *Semantic level,* to ensure that format and meaning of shared data
    is preserved and understood.

- *Organizational level,* to let stakeholders align goals,
    expectations, responsibilities, and business processes.

- *Legal level,* to make sure that organizations under different legal
    jurisdictions and frameworks can share data with common legally
    binding conditions.

Governance on the identified topics distinguishes between two
development lines for data space instances:

- *Intra data space interoperability,* between the data space
    authority, processing, and data sharing building blocks within a
    single data space instance.

- *Inter data space interoperability,* between multiple data space
    instances at each of the functional levels as distinguished in the
    framework shown in Figure 2.

To enable interoperability between data spaces, each of the functional
levels shown contains topics that require adequate
governance. For each of the levels, these topics are identified in the
following paragraphs. Their governance aspects are addressed in the next
chapter.

In general, the participant in a data space covers the technical and
semantic interoperability aspects, while the Data Space Governance
Authority defines the organizational and legal aspects.
Based on the governance scheme, the participants participate in the
defintion of the policies and rules of a data space, including the
framework or agreements on all four levels.

### Technical level

The technical level covers the software and hardware components for
controlled, sovereign and secure sharing of data. It consists of five
sublevels with the topics that require adequate governance:

### Governance instruments

The various governance instruments that may be considered by the IDSA
are listed in the Table below. These governance tools each describe a
different aspect of a certain activity and are used in the next section
to provide a multidimensional overview of the intra and inter data
spaces governance.

| **Governance Instrument** | **Governance instrument description**      |
|--------------------------------- |---------------------------------|
| *Standardization* | Ensuring that the tasks, processes, and guidelines around this activity are formalized, documented, and  aligned between data spaces instances and the IDSA. The standardization efforts can generally be used as a  blueprint or starting point for the stakeholders.|
| *Certification* | Validating that stakeholders act according to the standardized way of working. Certification is divided into component certification (certification of technical/software components) and organizational certification (organizational and legal processes).    |
| *Development* | The activity may require (software) development tasks as part of the realization, which should be compliant with the standardization activities and best followed by a certification. |
| *Operations*           | The operations are about the exploitation and usage of the developed components. The operations can be certified as part of the organizational certification. |
| *Communication*        | The dissemination of the activity is an important aspect which might include the awareness of the standardization and certification, but also contains marketing aspects. |
| *Support*   | The support activities include the structured assistance from stakeholders involved in the operation, development, certification, and communication activities. |

### Governance for inter data space interoperability

> update text

There will be no single data space. Individual sectors or communities
are expected to develop their own data space instances. Being able to
seamlessly share data over these data space instances brings clear
benefits. It extends the reach and scope of accessible data and allows
the development of new business models and services across sectors and
regions. Interoperability between data space instances adds major value,
resulting in a federation of interoperable data spaces.

The federation of data spaces require a common set of reusable standards
and technologies for the data spaces to adopt to become interoperable.
Furthermore, data spaces need to harmonize and accept common policies and
rules to be able to federate with each other.

### Conclusions

The now completed European [OPEN DEI](https://www.opendei.eu/) project aimed at defining the building blocks and standards for data
spaces, to realize interoperability between the building blocks within
specific data space instances (intra data space interoperability) and
between various data space instances (inter data space
interoperability).

The important role of IDSA and the IDS-stakeholders is to provide the
governance for data space instances in the broader context of:

> -the introduction of new or migration/ evolution of existing data
> sharing initiatives, intra data space interoperability
>
> -the embedding within the European ambition of a federation of
> interoperable data spaces and inter data space interoperability.

The [Data Spaces Support Centre (DSSC)](https://dssc.eu/) as a funded project by the
European Commisson, has the aim to provide a Blueprint for data spaces
based on the OPEN DEI Building blocks. The DSSC Blueprint contains legal,
organizational, business, and techncial building blocks. This structure shall
support in the creation of interoperable data spaces, addressing the needs
of inter- and intra data space interoperability.
