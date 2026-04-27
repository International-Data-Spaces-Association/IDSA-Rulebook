# Identity

The design of the identity provider is the first decision for the design
of the data space. If a central identity provider is chosen to manage
the identities for all participants, every other service depends on this
central verification, and decentralized designs are no longer fully
feasible.

Which mechanism to use to identify participants is the most fundamental
design decision. It impacts policies on autonomy and sovereignty as well
as technical solution architectures for other components of a data
space.

| **Identity System** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| **Centralized identity** | Simple management for DSGA | Low autonomy and sovereignty of participants |
| | High degree of control for DSGA | Single point of failure |
| | Traditional, well-known technology stack | Single point of attack |
| | | Harder to manage for participants |
| **Decentralized  identities** | Full autonomy and overeignty for participants | Complexity: DSGA management requires decentralized protocols |
| | Low resourcing need for DSGA | Lower degree of control for DSGA |
| | Easy to manage for participants | New and partially unfamiliar technology stack |
| | Harder to attack | |

## Attributes & self-description

Attributes and self-description should always be available as verified
presentations. The exact serialization format and service endpoints
depend on the implementation of the data space and the trust anchors in
use.

Note: The disadvantages listed for decentralized identities describe governance and operational trade-offs, not a loss of participant agency. DSGAs may define accepted trust anchors and onboarding processes; participants remain free to accept or decline those trust anchors and thereby preserve agency in their decision to join or interact.
