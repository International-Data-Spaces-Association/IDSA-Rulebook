# AI and Dataspaces: Shaping the Future of Trusted, Decentralized Intelligence
## Introduction
The convergence of Artificial Intelligence (AI) and Dataspaces marks a pivotal moment in the evolution of data ecosystems that strongly benefits from recent developments in Trusted Data Sharing. As organizations seek to unlock the full potential of their data, the emergence of decentralized, context-rich data ecosystems—known as dataspaces—offers a new paradigm for secure, collaborative, and trusted data sharing and use. This paper explores the technological, business, and governance dimensions of AI in dataspaces, positioning them as the foundation for next-generation digital trust and innovation.

## The Evolution of AI: From Learning to Reasoning
AI has entered its third wave, with machine learning and generative models (such as LLMs) now mainstream. The focus is shifting from data-driven learning to advanced reasoning, where AI agents must operate on real-time, context-rich data. The bottleneck is no longer just access to data, but the ability to reason with it in dynamic environments. 
Retrieval Augmented Generation (RAG) architectures combine LLMs with additional data sources to enhance reasoning. They allow AI agents to operate across distributed data sources, leveraging external tools and resources for complex tasks.
Dataspaces provide both, access to data and the essential context, moving the field from “prompt engineering” to “context engineering”. The technologies are a great match for each other as both have two important technical attributes in common: decentralization and asynchronous operations that enable autonomy and agency!

## Dataspaces: The Architecture of Trust and Collaboration
Dataspaces are higher-order orchestration technologies that separate the data plane (data transfer) from business logic. They enable trusted, decentralized negotiation of access to data and APIs, supporting data sovereignty, interoperability, and reduction of business risk through attribute-based trust mechanisms. Participants—represented by software agents—negotiate sharing contracts, ensuring that data is shared with a set of agreed policies and permissions and rules guiding it’s use.
Key features include:
- **Trust Contexts:** Dataspaces create environments where data sharing is governed by robust contracts and policies, reducing business risk.
- **Decentralized Management:** No central data vault; participants retain autonomy and agency and can belong to multiple overlapping dataspaces.
- **Legal and Regulatory Alignment:** Compliance with frameworks like the EU Data Act is integral.

## AI Agents in Dataspaces
In general, there are two overarching scenarios of how AI Agents could leverage dataspace technologies. It’s kind of a bit like the chicken and egg problem: which one was first? Is it from the perspective of a dataspace that has AI Agents acting on behalf of participants or is it an AI Agent acting on behalf of an organization that needs to join a dataspace or use dataspace protocols and processes to access and use data?

### Dataspace First
AI agents operate within the boundaries of an existing dataspace and leverage pre-negotiated rights and contracts, streamlining data sharing and compliance. Participants in a dataspace have already agreed on data sharing contracts and AI Agents are being issued tokens to execute those contracts. One could distinguish between two patterns:
- Dataspace Data Planes are used to transfer data from one participant to the other. Once all the relevant data is collected in one organization its AI agents can act on the data locally, as long as it respects the usage policies associated with the data. This is probably the easiest to implement but comes with several disadvantages, e.g. the potential staleness of data.
- The use of MCP in Dataspace Data Planes. This would effectively wrap the access to data in a thin façade that enables the use of the MCP Protocol. The data provider would build a data plane that hosts a MCP Server and provides data access according to the data sharing contract. The data consumer would have an MCP client that is aware of data usage policies and guarantees that policies of the data sharing contract will be respected. This would allow more complex access scenarios than the first pattern.

### Agent First
Agents discover data offerings that other organizations are publishing through dataspaces but don’t yet have existing access. Depending on the rules of those dataspaces the Agents will need to first branch out into a human workflow to join the dataspace and negotiate the required data sharing contract. Alternatively, if the data provider supports direct negotiation the Agent can leverage dataspace protocols to automate the negotiation for data access without requiring its organization to manually join the dataspace. To negotiate access ad hoc, Agents can leverage dataspace protocols using decentralized claims and policy mapping for dynamic, cross-organizational attribute access control to be granted permission to shared data and to agree on data usage contracts.

## Protocols and Governance
AI agents are becoming critical actors within data ecosystems, requiring new protocols for secure, trusted communication. Emerging standards such as the Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocols are maturing, enabling agents to interact with databases, computational systems, and each other. Dataspaces bring a set of new protocols, Dataspace Protocol (DSP) and the Decentralized Claims Protocol (DCP) which enable a decentralized, attribute-based access control system for negotiation of data sharing contracts, governing access and usage permissions.
Although those protocols are being developed separately, they fit together perfectly, solving for different problems on the path to providing AI Agents with high value data in a controlled but highly automatable and scalable way.

- **MCP**: Standardizes interactions between AI Agents and data resources, managing permissions and access on a technical machine to machine level
- **A2A**: Facilitates agent-to-agent communication, supporting federated and collaborative AI scenarios.
- **DSP**: Standardizes interactions between organizations. It enables the negotiation of data access and usage policies, as well as a high level control of data sharing activities.
- **DCP**: Moving beyond traditional identity providers, agents can prove compliance via verifiable claims, streamlining access and trust.

While MCP focuses on a token-based access control to individual resources DSP and DSP focus on the higher level trust creation that ultimately leads to the issuance of a token for resource access.
When an AI Agent working on behalf of Organization A needs data from Organization B the two organizations can use Decentralized Identities (DIDs) and Verifiable Claims (VCs) to exchange information about each other that leads to trustworthiness (without the need to establish a common identity provider). Trust between two organizations can be established when one organization defines policies for trustworthiness and the other organization provides evidence—through verifiable claims—that these policies have been met. By verifying these claims, both organizations can build confidence in the relationship, ensuring that trust is not assumed but demonstrated and substantiated.
 
DSP is used to negotiate a data sharing contract that contains details about the nature of the data, the type of data technology used, semantic models, provisioning requirements for resources and also usage controls which Organization agrees to adhere to. Once such a contract is negotiated and approved it needs to be executed.
This is where MCP comes into play. Through DSP and DCP the AI Agent will be handed information on where to locate the MCP Server, which access token to use and what usage is permitted. It can then instantiate the MCP client, connect to the data or API to fulfill its task.
The resource protected through a decentralized attribute-based access control can be a data set, but also an API or even another AI Agent.
Same as the negotiation of data sharing contracts an AI Agent access contract could be negotiated. The data plane for that contract then would have to be an A2A protocol implementation.

## Semantic Interoperability and Compliance
As it will be impossible to create a globally standardized semantic model for data sharing contracts AI can help with the interpretation of different models and therefore aid in the fulfillment of the data sharing contract.
AI’s ability to map different semantic models reduces the need for manual standardization, enabling automatic policy negotiation and compliance verification. Dataspaces often leverage domain-specific knowledge graphs and ontologies, providing the context layer essential for meaningful AI integration.

## Strategic Recommendations
1.	**Invest in Protocol Standardization:** Support the development and adoption of MCP, A2A, DSP and DCP to enable secure, scalable AI integration.
2.	**Prioritize Governance and Trust:** Establish clear frameworks for identity claims, and compliance. Leveraging AI for automated policy evaluation.
3.	**Enable Semantic Mapping:** Use AI to bridge semantic gaps, facilitating interoperability across diverse data sources and domains.
4.	**Foster Consortia and Ad-Hoc Collaboration:** Design data offers and dataspace processes to support both structured and dynamic data sharing scenarios.

## Conclusion
AI and dataspaces are converging to create decentralized, trusted ecosystems for intelligent data sharing and reasoning. As AI agents become more autonomous, robust protocols, governance models, and semantic interoperability will be essential. Organizations that embrace these innovations will lead to digital trust, compliance, and business agility.

