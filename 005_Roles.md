# Roles

## Technical Role - Participant
As established in the chapter on [Layers](004_Layers.md) the only technical role is the **Participant**. However, there are many different roles possible in the economic and legislative layers of a data space. This chapter explains the most important ones.

## Data Space Governance Authority

The Data Space Governance Authority (DSGA) is a special, functional role within a data space. It can be understood as the "legislative" of the data space by having the functional responsibility to define the rules and processes of the data space. 

It serves a logical purpose within the Data Space Governance Framework but has no single definition of how it is implemented. To fully explain the role of the DSGA and not to distract from the Participant roles it is described in detail in its own chapter: [Data Space Governance Authority(DSG)](http://link-to-dsga-chapter.md)

## Common Business Roles

Business roles in this Rulebook describe functions, and no status. The model
definition of roles should provide clarity about tasks and capabilities
and support the understanding of architectures and processes. Roles may
not always exist in their pure form - mixed forms are often experienced
by participants in data spaces - and new or more specific roles will
emerge over time. In this section we define the most important and
common roles without claiming to be exhaustive. In practice, it has
proven useful to first implement the essential roles that are necessary
for the data space to function. Three roles should be established first:
provider, consumer, and intermediary services.

### Data consumer

Data consumers are the recepients of a data sharing activity. In the IDSA Rulebook the data consumer is the party acting as the consumer of a data sharing contract. 

The closely realted term "data user" describes a natural or legal person who has lawful access to certain personal or non-personal data and has the right,  to use that data for commercial or non-commercial purposes.

The data user and data consumer can be separate organizations but often will be two perspectives on the roles of the same participant, depending on the context.

### Data provider

Data providers are the organizations that make data technically available for a data sharing activity. In the IDSA Rulebook the data provider is the party acting as the provider of a data sharing contract.

The closely related term "data holder" describes a natural or legal person, who is not a data subject with respect to the specific data in question, who has the
right to grant access to or to share certain data in accordance with applicable law.

The data holder and data provider can be separate organizations (e.g. in cases where intermediares are being introduced) but often will be two perspectives on the roles of the same participant, depending on context.

**Role mapping guidance:**
- **Data Holder:** the legal owner or rights holder of the data (responsible for legal compliance and consent decisions).
- **Data Provider:** the entity that makes the data technically available (responsible for data access, availability, and technical controls).
- **When roles differ:** Contracts must explicitly allocate responsibilities (consent, liability, enforcement, and notification) and the DSGA may require that member self-descriptions include role assignments to make responsibilities discoverable.

### Service Provider (intermediary, value-adding services)

In a data space optional service providers can offer [optional capabilities](http://link_to__value_added_services_chapter) to enable data sharing or to provide business services. Fundamentally, all such service providers are considered to be a participant in a data space and therefore bound to the agreed policies and rules of a given data space. Their implementation must be representable as a participant at the technical level.

**Intermediaries** are services that are acting on behalf of participants in the data space. This can be a range of activities within the data space: negotiating a data sharing contract on behalf of a participant, implementing technical infrastructure on behalf of the participant and making decisions on behalf of a participant, thus impacting their digital sovereingnty.

Such intermediaries may be regulated by local governments like the EU Data Governance Act in the European Union, which defines a specific "Data Intermediary" role. A detailed analysis can be found in the paper [Reflections on the DGA and Data Intermediaries](https://internationaldataspaces.org/download/42325/?tmstv=1708096468).

**Intermediary usage guidance:**
- **Optional:** Intermediaries may be used voluntarily by participants to simplify operations or reduce cost. When optional, their use is a matter of participant choice and does not reduce the baseline autonomy provided by the data space.
- **Mandatory (Regulatory):** If law or regulation requires an intermediary role, the DSGA must explicitly document this requirement and provide safeguards (e.g., audit rights, transparent processes, alternative providers where feasible) to limit negative impacts on participant autonomy.
- **Impact mitigation:** Where intermediaries are required or offer substantial control over interactions, the DSGA should require explicit documentation of the scope of delegated authority, revocation mechanisms, and participant redress processes.

**Value-added service providers** act as a participant in the data space and
do therefore conform to the data space governance framework. Such services aim to
support the value-creation process with a broad set of basic or advanced data
processing services. Common examples are:

- Data Discovery Services (Catalogs, Search Engines, Registries)
- Lookup Services (Vocabularies, shared information)
- Observability Services (Auditor, Notary)
- Commercial Services (Marketplace, Auctions, Match Making)

Such optional functionalities are described in the section on [value-added services](http://link-to-value-added-services).

#### Potential roles from legal defintions

Roles might also be described by legal regulation. An example of such regulation that defines roles in data sharing are the European Union regulations, like GDPR or DGA:
* Data Rights Holders are natural or legal persons, holding rights on the data.
* Data Recipients are legal or natural persons that act as data consumers and data users. 
* Data Users are natural or legal persons, which use the data under the given policies and regulations. 
* Data Subjects are defined in GDPR.
* Data Intermediation services or Data Intermediaries are subject of the Data Governance Act. (see [Reflections on the DGA and Data Intermediaries](https://internationaldataspaces.org/download/42325/?tmstv=1708096468))



## Summary

In line with the description of the [role models](005_Roles.md) and the [layered approach](#layers-of-a-data-space), the diagram below presents an overview on roles in data spaces and their affilation to the layers.

![Overview on roles and their affiliation to layers in data spaces](./media/Role%20Overview%20Rulebook.jpg)

This diagram is a foundation to depict the typical use cases of the roles in relation to data spaces. 
