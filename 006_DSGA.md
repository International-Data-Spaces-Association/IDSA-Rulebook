# Dataspace Governance Authority

## Definition

A Dataspace Governance Authority (DSGA) is a functional role. It is responsible for providing the basic governance framework, defining which [Dataspace Trust Frameworks (DTFs)](009_Dataspace_Trust_Frameworks.md) are being used for the data space, potentially defining an explicit DTF by defining business processes, policies and semantic models to be used by participants in the dataspace. 

The DSGA ensures interoperability through minimal shared semantics.

The DSGA is NOT the legal entity which provides runtime-enforcement. It is the collection of DTFs used within the dataspace and any additional provisions, definitions and processes specific to the individual data space.

While the DSGA is a logical role defining a governance model, this governance model needs to be enforced. There are multiple options how this can be achieved.

## Core Principle - Decentralization

A DSGA should not prescribe mandatory central services or federations without providing clear justification and documented mitigation measures. The DSGA applies to all participants and defers responsibility for implementing the governance model and its enforcement authority across participants, using consensus-based reconciliation to resolve conflicts.

**Important**: An Operator of a value-added data space service is NOT a DSGA. They can operate a service that supports the implementation of the governance model provided by the DSGA.

A DSGA is a formal specification of the governance model and rules of a data space; it describes policies, trust frameworks, and operational processes. While the DSGA itself is not a deployed runtime service, it must be instantiated (operationalized) through one or more implementation patterns — for example participant-enforced controls, service-provider implementations, or an operations company — and the chosen instantiation must be documented, transparent, and explain how enforcement is achieved.

## Implementation of the DSGA

- **By the Participants**: each participant has full knowledge of the DSGA and can enforce the rules of the DSGA in interactions with other participants. Value-Added Services or external Oracles might provide additional information needed to implement the governance model defined by the DSGA.

- **Service Providers**: multiple service providers operate value added data space services or external Oracles that enable the enforcment of the governance model provided by the DSGA. The participants of the data space are responsible to choose which services providers to use and are free to reject interactions with participants where a common set of accepted service providers cannot be identified. An example of such a service can be the issuance of a data space participant credential.

- **Operations Company**: in a very centralized designed data space the DSGA functions can be implemented by a single operations company which provides mandatory governance enforcement services. Note, that this is the least recommended design as it creates centralized control and single points of failure, thus impacting the autonomy and agency of participants.

## Additional considerations for DSGA design

- **Minimal Semantics**: Interoperability is achieved through shared core concepts (e.g., participant identity attributes, data space operations), not comprehensive ontologies (e.g. semantic models of the data being shared in the data space) to reduce complexity.

- **Socio-Technical Coupling**: Governance rules need to integrate technical feasibility with legal participant agreements. Ambiguities in policy interpretation are resolved through defined rules in the DSGA or its referenced DTFs. DSGA can provide prodcedures and escalation paths, assuming reasonable consensus thresholds to resolve conflicts in the data space.

