---
title: "CommBank's AI boyfriend"
date: 2025-08-12
cover:
  image: "cover.png"
  alt: "CommBank's AI boyfriend"
  relative: true
ShowToc: false
params:
  description: CommBank's AI boyfriend 
  images:
  - cover.png
  title: "CommBank's AI boyfriend"
tags: ["business", "secret lab", "yarn spinner", "money", "banks", "shit companies", "crooks", "commbank", "angry", "rant", "liars"]
---

[CBA](https://commbank.com.au) has been naughty, and too reliant on their [AI boyfriend](https://www.abc.net.au/news/2025-07-29/commonwealth-bank-says-ai-behind-dozens-of-job-cuts/105586312). Here's what happened:

- A CBA customer contacted bank requesting contact details for [Secretlab](https://secretlab.sg) (a company that _is not_ us, and makes chairs)
- CBA staff member queried ChatGPT (possibly via their own personal, unauthenticated access to ChatGPT) to obtain phone number for Secretlab
- CBA staff disclosed the retrieved phone number to the requesting customer
- The retrieved phone number is a number belonging to one of the directors of [Secret Lab](https://secretlab.games) (a company that does not make chairs, and _is_ us), a customer of CBA, and is used for our CBA account and our Director's CBA account
- Therefore, CBA disclosed customer personal information to another, unrelated customer, and trusted a third-party LLM (ChatGPT), accessed seemingly unauthenticated on the consumer ChatGPT platform, as a source for data to provide to another customer
- During investigation, CBA staff replicated the same ChatGPT query process, seemingly on a personal phone, again unauthenticated, and on the consumer ChatGPT platform
- Signs indicate this might be routine practice amongst CBA staff

Oh, and they gave out the phone number for us, Secret Lab (not chairs), to someone looking for Secretlab's (chairs) phone number. So, in the end of all this, they weren't even helpful. LLMs in a nutshell, really.

It certainly feels like CBA has violated, or come pretty close to violating, a lot of things, and this doesn't _feel good_...

### For example, the [_Privacy Act 1988_ (Cth)](https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act), and the [Australian Privacy Principles](https://www.oaic.gov.au/privacy/australian-privacy-principles):

**APP 6 Use or Disclosure of Personal Information:**
Personal information may only be used or disclosed for certain, good, reasons.

Disclosure of customer contact information to another customer falls outside permitted purposes.

**APP 8 Cross-border Disclosure:**
> "Before an APP entity discloses personal information about an individual to a person (the overseas recipient) who is not in Australia or an external Territory, the APP entity must take such steps as are reasonable in the circumstances to ensure that the overseas recipient does not breach the Australian Privacy Principles."

Querying ChatGPT involves transmitting the customer's business name to OpenAI's international servers, and relying on information sourced from those servers, without adequate safeguards for data handling. 

OK, _admittedly__, our business name isn't really personal information (our phone number is), but they still transacted with a cross-border entity for the information about us they then gave the other customer. 

Given we're CBA customers, this becomes pretty horrific.

**APP 11 Security of Personal Information:**
> "An APP entity must take such steps as are reasonable in the circumstances to protect the personal information that it holds from misuse, interference and loss and from unauthorised access, modification or disclosure."

Staff relying on unverified external AI sources for customer information retrieval and subsequent disclosure fails to meet reasonable security standards for protecting customer information.

### And the [_Banking Code of Practice_](https://www.commbank.com.au/about-us/opportunity-initiatives/policies-and-practices/banking-code-of-practice.html):

**Privacy:**
The Banking Code requires banks protect customer privacy.

Disclosure of customer information to another customer without consent or legal authority breaches fundamental confidentiality obligations.

**Customer Information Protection:**
A bank shall take reasonable steps to protect personal information held by it relating to a customer against loss and against access, use, modification or disclosure that is unauthorised.

The disclosure was unauthorised and failed to implement reasonable protective steps.

**Professional Standards:**
The Banking Code requires banks to maintain professional standards in customer service and information handling.

Using unverified external AI sources clearly fails to meet professional banking standards.

### And [AUSTRAC](https://www.austrac.gov.au/business/legislation/amlctf-act):

**Customer Due Diligence Requirements:**
AUSTRAC mandates banks maintain robust "Know Your Customer" (KYC) procedures and ongoing customer due diligence. Banks must verify customer identity using "reliable and independent documents or electronic data" from "at least two separate data sources."

Using ChatGPT as a source for customer information violates AML/CTF requirements for reliable, verified information sources and proper customer due diligence procedures. 

This _wasn't really_ part of a due diligence/KYC process, but they used it as a source of information, when it's not reliable or accurate. Very strange indeed.

### And then there's the [Australian Consumer Law](https://consumer.gov.au), specifically Misleading or Deceptive Conduct:

**Section 18 Competition and Consumer Act 2010:**
> "A person must not, in trade or commerce, engage in conduct that is misleading or deceptive or is likely to mislead or deceive."

CBA's disclosure of unverified information sourced from ChatGPT _could_ constitute misleading conduct by presenting potentially inaccurate information as reliable to customers.

### And, of course, [ASIC](https://www.legislation.gov.au/C2004A00819/latest/text): 

**Section 12D Misleading or Deceptive Conduct in Financial Services:**
> "A person must not, in trade or commerce, in relation to financial services engage in conduct that is misleading or deceptive or is likely to mislead or deceive."

Providing unverified customer information in a financial services context constitutes misleading conduct under financial services-specific legislation.

### For even more fun, we can look at the [CBA Privacy Statement](https://www.commbank.com.au/support/privacy.html) and the [CBA Information Security Policy Framework](https://www.commbank.com.au/content/dam/commbank-assets/about-us/2024-07/information-security-statement-july-2024.pdf):

**From CBA's Group Privacy Statement:**
> "We take our responsibility to protect your privacy very seriously. We apply strict security and privacy controls to the way we handle your personal information."

Staff querying external AI systems for customer information and disclosing retrieved results contradicts CBA's stated commitment to strict privacy controls.

**Permitted Sharing Categories:**
CBA's privacy policy lists specific circumstances for information sharing, including:
- Other CommBank Group companies
- Authorised third parties (with consent)
- Strategic business partners
- Regulatory/law enforcement bodies
- Service providers for transaction processing

Sharing customer information with another unrelated customer is not included in any permitted category.

**From CBA's published policies:**
> "We use a range of physical, electronic and other security measures to protect the security, confidentiality and integrity of the personal information we hold about you."

Staff relying on unverified external AI systems for customer information contradicts CBA's commitment to protecting information security and integrity.

### And their [Code of Conduct](https://www.commbank.com.au/content/dam/commbank-assets/about-us/docs/cba-code-of-conduct.pdf):

**Internal Policy Framework:**
CBA's Code of Conduct requires staff to act with integrity and follow proper procedures when handling customer information.

Using external AI tools without proper authorisation or verification procedures breaches internal conduct standards.

### For even more _fun_, we can think about Unconscionable Conduct:

**ASIC Act and Corporations Act:**
Both Acts prohibit "unconscionable conduct" which is regularly invoked by customers against financial services providers.

Disclosing customer information based on unverified AI sources could constitute unconscionable conduct, especially given the power imbalance between bank and customer.

And beyond any potential specific violations, there's all sorts of potentially systemic things here:

1. **Absence of Verification Protocols:** No verification of information accuracy from external AI sources
2. **Lack of Authority Checks:** No assessment of disclosure authority or customer consent
3. **Missing Security Controls:** No safeguards over external AI system reliance for customer information
4. **Training Failures:** Staff appear unaware of confidentiality obligations
5. **Use of Personal Devices/Accounts**

[I'm big mad](https://www.linkedin.com/posts/parisba_privacy-australia-useless-activity-7360481919626612736-h_DP/).