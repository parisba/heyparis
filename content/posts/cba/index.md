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

CBA has been naughty, and too reliant on their AI boyfriend. Here's what happened:
- A CBA customer contacted bank requesting contact details for "Secretlab"
- CBA staff member queried ChatGPT to obtain phone number for "Secretlab"
- CBA staff disclosed the retrieved phone number to the requesting customer
- The retrieved phone number is a private number belonging to one of the directors of Secret Lab, a customer of CBA
- Therefore, CBA disclosed customer personal information to another, unrelated customer, and trusted a third-party LLM (ChatGPT), accessed seemingly unauthenticated on the consumer ChatGPT platform, as a source for data to provide to another customer
- During investigation, CBA staff replicated the same ChatGPT query process, seemingly on a personal phone, again unauthenticated, and on the consumer ChatGPT platform
- Signs indicate this might be routine practice amongst CBA staff

It certainly feels like CBA has violated, or come pretty close to violating, a lot of things, and this doesn't _feel good_...

For example, the _Privacy Act 1988_ (Cth), and the Australian Privacy Principles:

**APP 6: Use or Disclosure of Personal Information:**
Personal information may only be used or disclosed for the primary purpose of collection or related secondary purposes. Disclosure of customer contact information to another customer falls outside permitted purposes.

**APP 8 - Cross-border Disclosure:**
> "Before an APP entity discloses personal information about an individual to a person (the overseas recipient) who is not in Australia or an external Territory, the APP entity must take such steps as are reasonable in the circumstances to ensure that the overseas recipient does not breach the Australian Privacy Principles."

**Violation:** Querying ChatGPT involves transmitting the customer's business name to OpenAI's international servers, and relying on information sourced from those servers, without adequate safeguards for data handling. OK, admittedly, our business name isn't really personal information, but they still transacted with a cross-border entity for the information about us they then gave the other customer.

**APP 11 - Security of Personal Information:**
> "An APP entity must take such steps as are reasonable in the circumstances to protect the personal information that it holds from misuse, interference and loss and from unauthorised access, modification or disclosure."

**Violation:** Staff relying on unverified external AI sources for customer information retrieval and subsequent disclosure fails to meet reasonable security standards for protecting customer information.

And the _Banking Code of Practice_:

**Section 41 - Privacy:**
The Banking Code requires banks to handle customer information in accordance with privacy laws and maintain appropriate confidentiality safeguards.

**Violation:** Disclosure of customer information to another customer without consent or legal authority breaches fundamental confidentiality obligations.

And AUSTRAC:

**Customer Due Diligence Requirements:**
AUSTRAC mandates banks maintain robust "Know Your Customer" (KYC) procedures and ongoing customer due diligence. Banks must verify customer identity using "reliable and independent documents or electronic data" from "at least two separate data sources."

**Violation:** Using ChatGPT as a source for customer information violates AML/CTF requirements for reliable, verified information sources and proper customer due diligence procedures. So, this wasn't really part of a due diligence/KYC process, but they used it as a source of information, when it's not reliable or accurate.

And then there's the Australian Consumer Law, specifically Misleading or Deceptive Conduct:

**Section 18 - Competition and Consumer Act 2010:**
> "A person must not, in trade or commerce, engage in conduct that is misleading or deceptive or is likely to mislead or deceive."

**Violation:** CBA's disclosure of unverified information sourced from ChatGPT could constitute misleading conduct by presenting potentially inaccurate information as reliable to customers.

And, of course, ASIC: 

**Section 12DA - Misleading or Deceptive Conduct in Financial Services:**
> "A person must not, in trade or commerce, in relation to financial services engage in conduct that is misleading or deceptive or is likely to mislead or deceive."

**Violation:** Providing unverified customer information in a financial services context constitutes misleading conduct under financial services-specific legislation.

For fun, we can also look at the _Telecommunications Act 1997)_ (Cth):

**Part 13 - Telecommunications Interception and Access:**
Unauthorised disclosure of customer telecommunications information (including phone numbers) may constitute a breach of telecommunications privacy provisions.

For even more fun, we can look at the CBA Privacy Statement:

**From CBA's Group Privacy Statement:**
> "We take our responsibility to protect your privacy very seriously. We apply strict security and privacy controls to the way we handle your personal information."

**Violation:** Staff querying external AI systems for customer information and disclosing retrieved results contradicts CBA's stated commitment to strict privacy controls.

**Permitted Sharing Categories:**
CBA's privacy policy lists specific circumstances for information sharing, including:
- Other CommBank Group companies
- Authorised third parties (with consent)
- Strategic business partners
- Regulatory/law enforcement bodies
- Service providers for transaction processing

**Violation:** Sharing customer information with another unrelated customer is not included in any permitted category.

And the CBA Information Security Policy Framework:

**From CBA's published policies:**
> "We use a range of physical, electronic and other security measures to protect the security, confidentiality and integrity of the personal information we hold about you."

**Violation:** Staff relying on unverified external AI systems for customer information contradicts CBA's commitment to protecting information security and integrity.

And their [Code of Conduct](https://www.commbank.com.au/content/dam/commbank-assets/about-us/docs/cba-code-of-conduct.pdf):

**Internal Policy Framework:**
CBA's Code of Conduct requires staff to act with integrity and follow proper procedures when handling customer information.

**Violation:** Using external AI tools without proper authorisation or verification procedures breaches internal conduct standards.

For even more fun, we can think about Unconscionable Conduct:
**ASIC Act and Corporations Act:**
Both Acts prohibit "unconscionable conduct" which is regularly invoked by customers against financial services providers.

**Violation:** Disclosing customer information based on unverified AI sources could constitute unconscionable conduct, especially given the power imbalance between bank and customer.

And of course there's our old friend, the Banking Code of Practice:

**Customer Information Protection:**
> "A Bank shall take reasonable steps to protect personal information held by it relating to a Customer against loss and against access, use, modification or disclosure that is unauthorised."

**Violation:** The disclosure was unauthorised and failed to implement reasonable protective steps.

**Professional Standards:**
The Banking Code requires banks to maintain professional standards in customer service and information handling.

**Violation:** Using unverified external AI sources fails to meet professional banking standards.

And beyond any potential specific violations, there's all sorts of potentially systemic things here:

1. **Absence of Verification Protocols:** No verification of information accuracy from external AI sources
2. **Lack of Authority Checks:** No assessment of disclosure authority or customer consent
3. **Missing Security Controls:** No safeguards over external AI system reliance for customer information
4. **Training Failures:** Staff appear unaware of confidentiality obligations
5. **Use of Personal Devices/Accounts**

[I'm big mad](https://www.linkedin.com/posts/parisba_privacy-australia-useless-activity-7360481919626612736-h_DP/).