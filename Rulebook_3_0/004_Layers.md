# Understanding Participants, Roles and Layers in Data Spaces

Data spaces are multi-layered data ecosystems that rely on the seamless integration of technical protocols & components, business processes, and legal frameworks. One of the foundational challenges in governing data spaces lies in the consistent definition and use of key concepts such as **"roles," "policies,"** and **"contracts."** These terms often carry different meanings in different layers and across domains. This chapter establishes a clear separation between technical and non-technical interpretations of such concepts to support the development of interoperable data spaces.

## Layers of a Data Space

Data spaces can be structured into three primary layers, each serving distinct functions:

### Technical Layer
Encompasses the architecture and protocols (e.g., Dataspace Protocol (DSP), Decentralized Claims Protocol (DCP)) that facilitate trusted and interoperable data sharing. Software agents, representing the participants of the data space, form a decentralized mesh of autonomous nodes.

### Economic Layer
Manages the services, interactions, and workflows that enable value generation. Alternative terms for this layer are also *Business* or *Operational Layer*.

### Legislative Layer
Enforces rights, obligations, and regulatory compliance across participants. Alternative terms for this layer are also *Regulatory* or *Governance Layer*.

While at the technical layer all participants are equal the layers building on top can lead to segmentation into individual communities as described in the chapter [What is a Data Space - Communities](003_WhatIsADataspace.md#communities)

![Layers of Data Spaces](./media/Layers.png)

These layers interact but must be conceptually separated to ensure clarity and reduce ambiguity in roles and responsibilities.

## Clarifying the Concept of Roles

The term **"role"** is context-dependent and must be clearly scoped:

- At the **technical level**, there is only one fundamental role: **participant**. 
    
    A participant acts as a **data provider**, a **data consumer**, or both within the Dataspace Protocol.

- At the **business level**, participants may take any role relevant for the business context.

    This includes roles such as **data intermediary**, **marketplace operator**, **auditor**, or **service provider**, but also explicitly the **data provider** and **data consumer** role in the context of the business transcation.

    These business roles do not exist at the technical layer but are mapped onto the core participant role based on the actions performed and services offered.

Maintaining this distinction ensures that governance models remain technically sound while accommodating diverse business scenarios.

## Distinguishing Data Spaces from Trusted Data Transactions

A clear differentiation must be made between **Data Spaces** and **Trusted Data Transactions (TDTs)**:

- **Data Spaces** are decentralized environments that enable participants to share data while ensuring their autonomy and agency. See the chapter [What is a Data Space](003_WhatIsADataspace.md) for details.

- **Trusted Data Transactions**, as under current standardization in the European Commission's Standardization Request on a Trusted Data Framework in CEN/CENELEC JTC 25, can also be  associated with the EU *Data Governance Act*. They can also be related to data intermediaries and service orchestration. Such models prioritize regulatory alignment and controlled environments.

While TDTs may operate within data spaces, they are conceptually distinct. Equating them risks narrowing the scope of data space implementations and excluding more decentralized or peer-to-peer configurations. Data spaces designed, built and operated according to the IDSA Rulebook enable the implementation of TDTs but don't mandate it. Also the implementation of a TDT is not dependent on the use of a data space. Both are independent concepts that can be used at the same time.

## Participation and Representation

Participants in a data space are defined by their ability to automate the negotiation and execution of data sharing agreements via technical protocols. This has several implications:

- **Organizations**, not individuals, are considered technical participants. These organizations are represented by **software agents** capable of executing standardized data space protocols.

- **Natural persons** interact with data spaces indirectly through applications or services operated by organizations. Their participation is strictly limited to the Economic and Legislative Layer. Software agents can represent a natural person but not impersonate it.

- As data spaces are fully decentralized and participants are responsible for their own **decentralized identity (DID)** there are **no identity providers** in a data space. Participants provide proof of their identity to others through the use of claims (e.g. expressed through verifiable credentials) and not through a common identity provider. Access to resources is managed through authentication tokens issued directly by the participants sharing those resources.

## The Role of External Actors

Entities that provide static resources (such as ontologies, schemas, or public credentials) may support the data space but are not considered participants unless they actively engage via governed interfaces implementing the standardized data space protocols. For example:

- A web service that hosts a data sharing ontology is not a participant but serves as an **external reference**.

- A dataspace trust framework provider usually acts as an external reference. However, it may act as a **participant** if it delivers services subject to data space governance policies provided through an implementation of standardized data space protocols.

- **Trust anchors**, **regulators** and similar legal entities may influence data transactions but do not participate directly unless they act through technical interfaces governed by data space rules. Most commonly they provide external services which are referenced in the data space (e.g. common data lookup services, registries, etc...)

This model guarantees the adherance to the governance model and thus supports trust while preserving digital sovereignty of each participant and the integrity of technical interactions. Flexibility is created through processes in teh economic layer which supports extensive customization. There is no mandatory central or federated service that can restrict the autonomy and agency of an organization.

Participation requires **governance commitment** and **technical integration**.

## Implications for the Rulebook

The Rulebook reflects these principles clearly:

- The only **technical role** is the **participant**, which may act as data provider, consumer, or both.

- **Business roles** are supplementary and must be defined within the economic or legal governance layers.

- **Clarity:** Visual representations and descriptions in the IDSA Rulebook must be clearly labeled to indicate whether they depict technical, business, or legal perspectives.

Such clarity supports interoperability, ensures accurate alignment with regulatory frameworks, and promotes broad adoption across sectors.

## Overview on roles and Layers

In line with the description of the [role models](005_Roles.md) and the [layered approach](#layers-of-a-data-space), the diagram below presents an overview on roles in data spaces and their affilation to the layers.

![Overview on roles and their affiliation to layers in data spaces](./media/Role%20Overview%20Rulebook.jpg)

This diagram is a foundation to depict the typical use cases of the roles in relation to data spaces. 

## Conclusion

Effective data space governance depends on the precise use of terminology and clear separation of concerns across layers. Establishing the **participant** as the core technical role, while accommodating richer business and regulatory interactions above it, ensures a scalable and interoperable foundation. This layered perspective will guide the elaboration of rules, responsibilities, and interactions in subsequent chapters of the Rulebook.