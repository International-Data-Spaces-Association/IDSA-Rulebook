# Understanding the planes of a data sharing solution

A data sharing solution can be described as a set of interacting planes with distinct responsibilities: the **Control Plane** for discovery and contract negotiation, the **Data Plane** for data transfer/access execution, the **Data Management Plane** for lifecycle and governance within organisations, and the **Application Plane** for user-facing value creation. The separation clarifies responsibilities and reduces architectural coupling.

## Control Plane

The control plane in a data space is the layer responsible for managing the discovery of available assets and the negotiation and orchestration data sharing interactions contracts. 

It operates independently of the actual data access, focusing on establishing and maintaining the data sharing contracts that provide the requirements for the data sharing execution. The core capability of data spaces, the dynamic trust negotiation through policy reconciliation are executed in the control plane. 

The control plane influences (orchestrates) but does not directly handle data flows (data plane), data lifecycle management (data management plane), or application logic (application plane). 

## Data Plane
The Data Plane is the actual technical data access technology. Its role is to provide access to or transmit data according to the policies agreed upon in the data sharing contract.

### Examples of Data Planes

- **RESTful APIs**: A common data plane implementation using HTTP-based protocols for synchronous data retrieval. 

- **Message Queues (e.g., AMQP or MQTT)**: Asynchronous data transmission via publish-subscribe models. 

- **Peer-to-Peer Protocols (e.g., IPFS or BitTorrent-like systems)**: Decentralized file sharing without central servers.

- **Streaming Protocols (e.g., Kafka or WebSockets)**: Continuous data streams with subscriptions. It handles high-volume, low-latency flows while maintaining separation from control plane governance.

These examples assume minimal shared semantics for interoperability. Implementations must account for failure modes, such as network failures or policy violations.

Sovereign capabilities depend on the specific implementation of a data plane and the underlying data transfer technology.

## Data Management Plane

Once data has been shared it usually needs to be managed to enforce governance models and ensure the adherance to policies negotiated in the control plane.

The Data Management Plane encompasses the organisational functions responsible for managing the lifecycle, quality, and governance of data within a data sharing solution. This includes ensuring data integrity, compliance with contractual obligations, and usability across internal systems.

The Data Management Plane encompasses the functions responsible for the lifecycle, quality, and governance of data within a data sharing solution.

While it operates separately from data transmission (data plane) and orchestration (control plane), the Data Management Plane supports participation in the data space by integrating governance requirements into the organisation’s internal processes and systems.

### Typical Functions of Data Management

- **Data Ingestion and Storage**: Collecting, validating, and storing data from various sources, ensuring format consistency and metadata attachment. It enforces invariants like data provenance and traceability to support sovereignty.

- **Data Processing and Transformation**: Applying algorithms for cleansing, aggregation, or anonymization, while adhering to policies reconciled in the control plane. 

- **Data Cataloging and Discovery**: Maintaining metadata registries for asset discovery, ensuring that policies from data sharing contracts are being enforced. 

### Typical Functions of Data Governance

- **Policy Enforcement and Compliance**: Monitoring adherence to governance rules, such as retention policies or usage constraints, through runtime checks. 

- **Quality Assurance and Auditing**: Assessing data accuracy, completeness, and lineage, with audit trails for trust verification. 

- **Risk Management and Data Sovereignty Protection**: Identifying and mitigating risks, including sovereignty violations, by enforcing participant controls. It prioritises conservative approaches, such as deny-by-default for sensitive data.

These functions are clearly separated from other planes. However, interaction and integration with other planes is necessary for building full governance and management capabilities.

## Application Plane

The Application Plane is the user-facing layer that consumes and processes data from the Data Management Plane to deliver value to the user. It operates independently of data transmission (data plane), orchestration (control plane), and lifecycle management (data management plane), focusing on application logic and user interactions. It integrates with organisational governance mechanisms to ensure compliant use of data.

### Key Characteristics

- **Data Consumption**: Retrieves processed data from the Data Management Plane, applying policies for access and usage in coordination with the data management plane based on the permissions and access controls associated with the identified user. 

- **Service Provision**: Provides services such as analytics, visualization, and reporting to end-users, enabling decision-making and insights. These services are built on top of managed data, prioritising usability and performance while adhering to governance rules managed by the data management plane.

- **User Interaction**: Supports interfaces for human or machine users (agents), including dashboards, APIs, or automated workflows. 

### Examplary Functions

- **Analytics**: Performs computational analysis on data from the Data Management Plane, such as statistical modelling or machine learning, to generate insights. 

- **Visualization**: Renders data into graphical representations (e.g., charts, maps) for user consumption.

- **Reporting**: Generates structured reports or alerts based on processed data, integrating audit trails for traceability. 

The Application Plane must maintain clear boundaries with other planes, interacting via standardised interfaces. It can support dynamic trust by propagating policy constraints, mitigating risks such as sovereignty breaches and manage user consent mechanisms. 