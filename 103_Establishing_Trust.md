# Establishing trust

Humans build trust with each other by evaluating attributes of the other person: attributes that are immediately verifiable (e.g., a language spoken) or attributes that require an external authority to verify them (e.g., a passport). To build trust, these attributes are matched against rules (personal, internal, implicit and/or explicit). If a sufficient number of policies are met, trust is established. Based on the attributes that have been evaluated, different levels of trust can be negotiated.

**Establishing trust is the fundamental reason for data spaces to exist!**

To create value, data needs to interact with other data and then support decision
making to enable actions that will create value. The potential to create value increases if data is more diverse, which often requires that multiple actors need to come together and share their data with each other. However, like in any human relationship: Before sharing comes trust. Without trust, the risk of something going wrong seems too high and unmanageable. Creating trust reduces risk. Reduced risk lowers the barrier for sharing data.

**Increaseing Trust lowers Risk**

Data spaces can create context-specific trust where trust did not exist before or where it is difficult to establish -- for example between competitors. Therefore data spaces reduce the risk of sharing data and through that enable the creation of value.

## Attribute-based trust

Attribute-based trust is a way to establish trustworthiness between two parties based on specific attributes rather than a fixed identity. It functions as a control mechanism with minimal disclosure -  proving that certain conditions are met without revealing full details on every interaction. 

It's mechanism can be summarised in a couple of simple statements:

- A Participant holds a collection of attributes
- A data sharing contract is a collection of policies
- When negotiating a data sharing contract attributes are matched to policies

A participant's trustworthiness is determined by evaluating their participant
attributes. This evaluates the potential risk of sharing data with another participant. Lower risk means higher trust.

In addition to the attributes of the participant the trust level is also based on additional context: the attributes of the data space and the attributes of the data shared in the data space, the applicable trust anchors and trust
frameworks, and potentially others. 

It can be expressed by complex rule sets that can evaluate many attributes and understand their provenance and who is providing guarantees about them. There is no limit to the attributes that can be defined and the expression of policy rules to evaluate those attributes. It is also possible to define policies that branch into additional workflows, e.g. human approvals, for evaluating claims about the participant attributes.

Depending on the level of tolerable risk (and thus required trustworthiness) for sharing an asset, restrictions need to be put in place. The restrictions are expressed through policies as described above. The proofs of adherence
to the policies and rules are expressed through cryptographically signed claims, as well as additional attributes that might be provided by the participant directly or indirectly represented through the claims presentation process during the trust negotiation (e.g., proof that commercial contract for the data exists and that payment for the data has been submitted; proof of technical capabilities (e.g. encryption at rest, secure communication channels, etc...)).

Attributes can be expressions representing a single claim (e.g., membership credentials of an association) or a set of multiple claims (e.g., the other entity is under a specific jurisdiction and the destination for the data transfer in a specific country). Claims can represent static values (e.g.,
jurisdiction = country) or contain statements about proofs of technical capabilities (e.g., support a specific encryption algorithm).

Many situations will required attributes that are rather complex and might
require additional workflows that can include human intervention. It is not
possible to generally prescribe in the IDSA Rulebook how to handle extended, composite and complex attributes. This is a question of the design of the data space and its rules. Further guidance can be found in the [IDS RAM](https://link2RAM).

>Attribute-based trust provides a dynamic, context- and risk-aware trust
>model, that enables precise control by including attributes from many
>different information systems with customised rules. It allows
>participants flexibility to build and use different implementations
>based on their requirements.
>
>It eliminates the need for an identity provider that >controls absolute decisions and thus removes a single point of control and >potential failure. It enables autonomy, agency and thus digital sovereignty of >the individual participant.

