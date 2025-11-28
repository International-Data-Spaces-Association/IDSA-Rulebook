### Establishing trust

Establishing trust is fundamental to a data space. To create value from
data, it needs to interact with other data and then supports decision
making. The different entities must trust each other - without trust,
data will not be shared. Data spaces can create context-specific trust
where trust did not exist before or where it is difficult to establish
-- for example between competitors.

#### Attribute based trust

Establishing trust based on attributes is a control mechanism. A
participant's level of trust is determined by evaluating participant's
attributes, data contract, data asset, and environment attributes. This
evaluates the potential risk of sharing data with another participant.
This trust level is also based on the participant attributes, the
attributes of the data space and the attributes of the data shared in
the data space, as well as the applicable trust anchors and trust
frameworks. It can express complex rule sets that can evaluate many
attributes. There is no limit to the attributes that can be defined and
the expression of policy rules to evaluate those attributes.

Depending on the level of risk that can be tolerated for sharing an
asset, restrictions need to be put in place. The restrictions are
expressed through policies as described above. The proofs of adherence
to the policies and rules are expressed through the participant
self-description (PSD), as well as additional attributes that might be
provided by the participant outside the self-description (e.g., proof
that commercial contract for the data exists and that payment for the
data has been submitted).

Attributes can be atomic expressions (e.g., the other entity is a
participant of a specific industry association) or a set of multiple
atomic expressions (e.g., the other entity is under a specific
jurisdiction and the destination for the data transfer in a specific
country). Attributes can be compared to static values (e.g.,
jurisdiction = country) or to one another (e.g., both parties support
the same encryption algorithm).

Many situations will required attributes that are complex and might
require complex workflows that can include human intervention. It is not
possible to generally answer how to handle extended and complex
attributes. This is a question of the design of the data space and its
rules.

Attribute based trust provides a dynamic, context- and risk-aware trust
model, that enables precise control by including attributes from many
different information systems with customized rules. It allows
participants flexibility to build and use different implementations
based on their requirements.

#### Data space policies and rules

As introduced above, data spaces require membership policies (MP) as
first barrier to their data space. There must also be a trust basis to
prove compliance with the policy, and an appropriate mechanism to allow
each participant to verify that their counterpart is adhering to it.
Every data space must define what level of trust is the minimum for
members. Each participant can verify other participants membership
through a digital signature mechanism provided by the data space or
separately verify compliance with data space policies and rules as
needed (e.g., if especially sensitive data is shared, all relevant
policies and self-descriptions can be evaluated ad hoc to ensure the
necessary trust level). Additional trust frameworks (e.g., the Gaia-X
trust framework) can be used to provide additional compliance
mechanisms. The data space could even be its own trust anchor. The
participants decide whether to trust the DSGA and its trust anchors.

The first level at which policies take effect in a data space is the
membership level. The next level is the catalog: Every participant
should only see items in the catalog that match the permission resulting
from matching the participant's attributes to the access policies of the
catalog. A contract offer should only be visible to those participants
who have the right to access it, to minimize unintentional sharing of
information. During the negotiation process for a data contract, the
detailed policies of that contract will be applied. Some of those
policies may be fully evaluated at that time while others may not be
evaluated until later when the data transfer is made or after the data
has been received. We refer to these policies as contract policies (CP)
and highlight the sub-group of usage policies (UP) because of their
importance in data sharing.

It will be impractical for many data spaces to act as the root of trust
as they would need to provide the necessary service functions. (e.g.,
compliance service to verify external attributes). Also, many data
spaces will require multiple external roots of trust, whether for
regulatory purposes, legal requirements, or simply because of existing
trust in established organizations.

A key question of a data space is therefore which roots of trust are
considered acceptable and whether any should be rejected. Since this is
an attribute of the data space it can be expressed through the data
space self-description (DSSD) and its acceptance mandated by the
membership policies encoded in the DSSD.

Another element needs to be part of the DSSD - the mandatory policy
information model for the data space. Every data space needs to define
the vocabulary to ensure a common understanding of the meaning of the
policies. There might be different meanings to the same policy
expressions in different data spaces. Therefore, is has to be done
individually.

This shows how important the DSSD is for the interaction with the data
space functions and to clearly understand the context and risk factors
of the data space. A data space needs to have an identity -- not just to
be clearly identifiable for the participants and potential members, but
also because the identity is the root element to which the DSSD is tied.
As mentioned above, the decision on how the functional elements are
implemented and expressed through the functional role of the data space
governance authority is highly dependent on the needs of the data space and is the
most important decision to be made when designing a data space.

<!-- more details on how trust is established in an attribute based system>