#  WORK IN PROGRESS!!!


- benefits of decentralization
- onboarding
- participant registry (none)

#### Decentralized data space governance authority

Using a decentralized design enables the highest level of autonomy and
sovereignty. The core element enabling a participant to act autonomously
is the identity system. By using a decentralized identity system each
participant is responsible to maintain identity information that can be
verified by other participants or the DSGA, rather than relying on a
centralized identity provider.

Once decentralized identities are established, all other functional
services can also to be decentralized, minimizing or even eliminating
barriers to participant sovereignty.

It should be noted that in a decentralized data space a lot of the
responsibility for operating essential functional roles shifts from the
DSGA to the participants. For example, in a centralized model, the DSGA is
expected to operate the catalog of available data assets, while in a
decentralized model, each participant is responsible for publishing its
available data directly and in turn, each participant needs to ask all
other participants about their available assets.

Another advantage of a decentralized system is that it is usually more
resilient to errors or bad actors, since problems in individual nodes do
not automatically affect all participants of the data space. Finally, a
decentralized system does not require an ever-increasing number of
centralized services. Each node is self-contained and provides all the
endpoints necessary to interact with it. A data space can grow and scale
much more efficiently than a centralized design, where the resources to
provide central services must grow exponentially.

### Decision areas

#### Sovereignty

The goal of digital sovereignty is autonomy, which is different from
independence -- it means acting with choice. It includes control over
when and where data is stored and how it can be accessed. Sovereignty
and autonomy are not binary concepts but move along a spectrum. The goal
is to increase sovereignty and autonomy until a desired threshold is
reached. In that sense, the concept is similar to that of privacy.

#### Resilience

Resilience in a data space is about the ability of the ecosystem and
individual actors to continue functioning in the event of unforeseen
problems.

#### Scalability

Scalability of a data space is not about the volume of data but about
the number of participants, the amount of the data assets shared, and
the number of negotiated contracts.

#### Control

In this context, a high level of control means that the entity operating
the DSGA can control access to the services as well as the content they
provide. This is in direct contrast to sovereignty, where the control
lies with the individual participant.

#### Simplicity

Well-established technologies and architecture models are easier to
deploy because implementing teams have experience with them. The
interaction model between participants as well as the business model of
the data space are included in this category.

#### Discoverability

Discoverability is the measure of how many steps are necessary to find
the data offered in the data space. Since data asset information can
always be exchanged directly between participants, this measure only
considers how complex a query would be to find all data assets currently
offered in the data space.

### Decision support

As all decision areas are connected and partially work against each
other, it is necessary to look at them holistically and not focus on one
area. Make sure you weigh the importance of these decisions according to
your business and technical needs. The technical maturity of the planned
participants is an important factor. Many organizations are willing to
compromise on their digital sovereignty in exchange for convenience and
business value.

Many models exist in between the main three implementation designs. The
following charts highlight some of the interdependencies between the
decision areas for planning, implementing and operating a data space:

With a centralized design the entity operating identity and catalog
services has a lot of control. It is easy to setup, only one entity
needs to deal with the DSGA services, and participants can simply query
one catalog and rely on the DSGA as a trust anchor to issue a participant
ID. But this design impairs participant sovereignty, is less resilient
and difficult to scale as the central services will grow exponentially
in their resource requirements as more participants join.

The distributed design sits in the middle of the spectrum. Control is
not exercised by a single entity but by multiple federators and thus not
a single entity can make arbitrary decisions. However, participants
still do not have full control over their actions, so sovereignty is
still impaired. Resilience and scalability are improved by having
multiple nodes of the data space services that can either be setup as
partitions or as replicas. Discoverability must take into account the
partitioning of the catalog and might become more complex.

The aim of the decentralized design is to maximize the sovereignty of
individual participants and grant them as much autonomy as possible.
This reduction in dependency on central services automatically leads to
higher resilience and better scalability. However, it adds complexity
for the individual participant, as all participants now need to operate
service nodes that participate in the discovery process of available
data. Some data spaces might require additional control over
participants and their actions, which is harder to achieve in a
decentralized implementation.

The figure below gives a comprehensive overview of the values within the
decision areas when implementing a centralized, federated/distributed,
or decentralized approach.

![Comparison of models for decision support](../media/media/image16.png)

Another way to compare the features and
capabilities of the different designs is to separate the decision areas
into a business and a technical perspective. Which design benefits the
business value of the data space vs. which design aspects are a
technical necessity? A careful compromise design-decision can be voted
on by the founding parties of the data space to reach the optimal
implementation.

These three models are just examples of possible implementation designs.
Every data space should be tailored to the needs of its participants.
Any entity that wishes to participate in a data space should investigate
the implementation design in detail to ensure the design grants them the
aspired level of sovereignty and supports its business goals.
