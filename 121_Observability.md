# Observability

This chapter aligns with the IDSA position paper *Observability in Data Spaces* and uses the terms *observability* and *observer* as the primary concepts for this functional area.

Many times it is necessary to make the data sharing process observable. This can be done for legal reasons to prove that data has been shared only with authorised entities, or for business reasons such as billing, dispute resolution, and compliance evidence.

To enable observability in practice, related business processes between participants (for example log exchange, evidence retention, dispute handling, and escalation paths) should be defined and, where required, included in the governance framework of the data space.

Depending on the architecture of the data space, multiple solutions are
possible. 
- Centralized or federated observer model, which has two main shortcomings when implementing large-scale data spaces: It presents an additional vulnerability that could affect the sharing of mission-critical data. Also, a central observer with information on all data sharing contracts represents potentially valuable knowledge about participants. This can be exploited for financial gain, making it a target for bad actors.

- Decentralized architecture can minimise the risks associated with a centralized or federated observer model.

In a decentralized observer architecture, every participant keeps the
information about the agreed contracts and their execution in their own
environment. Meaning that there are at least two copies of corresponding
logging information in the data space. The two copies can always be
identified through a correlation ID linking them. This log data can be shared with a participant that is providing the observer role. The observer then
matches the corresponding logging information and reports any irregularities to the parties participating in the sharing contract (or to the
respective regulator if required). The same mechanism can also be used for example for billing and notary functions.

The observer role may be assumed by the participants involved in a data sharing transaction or by third-party participants identifiable through specific credentials (for example an industry auditor rooted in a governmental trust anchor).

E.g.: If regulation requires an auditor to review data sharing information this information can be obtained through dataspace mechanisms. To audit the contracts of a participant, the auditor
requests the log data which is published as data contract
offer with an access policy restricting access to the auditor. To
verify the validity of those log entries, digital signing mechanism are used or the corresponding log data from other participants can be
requested to reconcile claims. This limits access to sensitive observation data to observers that are participants of the data space, have special credentials which qualify them as trusted auditors and are bound to the policies of those
contracts due to the contracts on the collected observability data. Observer
actions are automatically logged by the system and can be tracked and
monitored. This would enable a trust relationship in which auditors can
be audited by participants.

To simplify observability in a data space, the DSGA can mandate that
participants make their observability data available through data sharing contracts for ongoing event notifications or streams by default.

Following the same pattern, additional optional functional roles can be
implemented: invoicing, billing and  payment clearance services, notary services, regulator reporting, and the like.

Reference: [Observability in Data Spaces (IDSA Position Paper)](https://internationaldataspaces.org/download/51606/?tmstv=1773925364)

