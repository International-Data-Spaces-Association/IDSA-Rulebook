A data space needs defines policies that specify what attributes an
applicant must meet to become a trusted participant, often also referred to as a member. The data space governance authority ([DSGA](006_DSGA.md)) manages those policies, and it defines the business processes that might be necessary for this onboarding. As policies need to be clearly understandable and interpretable the DSGA also needs to provide a semantic model that details the defined policies so that applicants can correctly interpret the policies and provide proper claims about their attributes. The referenced semantic model describes the acceptable policies, their names, the potential value, and the format in which those values are accepted.


## Data space policies and rules

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

