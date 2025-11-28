#### Policies

Policies ensure a trusted data ecosystem within a data space. They are
used at multiple levels and at almost any interaction point. The two
main policy groups that are central to the functionality of a data space
are access policies (which control access to contracts) and contract
policies (which control the contract terms and the usage of data). While
the use of policies can be expanded by custom design within a data space
there are several fundamental policy points that enable the operation
and are therefore essential to understand.

It is essential to use policies for attribute-based trust in a data
space. Which policies need to be mandatory depends on the design and its
requirements. One data space might require policies that reflect the
sensitivity of health data in an international setting, while another
data space will need to enforce policies for national energy regulation.
Therefore, data spaces must define their own policies and communicate
them clearly. Participants may always choose additional policies in
their data contracts to further restrict access and use.

In a centrally managed data space, the DSGA might simply define the
ontology of policies. In a decentralized data space, there might be an
additional negotiation protocol that enables participants to agree on
the policy for their interaction.

Policies generally express three possible restrictions: prohibitions,
obligations, and permissions. Constraints expressing a rule can be
combined into more complex rules, which then form the applicable policy.
For example, a group of data space participants may only allow access to
their data for participants who belong to the same industry association,
allow to process data under the condition only anonymized results are
produced, and then permits to share the results with a third party for
processing if they meet a set of ISO
standards.

![Different policies  in data spaces](../media/Different_policies_in_data_spaces.jpg)

As discussed above, the first line of policy defense is the membership
policies (MP) and rules required to join a data space. These policies
ensure that only companies with certain attributes they can verifiably
prove, can join. These could be policies that verify the applicant's
nationality, industry certification, membership in industry
associations, but also policies that would require human interactions
and complex workflows, such as a valid contract with the DSGA that must
be negotiated before an applicant can become a participant.

Once an applicant becomes a participant, the next set of policies
becomes relevant: access policies (AP). An AP defines which attributes
must be available to access data contracts. A participant that does not
have access to a specific data contract should also not be able to see
the contract offer in the catalog. Optional services, like a
marketplace, should adhere to this principle as well and only show items
based on matching access policies and participant attributes. In a
scenario where contract offers should be made visible to everyone, the
access policy can also be expressed as an empty policy, not triggering
any restrictions. From a functional perspective, an access policy always
needs to be present, even if it grants access to everyone. A common
scenario is policies that grant access to anyone within the data space
but hide the associated item from queries by non-members (in case the
catalog endpoint is publicly accessible).

Each participant can define such policies, whether providing or
consuming data. For example, a participant interested in data could
define a policy to see only data with a distinct proof of origin, and
participants offering data could restrict access to their data to
members of a certain jurisdiction. This is often referred to as provider
policy and consumer policy.

When a participant has access to a data contract offer (DCO) the next
set of policies comes into play. A DCO can have contract policies (CP)
that define what attributes are needed for a data contract agreement
(DCA). CPs review attributes that must be provided at the contract
negotiation. This could be as simple as ensuring that the participant
uses a specific encryption algorithm or software package -- both of
which could be verified with a technical handshake procedure (e.g.,
sending a piece of information and requesting the properly encrypted
version). A more complex attribute example involving human interaction
is the association of the data contract with a legal contract between
the two parties that typically occurs outside of the data space
processes. The negotiation of policies can be on the spectrum of 100%
machine-processable and immediate to a human workflow potentially taking
a long time.

A contract may also specify policies for the transport mechanism for the
data asset transmission: like requiring a protocol, specifying pull or
push of data, mandating a data sink in a specific geographic area and
other details.

CPs may also include usage policies (UP) that take effect after the data
is transmitted and control how the data can be used by the receiving
party. Depending on the value of the data, use cases, trust levels,
contracts in place and many more attributes, there are different
possibilities to enforce UPs which come at varying costs.

For data with low importance or data not under a specific legal
protection, it might be too expensive to build a system that guarantees
control - it may be sufficient to simply monitor data use and fall back
to a legal contract should misuse of the data be detected. Other data
might be very sensitive, legally regulated, or costly and require
stronger protection and higher technical costs.

When designing a data space and deciding which data to share, it is
important to understand the data's classification, and regulatory
controls to design not just the right policies but also to mandate the
appropriate level of technical components that ensure proper handling of
the data.
  
| **Example**  |    **ProtectionNeed** | **Explanation** |
| :------------| :--------------------: | :---------------|
| Public weather data | low | Some data sets are already publicly available and can be shared without enabling others to derive sensitive data about persons or business secrets. |
|  Shipping information | medium  | Some data are valuable and at large scale likely to be highly protection worthy as they can give insights into business relations and transactions. |
|  Personal health data |  high | Personal health data are highly protection worthy due to strong laws and potential danger to the individual in case of data misuse. |
| Machine operations data | high | Industrial data is also usually of high value due to the sensitive business information it represents.|

The atomic expressions of policies can be further broken down into a set
of restrictions against which machine-readable attributes can be
compared.