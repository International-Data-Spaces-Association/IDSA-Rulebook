# IDSA Rulebook WG — International Perspectives: Europe

| | |
|---|---|
| **Status** | Working draft for publication, v1.0-draft |
| **Date** | 23 June 2026 (regulatory content reflects status as of this date) |
| **Maintainers** | IDSA Rulebook Working Group, International Perspectives subgroup |
| **Licence** | CC BY 4.0 (aligned with the IDSA Rulebook) |
| **Contributing** | Corrections and proposals via GitHub issues and pull requests. Open questions in Section 9 are tracked as issues in this repository. |

> **Note.** This annex is analysis produced by the IDSA Rulebook Working Group. It does not constitute a formal IDSA policy position. For IDSA positions on specific regulatory files, see the position papers referenced throughout.

## 1. Overview

Europe has taken a regulatory-driven and sovereignty-oriented approach to data spaces, combining industrial policy, legal harmonisation, and technical standardisation. This annex provides region-specific guidance on implementing IDSA principles within the context of EU regulatory requirements, established trust frameworks, and coordinated initiatives.

Understanding the European data spaces landscape requires navigating multiple layers: legal frameworks (e.g. Data Act, Data Governance Act, AI Act), technical standards and infrastructures (e.g. CEN-CENELEC, Gaia-X), governance models (e.g. iSHARE), and sector-specific implementations (e.g. European Health Data Space). This document maps these elements to help organisations build interoperable, compliant data spaces aligned with both the IDSA Rulebook and European expectations.

## 2. Key Initiatives and Infrastructure

Europe's data space ecosystem is characterised by multi-actor coordination rather than single-platform dominance. The European Data Spaces Landscape is growing rapidly with numerous initiatives, standards, frameworks, and tools being developed and used. Some initiatives have a regional focus, while others have their focus on a global level; some focus on specific domains, while others aim to develop industry-wide standards. This section outlines key initiatives in the context of European data spaces.

### 2.1 Governance and Reference Frameworks

| Initiative | Role |
|---|---|
| IDSA (IDS-RAM & Rulebook) | Reference architecture and governance framework for data spaces: defining how data space participants, data space governance authorities, connectors and ecosystems should operate. Note: IDSA forms the normative basis for most European data space initiatives. |
| Gaia-X Association | Provides data governance models, trust framework, and interoperability guidance. Gaia-X solutions are frequently combined with IDS standards to build sovereign data spaces. |
| Data Spaces Support Centre (DSSC) | EU-backed support and coordination hub: publishes blueprints, building blocks, starter kits and toolboxes; fosters interoperable data spaces across sectors and supports implementers (e.g. SMEs, public sector). The DSSC continues in its second phase in 2026 with IDSA remaining a member of the consortium. |

### 2.2 Technical Infrastructure and Building Blocks

| Initiative | Role |
|---|---|
| SIMPL | SIMPL (Smart Middleware Platform) is a European Commission initiative that provides a cloud-to-edge middleware platform to support the implementation of sectoral data spaces. It aims to offer reusable technical building blocks complementing governance and reference frameworks such as IDSA and Gaia-X in the European data space ecosystem. |
| iSHARE trust framework | Provides a standardised trust / identity / access / authorisation layer, enabling controlled, sovereign data sharing across participants. |

### 2.3 Ecosystem Coordination

| Initiative | Role |
|---|---|
| Big Data Value Association (BDVA) | European industry-driven association that promotes data-driven innovation and artificial intelligence across sectors. In the context of data spaces, BDVA has helped align industrial requirements, reference architectures, and standardisation efforts. |
| European Data Innovation Board (EDIB) | Advisory body coordinating data space strategies across EU Member States. The pending Digital Omnibus package (see Section 3) proposes strengthening the EDIB's coordination role for consistent application, interoperability, and data space governance. |

### 2.4 Common European Data Spaces (CEDS)

The most concrete expression of the European approach is the family of Common European Data Spaces announced in the 2020 European Strategy for Data and funded primarily through the Digital Europe Programme (with complementary support from Horizon Europe and sectoral programmes such as EU4Health). Fourteen sectoral and domain data spaces are currently being developed. Many of them follows the same general pattern: a preparatory/coordination action to map the ecosystem and define building blocks, followed by a deployment action, but they are at markedly different stages of maturity, and one (health) is backed by dedicated legislation. The Data Spaces Support Centre provides the common blueprint and coordination across all of them, and SIMPL provides shared middleware.

Status summary as of June 2026:

| Data space | Status (June 2026) |
|---|---|
| Health (EHDS) | The most advanced CEDS and the only one with its own regulation: the European Health Data Space Regulation was published in March 2025 and applies in stages, with key primary- and secondary-use obligations phasing in from 2029. Supported by the TEHDAS2 joint action and EU4Health funding alongside Digital Europe. |
| Mobility (EMDS) | Commission Communication (November 2023) defines the approach: a federating framework rather than a central database. Preparatory action PrepDSpace4Mobility completed 2023; the deployment action deployEMDS runs to October 2026, implementing use cases in traffic and urban mobility. |
| Energy | Deployment underway following the 2024 Digital Europe call (ENERSPACE), building on preparatory projects and the EU Action Plan on digitalising the energy system; focus on grid balancing, flexibility, and integration of renewables. |
| Manufacturing / Industrial | Deployment stage via the 2024 Digital Europe call (MANUFSPACE), closely linked with industry initiatives such as Catena-X and Manufacturing-X that already operate at scale in the automotive supply chain. |
| Agriculture | Preparatory action (AgriDataSpace) completed; deployment phase in progress under Digital Europe, building on national agricultural data-sharing initiatives. |
| Green Deal | Deployment call issued 2024 following the GREAT coordination action; interlinks with Destination Earth (DestinE) digital twins and the GreenData4All initiative for environmental data. |
| Cultural heritage | Operational. Run by the Europeana Foundation-led consortium; a data space strategy for 2025–2030 has been published, with priorities including 3D/XR content (the "Twin it!" campaign) and re-use in education and tourism. |
| Media (TEMS) | Deployment stage: the Trusted European Media Data Space (TEMS) has been deploying trials across media provenance, content exchange, AI services, and delegated publishing since 2024. |
| Language | Deployment ongoing through the Language Data Space, complemented by the Alliance for Language Technologies EDIC (ALT-EDIC), a direct input to European AI development. |
| Tourism | Preparatory action (DATES) completed; deployment of the European Tourism Data Space in progress. |
| Skills | Preparatory action (DS4Skills) completed; deployment phase under Digital Europe connecting education, training and labour-market data. |
| Research & Innovation (EOSC) | The European Open Science Cloud predates the CEDS framing and is the most operationally mature federation: the EOSC EU Node has been live since 2024, with a federation of national and thematic nodes building out. |
| Finance | Legislative-led rather than deployment-led: the proposed Financial Data Access (FiDA) Regulation, in negotiation, would establish the open-finance framework on which a financial data space builds. |
| Public administrations | Multiple strands rather than a single space: the Public Procurement Data Space (PPDS) is live for EU-level procurement data, complemented by the Interoperable Europe Act framework for public-sector interoperability. |

Three observations are relevant for Rulebook readers. First, the maturity spread is wide: from a regulation in force (health) and operational federations (cultural heritage, EOSC) to spaces still in preparatory transition. This means that "the CEDS" should never be treated as a single homogeneous state of play. Second, the governance models differ: some spaces are legislation-anchored (health, finance), some are consortium-operated (cultural heritage, media), and some are federations of national initiatives (mobility, agriculture). Third, cross-CEDS interoperability is now the frontier question: the EDIB, DSSC and SIMPL exist precisely to prevent fourteen sectoral silos from re-creating the fragmentation data spaces were meant to solve. This connects directly to the federation question in Section 9.

Reference: [Common European Data Spaces — European Commission, Shaping Europe's Digital Future](https://digital-strategy.ec.europa.eu/en/policies/data-spaces)

## 3. Legal and Regulatory Dimension

The European approach to data spaces is strongly shaped by a regulatory framework that actively defines the conditions for trusted data sharing. Unlike purely market-driven models, the European Union uses legislation to shape market behaviour, establish common rules, and create predictable conditions for cross-sector data exchange. Key regulatory instruments define governance roles, responsibilities, and rights related to data access and use, thereby providing legal clarity for participants in data sharing ecosystems.

Key regulations which influence European data sharing are:

- **Data Act:** Rules for fair access to and use of data, particularly from connected products and related services; data spaces can operationalise these requirements by enabling secure, interoperable, and policy-controlled data sharing. Applicable since 12 September 2025.
- **Data Governance Act:** Establishes a framework for data intermediaries, data altruism, and public sector data reuse. Focuses on data intermediaries and defines neutral third-party roles aligned with data space governance authorities (DSGAs).
- **AI Act:** High-risk system governance requires structured risk management, documentation, human oversight, and traceability throughout an AI system's lifecycle. Data spaces can support these obligations by providing trusted data provenance, controlled access, and auditable policy enforcement across participating organisations.
- **GDPR:** Foundational; data spaces must implement technical and organisational measures for lawful processing.
- **NIS2 Directive:** Cybersecurity requirements for essential and important entities; affects data space operator security baselines.
- **eIDAS 2.0:** European Digital Identity Wallet; enables cross-border participant authentication. Member State wallet availability obligations fall due in 2026.

The focus of European legislation lies also on the clear definition of Data Space Governance Authorities and Data Intermediaries.

### Regulatory developments in flight (status: June 2026)

The Digital Omnibus package, proposed by the European Commission on 19 November 2025 as part of the EU's simplification agenda, proposes targeted amendments to several of the instruments listed above, including the GDPR, ePrivacy, Data Act, Data Governance Act, AI Act, NIS2 and DORA. It consists of two files moving at different speeds:

- The **Digital Omnibus on AI** adjusts AI Act implementation timelines, particularly for high-risk obligations, and is expected to complete adoption first.
- The **Digital Omnibus on data** remains in negotiation between the co-legislators. Proposals relevant to data spaces include a strengthened coordination role for the European Data Innovation Board (EDIB), a shift of the DGA data-intermediation regime towards a voluntary EU label with EU-level registers, single-entry-point incident reporting across GDPR/NIS2/DORA, and a contested recalibration of the definition of personal data (on which the EDPB and EDPS issued a critical Joint Opinion in February 2026).

Readers should treat the descriptions of the DGA intermediation regime and AI Act timelines in this annex as subject to change and consult the current legislative state. This box will be updated as the package progresses.

Related IDSA and DSSC materials:

- IDSA paper on the AI Act and Data Spaces: [Data Spaces for the AI Act](https://internationaldataspaces.org/wp-content/uploads/dlm_uploads/IDSA-Position-Paper-Data-Spaces-for-the-Al-Act-1-1.pdf)
- IDSA reflection paper on the DGA and Intermediaries: [Reflections on the DGA and Data Intermediaries](https://internationaldataspaces.org/wp-content/uploads/Reflections-on-the-DGA-and-Data-Intermediaries.pdf)
- DSSC explanation of Data Space Governance Authorities: [Organisational Form and Governance Authority — Blueprint v1.0](https://dssc.eu/space/BVE/357074549/Organisational+Form+and+Governance+Authority)

## 4. Data Sovereignty and Data Space Governance

The European approach to data spaces is strongly shaped by the concept of data sovereignty, which has become a central objective of European digital policy. Rather than focusing on data ownership or localisation, European data sovereignty emphasises decisional autonomy, i.e. the ability of organisations to retain meaningful control over how their data is accessed, shared, and used. This objective is embedded in a growing body of EU legislation, including the Data Act and the Data Governance Act, which seek to create trusted conditions for data sharing while safeguarding the rights and interests of data holders and data subjects. Within this framework, data spaces serve as governance-enabled infrastructures that allow participants to collaborate while maintaining control over their data assets.

A key element of the European model is the prevention of platform lock-in and structural dependency. European data space initiatives aim to avoid situations where participation in a data ecosystem requires reliance on a single technology provider, platform operator, or identity broker. Instead, data spaces are designed as ecosystems where multiple service providers and infrastructures can coexist. Governance frameworks such as those defined by the Data Space Governance Authority (DSGA) ensure that the rules of participation, technical standards, and trust mechanisms are collectively defined and transparent to all participants.

European data sovereignty also relies on collective governance mechanisms that enable participants to jointly define and evolve the rules of the ecosystem. Rather than relying on a central platform operator that unilaterally defines policies, European data spaces emphasise governance structures where stakeholders participate in decision-making regarding membership criteria, technical standards, semantic models, and operational policies. This approach ensures that the evolution of the data space reflects the interests of the participating community while maintaining interoperability with other data spaces and ecosystems.

Finally, European data spaces promote multi-anchor trust models and ex-ante compliance mechanisms. Trust frameworks allow multiple credential issuers and trust anchors to be recognised within a data space, preventing dependency on a single identity provider while maintaining interoperability. At the same time, European regulation increasingly emphasises ex-ante compliance, meaning that governance rules, technical safeguards, and policy enforcement mechanisms must be established before data sharing takes place. Data spaces operationalise these principles by providing governance-defined trust anchors, policy-enforceable usage control, and technical mechanisms that support compliance with regulatory requirements from the outset.

## 5. Interoperability in Data Spaces

Interoperability is a fundamental requirement for the successful operation and scaling of data spaces. In Europe, interoperability principles are strongly influenced by the European Interoperability Framework (EIF), which promotes alignment across legal, organisational, semantic, and technical layers. These principles are increasingly applied beyond the public sector and provide a useful reference for designing interoperable data sharing ecosystems. In the context of data spaces, interoperability ensures that organisations can exchange and use data across different technical systems, organisational contexts, and sectoral environments without requiring bespoke integrations.

The following documents published by IDSA address the relevant approaches to standardisation and semantic interoperability:

- IDSA Standardisation Landscape: [Data Spaces Standardization Landscape — Europe and International](https://internationaldataspaces.org/wp-content/uploads/dlm_uploads/IDSA-Position-Paper-Data-Spaces-Standardization-Landscape-Europe-and-international-2.pdf), covering key interoperability and standardisation work such as:
  - ISO/IEC 20151-1 Dataspaces — Part 1: Concepts and characteristics — at FDIS stage as of mid-2026, with publication expected late 2026 / early 2027; work on further parts (including Dataspace Trust Frameworks) has been registered
  - ISO/IEC TS 10866:2024 (organizational autonomy)
  - ISO/IEC 19941 (cloud interoperability and portability)
  - ISO/IEC JTC 1 SC 38 (Cloud Computing and Distributed Platforms), whose WG 6 hosts the dataspace work and processes the Eclipse PAS submissions
  - [Dataspace Protocol (Eclipse Dataspace Protocol 2025-1)](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/) — the 2025-1 release is the version submitted to ISO/IEC JTC 1 through the PAS process (as ISO/IEC 26450)
  - [Decentralized Claims Protocol (Eclipse Decentralized Claims Protocol v1.0)](https://eclipse-dataspace-dcp.github.io/decentralized-claims-protocol/) — submitted alongside DSP (as ISO/IEC 26451)
  - CEN/CENELEC JTC 25 (European Trusted Data Framework), whose deliverables include the Trusted Data Transactions series — EN 18235-1:2026 (Terminology, concepts and mechanisms) is published, with Parts 2 (Trustworthiness requirements) and 3 (Interoperability requirements) in development — and CEN/CLC/TS 18331:2026 (Maturity assessment of Common European Data Spaces)
- IDSA paper on semantic interoperability: [Semantic Interoperability in Data Spaces](https://internationaldataspaces.org/wp-content/uploads/dlm_uploads/IDSA-Position-Paper-Semantic-Interoperability-in-Data-Spaces-V1.1-1-5.pdf)

## 6. Trust, Privacy, and Security

Data sharing ecosystems are designed to ensure that participants can exchange data in a trusted environment where legal compliance, technical safeguards, and governance mechanisms work together. A key element of trust is the use of trust frameworks that enable participants to authenticate each other and validate credentials issued by recognised authorities. Instead of relying on a single identity provider, European data spaces typically support federated trust models where multiple credential issuers and trust anchors may be accepted according to governance rules defined by the data space. This approach promotes interoperability, reduces dependency on individual providers, and strengthens the resilience of the ecosystem.

Privacy protection is primarily shaped by the requirements of the General Data Protection Regulation (GDPR), which establishes strict rules for the lawful processing of personal data. Data spaces operating in Europe must therefore implement appropriate technical and organisational measures that support principles such as purpose limitation, data minimisation, accountability, and privacy by design. Where personal data is involved, participants must ensure that data sharing agreements, policy enforcement mechanisms, and governance processes support compliance with applicable data protection requirements.

Security requirements in European data spaces are increasingly influenced by regulatory frameworks such as the NIS2 Directive, which establishes cybersecurity obligations for essential and important entities. Data space implementations are therefore expected to incorporate strong authentication mechanisms, secure communication channels, and robust operational security practices. These technical measures must be complemented by governance processes that define responsibilities, incident management procedures, and auditing capabilities within the data space ecosystem.

## 7. Public-Private Collaboration

Public–private collaboration is a defining feature of the European data space ecosystem. European policy promotes the joint development of data spaces by industry, public authorities, research organisations, and standardisation bodies. This collaborative model helps ensure that governance frameworks, technical architectures, and sector-specific requirements are developed in alignment with both market needs and regulatory objectives.

Several sectoral initiatives illustrate this approach, where public institutions and industry partners jointly develop data spaces to support innovation and data-driven services. Examples include the Mobility Data Space, which enables data sharing across transportation stakeholders, as well as similar initiatives in energy, agriculture, and health.

Public funding programmes at both EU and national levels play an important role in accelerating the development and adoption of data spaces. Key European programmes include Horizon Europe, which supports research and pilot projects, and the Digital Europe Programme, which funds deployment of digital capacities and sectoral data space initiatives. Many EU Member States also support national data space projects and innovation hubs that contribute to the broader European data space ecosystem.

Through this combination of industry collaboration, public sector engagement, and targeted funding programmes, Europe aims to create interoperable data spaces that support innovation, competitiveness, and trusted data sharing across sectors and borders.

## 8. Cross-Border Data Flows

Cross-border data flows are a central objective of the European data space strategy. Within the European Union, data spaces are designed to enable seamless data sharing across EU Member States by relying on harmonised legal frameworks and interoperable technical standards. This approach supports the creation of a Single Market for Data, where organisations can exchange data across sectors and borders while complying with EU regulations. Data spaces facilitate this cross-border collaboration by providing trusted governance structures, interoperable protocols, and policy enforcement mechanisms that allow organisations in different jurisdictions to exchange data while maintaining control over its usage.

Beyond the EU, European data spaces also support collaboration with organisations in other European countries and global partners. Cross-border sharing of personal data with third countries must comply with the transfer mechanisms of GDPR Chapter V — adequacy decisions (in force for, among others, Japan, the United Kingdom, and the United States under the EU–US Data Privacy Framework for certified organisations), standard contractual clauses, or binding corporate rules. Non-personal data flows are shaped by the Free Flow of Non-Personal Data Regulation within the EU and by the Data Act's provisions on international access and transfer. In this context, data spaces can help organisations implement policy-controlled data sharing, provenance tracking, and auditability mechanisms that support compliance with international data transfer requirements.

Overall, the European approach seeks to enable open and interoperable data ecosystems while ensuring that cross-border data flows remain aligned with European standards for privacy, security, and data sovereignty. Data spaces provide the governance and technical mechanisms necessary to balance international data collaboration with regulatory compliance and trusted data sharing.

## 9. Open Questions for Future Research

Europe has established strong policy and governance foundations for data spaces, yet critical questions remain regarding large-scale adoption and long-term evolution. These questions are tracked as open issues in this repository; contributions are welcome. Some areas of future research are the following:

- **Regulatory–business–technical alignment:** How can the Data Act, AI Act, and sectoral regulations operationalise coherently within data space architectures? Emerging tensions, such as mandatory access rights versus usage control enforcement, or AI transparency requirements versus trade secret protection, require systematic resolution. Research must address sustainable business models that balance fair compensation for data providers with affordable access for SMEs and researchers.
- **Cross-data-space interoperability and federation:** As sectoral and regional data spaces proliferate, mechanisms for seamless interaction become critical. Can a healthcare data space federate with a research data space while maintaining distinct governance? How do trust anchors, certification schemes, and dispute resolution mechanisms scale across dozens of independent spaces without creating prohibitive complexity? Practical federation architectures require validation beyond theoretical frameworks.
- **Technology convergence and governance evolution:** Developments in areas such as artificial intelligence, digital twins, and cross-sector analytics introduce new requirements that challenge current data space designs. Simultaneously, governance models proven effective for hundreds of participants may not scale to ecosystems with tens of thousands. Research must identify governance innovations that maintain legitimacy and effectiveness at scale.