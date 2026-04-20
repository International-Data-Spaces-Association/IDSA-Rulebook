
# Introduction

## Who should read this Rulebook?

This Rulebook is addressed to the broad community of actors who design, build, operate, regulate, or participate in data spaces. That includes private enterprises, public sector organizations, research institutions, standards bodies, and individuals who are responsible for data governance, stewardship, compliance, or innovation. As data sharing assumes an ever more fundamental role in economic activity and public policy, a clear understanding of the principles, requirements and governance models set out here is essential.

The Rulebook offers practical guidance for those working with diverse forms of data sharing — from peer-to-peer sharing and federated ecosystems to data marketplaces and platform-based services. It is especially useful for readers who seek to promote trustworthy, sovereign, and legally compliant data sharing; to manage business risk and contractual governance; and to implement technical architectures that preserve participant autonomy and agency.

## Goals and scope of the IDSA Rulebook

### The purpose and scope of the IDSA Rulebook

The IDSA Rulebook supports the creation, operation, and growth of data spaces by distinguishing mandatory requirements from optional, value-adding practices. Its scope spans technical, commercial, and legal dimensions:

- Common technical guidance, including functional requirements and specifications.
- Recommendations for applying IDSA technical artefacts and for alignment with partner frameworks.
- Operational guidance for collaboration, roles, and processes that enable data space ecosystems.
- Perspectives on implementing and complying with international legal and regulatory obligations to facilitate trusted, cross-border data sharing.

The Rulebook describes how technical roles (for example, Participant and Data Space Governance Authority — DSGA) relate to economic and legal responsibilities, and how these roles may map to obligations under instruments such as the [EU Data Governance Act](https://eur-lex.europa.eu/eli/reg/2022/868/oj/eng), the [EU Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj), and international programms like the [Data Free Flow with Trust (DTFF)](https://www.oecd.org/en/about/programmes/data-free-flow-with-trust.html)

### Goals of the IDSA

<!-- ![Overview IDS enabled ecosystems](../media/Overview_IDS_enabled_ecosystems.jpg)

<span style="color: red;">TODO: We need a new diagram here, replacing the outdated bottom layer of this picture.</span> -->

The International Data Spaces Association (IDSA) aims to cultivate a vibrant practitioner community and to provide concrete guidance that enables the realization of data spaces across a range of capabilities and organisational models.

To that end, IDSA develops the Data Space Requirements (the IDSA Rulebook), the Reference Architecture Models (RAMs), complementary implementation and operations guidance. IDSA also engages with international standardization bodies and open-source initiatives to harmonize and share the knowledge contributed by its members, thereby supporting the global adoption and interoperability of data space technologies and business models.
 
The central objectives for data spaces is the establishment of trustworthiness in data sharing. The [Manifesto of international data spaces](https://docs.internationalDataSpaces.org/ids-knowledgebase/manifesto-for-international-dataspaces/) articulates the fundamental principles that underpin these objectives:

- Data Spaces are a mechanism of Trust (Data Spaces enable Trusted Data Sharing)
- Your Data, Your Choice (Actors shall have full autonomy in deciding with whom they share data with and under what conditions)
- With great responsibility comes great power (Actors shall be responsible for ensuring their freedom to act autonomously)
- Data Spaces are Decentralized & Neutral (All actors shall be treated equitable in their rights and obligations)
- Data does not flow through the Dataspace (Sharing of data is executed on private channels)
- Unity in Standards - Freedom in Implementation (Data Spaces shall be based on international standards)
- There is no single platform to rule them all (Data Spaces shall be infrastructure agnostic)
- Data Spaces are not Data Ecosystems (Data Spaces are building blocks for data ecosystems)
- The opportunity is boundless (Data Spaces shall be business model agnostic)
- Act in good faith, but verify (Actors shall honor all data contracts and its associated policies and verify adherence by others)

These principles provide the foundation for trusted data sharing and for the consequent development of data-driven services and business models.

IDSA specifies foundational requirements and implementable reference architectures that enable organizations of all sizes and sectors to offer, discover, negotiate, and consume data-sharing arrangements for their digital assets.

You can find additional information about data space elements from IDSA in the following sources:

- The IDSA website (<https://www.internationaldataspaces.org>) provides information about our work, use cases, publications and events.
- The IDSA GitHub repositories (<https://github.com/International-Data-Spaces-Association>) host specifications, reference implementation guidelines and an open forum for member collaboration via issues, discussions and pull requests.

## Relationship with other organizations, projects & initiatives

### How Do Initiatives Relate in the field of Data Spaces?
The field of Data Spaces and trusted data sharing is rapidly evolving. As industries, research institutions, and governments seek to collaborate across organizational and national boundaries, the need for interoperable approaches to data exchange has become critical. Multiple initiatives and groups are contributing to this ecosystem, each playing a distinct but complementary role. Together, they create the foundation for standardized, reliable, and scalable Data Space solutions.
This section explains how these initiatives relate to one another, highlighting their contributions to specifications, standards, open-source implementations, and testing frameworks.
It includes organizations, projects or standards that have made a significant contribution to or own a dependency for the IDSA Rulebook. This section will be regularly updated as the ecosystem grows and further contributions are made or when new dependencies arise.

### International Data Spaces Association (IDSA)
The International Data Spaces Association (IDSA) brings together global members from both industry and research. Its mission is to develop and promote the concept of data spaces, covering the full spectrum from legal frameworks and business models to technology foundations.

IDSA provides a unique forum for aligning perspectives across its community. By collecting and structuring requirements, the association ensures that the needs of diverse stakeholders are represented in discussions about data space architecture. The value of this end-to-end perspective lies in its ability to integrate legal, organizational, and technical considerations into a coherent vision. At the technical level, IDSA emphasizes the importance of a common core for specification and standardization. This core is designed to foster interoperability between data space solutions at the protocol level. To achieve this, IDSA aggregates member requirements and channels them into international specification projects (e.g., within the Eclipse Foundation) and formal standardization activities (such as ISO/IEC JTC 1/SC 38 or CEN/CENELEC Joint Technical Committee (JTC) 25).

In short, IDSA serves as the bridge between conceptual discussions, community requirements, and downstream technical specifications.

## ISO/IEC 20151: A Common Foundation
One of the major cornerstones in formal standardization of data spaces is **ISO/IEC 20151, Information Technology – Cloud Computing and Distributed Platforms – Dataspace Concepts and Characteristics**.
This standard provides a clear and authoritative definition of Data Space concepts, distinguishing them from related ideas such as data warehouses, data lakes, data fabrics, or data meshes. By describing the essential characteristics and requirements of a data space, ISO/IEC 20151 reduces ambiguity and helps ensure consistency in design and implementation.
The standard is not only conceptual; it also provides the baseline for interoperability. By establishing common ground, it enables both intra-data space (within a single ecosystem) and inter-data space (across ecosystems) technical compatibility. In doing so, it creates the foundation on which further specifications and open-source implementations can build.

## Dataspace Protocol (DSP) and Decentralized Claims Protocol (DCP)
The Dataspace Protocol (DSP) and Decentralized Claims Protocol (DCP) are two key specification projects that operationalize the concepts defined by IDSA and ISO/IEC 20151.	

- DSP focuses on the communication mechanisms required for trusted data sharing between participants in a data space. 
- DCP addresses decentralized identity and claims management, which are central to ensuring trustworthiness and accountability.

Both protocols are developed under the governance of the Eclipse Foundation, ensuring transparent processes and adherence to rigorous intellectual property rules. While they are rooted in the requirements articulated by IDSA, their development is open to a broad community beyond the association. This open governance model fosters collaboration and ensures that the specifications can evolve in line with real-world needs.

## Eclipse Dataspace Working Group (EDWG)
To coordinate and endorse data space-related efforts, the Eclipse Foundation has established the Eclipse Dataspace Working Group (EDWG).
The EDWG serves several purposes:

- It associates and endorses specification projects like DSP and DCP.
- It provides a governance structure through its committees, which decide on project alignment and associations.
- It supports submissions towards ISO Publicly Available Specifications (PAS), ensuring that community-driven specifications can support international standards, speeding up standardization in response to urgent market needs.

By bringing specifications and open source implementations under one umbrella, the EDWG provides coherence and continuity. It is a key mechanism that, through the participation of its members, it ensures data space technologies remain consistent, interoperable, and aligned with global standards.

## Eclipse Dataspace Components (EDC)
Specifications alone are not enough; they must be validated through implementation. This is where the Eclipse Dataspace Components (EDC) project plays a vital role.
EDC is a reference implementation of both DSP and DCP. It provides a framework for developers to build data space components with a common core and extensibility mechanism. This design allows rapid integration with existing technologies, such as storage systems, vault services, event processing platforms, or policy engines.
Compliance is a central focus of EDC. Each release version of the framework, together with a defined set of core extensions, is tested against a Technical Compatibility Kit (TCK). Successful test results are published openly, ensuring transparency and building trust in the framework’s conformity to the specifications.

For solution providers, EDC offers two key benefits:

- A ready-to-use building blocks, forming an extensible foundation for data space components.
- Confidence that their solutions can achieve compliance with DSP and DCP with minimal integration cost.

## Technical Compatibility Kit (TCK)
The Technical Compatibility Kit (TCK) is the backbone of compliance verification. It is a test harness and collection of tools designed to automate the validation of data space implementations against DSP and DCP.
By leveraging shared core libraries, the TCK provides comprehensive tests that cover protocol compliance and interoperability scenarios. Solution providers can run their implementations against the TCK to obtain evidence of compliance. Passing results serve as an objective and transparent proof that a solution adheres to the agreed specifications.

The availability of the TCK ensures that the ecosystem does not fragment into incompatible variants. Instead, it promotes trust and interoperability, which are prerequisites for scaling Data Space adoption across industries and borders.

### The Data Space Landscape

#### Data Space Connector Report
The [Data Space Connector Report](https://internationaldataspaces.org/idsa-data-space-connector-report/) is a key regular publication from IDSA offering a comprehensive overview of Data Space Connectors and their role in interoperable data spaces.

In particular, the Data Space Connector Report:

- highlights the importance of Data Space Connectors, explaining what they are and why they are a key element in data spaces.
- it provides a summary of all the key requirements to make Data Space Connectors interoperable (e.g. relying on standards, having clear specifications, enabling semantic interoperability via the Data Catalog Vocabulary (DCAT) and specific vocabularies, etc.) based on the Dataspace Protocol.
- it gives visibility to existing connector implementations, provides details about them and follows their evolution over time.
- it is the reference point for learning and fostering interoperability in data sharing ecosystems.

#### Data Spaces Radar
The [Data Spaces Radar](https://internationaldataspaces.org/use/data-spaces-radar/) serves as the central repository for all data space endeavors. It is an accessible tool designed to provide a comprehensive view of various data space initiatives worldwide. Offering insights into the 18 different sectors, global expansion, technical transparency and new stages of development of the data spaces featured in the radar.

## How to contribute
The IDSA Rulebook is published under the [CC-BY license](https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/blob/main/LICENSE.md). If you wish to contribute, please take a look at our [Contribution Guidelines](https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/blob/main/CONTRIBUTING.md). Please take our [Code of Conduct](https://github.com/International-Data-Spaces-Association/IDSA-Rulebook/blob/main/CODE_OF_CONDUCT.md) into account.

