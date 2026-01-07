---
title: "Australia's AI Safety Institute: Lessons from the UK and US"
draft: true
date: 2026-01-07
cover:
  image: "cover.jpg"
  alt: "Australia's AI Safety Institute: Lessons from the UK and US"
  relative: true
ShowToc: false
params:
  description: Comparing Australia's newly announced AI Safety Institute against the UK and US equivalents. What have they actually done? What can Australia learn?
  images:
  - cover.jpg
  title: "Australia's AI Safety Institute: Lessons from the UK and US"
tags: ["ai", "ai safety", "australia", "policy", "auspol", "analysis", "uk", "us", "international", "aisi"]
---

On 25 November 2025, Minister for Industry and Innovation Tim Ayres [announced the establishment of the Australian AI Safety Institute (AISI)](https://www.minister.industry.gov.au/ministers/timayres/media-releases/establishment-australian-ai-safety-institute). With a [$29.9 million commitment](https://www.gadens.com/legal-insights/australia-launches-ai-safety-institute-and-releases-national-ai-plan/) and operations commencing "early 2026", Australia will become the latest nation to join the [International Network of AI Safety Institutes](https://www.nist.gov/system/files/documents/2024/11/20/Mission%20Statement%20-%20International%20Network%20of%20AISIs.pdf).

The timing is interesting. The UK's AI Safety Institute (now rebranded as the "[AI Security Institute](https://www.aisi.gov.uk/)") has been operational for over two years. The US AI Safety Institute has been gutted by the Trump administration and [rebranded as the "Center for AI Standards and Innovation"](https://fedscoop.com/trump-administration-rebrands-ai-safety-institute-aisi-caisi/), with "safety" explicitly excised from both its name and mission. Australia is entering a field where the two supposed leaders are heading in opposite directions.

So what has the UK actually accomplished? What went wrong in the US? And what does this tell us about Australia's prospects?

## The UK: Actually Doing Things

The UK AI Safety Institute was [established in November 2023](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute), following the Bletchley Park AI Safety Summit. With an [initial £100 million investment](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute) (the largest public AI safety commitment globally at the time), the UK has had a meaningful head start.

What have they actually done?

**Evaluations at scale.** The UK AISI has now [tested more than 30 of the world's most advanced AI models](https://www.aisi.gov.uk/blog/our-2025-year-in-review). They've conducted joint pre-deployment evaluations with the US (back when the US cared about this) of [OpenAI's o1 model](https://www.gov.uk/government/news/inaugural-report-pioneered-by-ai-security-institute-gives-clearest-picture-yet-of-capabilities-of-most-advanced-ai) and Anthropic's latest systems. Their end-to-end biosecurity red-teaming with OpenAI and Anthropic [revealed dozens of vulnerabilities](https://www.aisi.gov.uk/blog/our-2025-year-in-review), including new universal jailbreak paths. They conducted [the largest study of backdoor data poisoning to date](https://www.aisi.gov.uk/blog/our-2025-year-in-review) with Anthropic.

**Open-source infrastructure.** In May 2024, the UK [released Inspect](https://www.gov.uk/government/news/ai-safety-institute-releases-new-ai-safety-evaluations-platform), an open-source evaluation framework under an MIT licence. [Inspect](https://inspect.aisi.org.uk/) provides standardised testing techniques, [over 100 pre-built evaluations](https://inspect.aisi.org.uk/evals/), and tools for monitoring and visualising results. As Ian Hogarth, the AISI Chair, put it: "[Successful collaboration on AI safety testing means having a shared, accessible approach to evaluations](https://www.gov.uk/government/news/ai-safety-institute-releases-new-ai-safety-evaluations-platform)." The framework is now [used by governments, companies, and academics globally](https://www.aisi.gov.uk/blog/our-2025-year-in-review).

**Published research with teeth.** The December 2025 [Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report) drew on two years of evaluations to document capability trajectories. The findings are sobering: cybersecurity task success rates rose from under 9% in 2023 to around 50% in 2025, with a model completing an [expert-level cyber task requiring up to 10 years of experience](https://www.aisi.gov.uk/frontier-ai-trends-report) for the first time. Software engineering task completion rose from below 5% to over 40%.

This is what an AI safety institute should look like: actually testing systems, publishing findings, building shared infrastructure, and identifying risks *before* they materialise at scale.

## The US: What Happens When Politics Wins

The US AI Safety Institute was [established in November 2023](https://en.wikipedia.org/wiki/AI_Safety_Institute) under Biden's Executive Order on AI, housed within NIST. By August 2024, it had [signed MOUs with Anthropic and OpenAI](https://www.nist.gov/news-events/news/2024/08/us-ai-safety-institute-signs-agreements-regarding-ai-safety-research) for pre-deployment access to major new models. The [AI Safety Institute Consortium](https://www.nist.gov/news-events/news/us-ai-safety-institute-consortium-holds-first-plenary-meeting-reflect-progress-2024) grew to over 290 members. In November 2024, they launched the [Testing Risks of AI for National Security (TRAINS) Taskforce](https://www.nist.gov/news-events/news/2024/11/us-ai-safety-institute-establishes-new-us-government-taskforce-collaborate).

Then Trump happened.

Within his first week back in office, Trump [signed an executive order revoking Biden's AI governance directives](https://www.nbcnews.com/tech/tech-news/trump-administration-cuts-safety-ai-safety-institute-rcna211049). The US refused to sign the final communique at the February 2025 AI Action Summit in Paris. And on 3 June 2025, Commerce Secretary Howard Lutnick [announced the transformation](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai) of the AI Safety Institute into the "Center for AI Standards and Innovation" (CAISI).

The rebranding wasn't cosmetic. Lutnick's statement was explicit: "[For far too long, censorship and regulations have been used under the guise of national security. Innovators will no longer be limited by these standards.](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai)"

CAISI's new mission is to "[guard against burdensome and unnecessary regulation of American technologies by foreign governments](https://www.techpolicy.press/from-safety-to-security-renaming-the-us-ai-safety-institute-is-not-just-semantics/)" and "[ensure US dominance of international AI standards](https://fedscoop.com/trump-administration-rebrands-ai-safety-institute-aisi-caisi/)". The focus shifted from understanding and mitigating risks to "enhancing US competitiveness" and preventing other countries from regulating American AI companies.

As [TechPolicy.Press noted](https://www.techpolicy.press/from-safety-to-security-renaming-the-us-ai-safety-institute-is-not-just-semantics/), this wasn't about semantics. The word "safety" was deliberately removed because it implied constraints on industry. The institute that was supposed to test frontier AI systems for catastrophic risks is now primarily concerned with helping those systems reach market faster.

## Where Does Australia Fit?

Australia's $29.9 million commitment sits awkwardly between these two models. It's [a fraction of the UK's £100 million](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute), but at least it exists. The question is: which path will Australia follow?

The [ministerial announcement](https://www.minister.industry.gov.au/ministers/timayres/media-releases/establishment-australian-ai-safety-institute) offers some clues. Minister Ayres stated the AISI will "provide the capability to assess the risks of this technology dynamically over time" and that "[we need to make sure we are keeping Australians safe from any malign uses of AI](https://www.minister.industry.gov.au/ministers/timayres/media-releases/establishment-australian-ai-safety-institute)".

The AISI will join the [International Network of AI Safety Institutes](https://digital-strategy.ec.europa.eu/en/news/first-meeting-international-network-ai-safety-institutes), which now includes Australia, Canada, the EU, France, Japan, Kenya, Korea, Singapore, the UK, and (nominally) the US. This network was [launched at the Seoul Summit in May 2024](https://www.gov.uk/government/publications/seoul-declaration-for-safe-innovative-and-inclusive-ai-ai-seoul-summit-2024/seoul-statement-of-intent-toward-international-cooperation-on-ai-safety-science-ai-seoul-summit-2024-annex) and has since been renamed the "International Network for Advanced AI Measurement, Evaluation and Science" (presumably to keep the Americans onside).

But here's the problem: **Australia isn't building frontier AI systems**. The UK and US institutes exist partly to test *their own* companies' models before deployment. The UK has DeepMind. The US has OpenAI, Anthropic, Google, Meta, and a dozen others. Australia has... imported models running on Microsoft Azure.

This creates a fundamental question about scope. Is Australia's AISI going to:

1. **Test models before Australian deployment?** Meaning evaluate systems *after* they've already been released globally, which is less prevention than documentation.
2. **Contribute to international evaluation efforts?** Which requires deep technical expertise that takes years to build.
3. **Focus on Australian-specific deployment risks?** Which might be more tractable but requires different capabilities.

The [job ads currently posted](https://www.industry.gov.au/news/australia-establishes-new-institute-strengthen-ai-safety) for the AISI suggest the government is thinking about this. They're recruiting for roles covering "CBRN misuse, enhanced cyber capabilities, loss-of-control scenarios, information integrity and influence risks, and broader systemic risks arising from the deployment of increasingly capable general-purpose AI systems".

That's a broad remit. Arguably too broad for a $29.9 million institute that won't be operational until 2026.

## What Australia Should Learn

**From the UK:** Build real technical capability. The UK's Inspect framework exists because they invested in software engineers who could build it. Their evaluations have teeth because they hired researchers who know how to probe AI systems. [Over 30 technical staff](https://www.gov.uk/government/publications/ai-safety-institute-overview/introducing-the-ai-safety-institute), including senior alumni from OpenAI, Google DeepMind, and Oxford, weren't hired to write policy papers. They were hired to do science. Australia needs to decide if it's building a research organisation or a policy shop, and fund accordingly.

**From the US:** Institutions need statutory protection. The US AI Safety Institute collapsed because it existed at executive discretion. When the executive changed, so did the mission. If Australia wants an AISI that survives changes of government (and given the Coalition's likely approach to AI regulation, this matters), it needs legislative grounding, not just ministerial announcements.

**From both:** International cooperation requires something to offer. The UK can contribute evaluations, open-source tools, and technical findings to international networks. The US (under Biden) could offer access to frontier labs and testing infrastructure. What does Australia bring? If the answer is "a willingness to participate", that's insufficient. Australia needs a niche, whether that's specific risk domains, deployment context expertise, or evaluation methodologies suited to smaller nations importing AI capabilities.

## The Timeline Problem

Australia's AISI won't be operational until early 2026. By then:

- The UK will have been running for over three years
- The US will have completed its transformation into an industry-friendly standards body
- The [GovAI platform will already be live](https://ministers.finance.gov.au/financeminister/media-release/2025/11/12/whole-government-ai-plan-released) across the Australian Public Service
- Multiple federal agencies will have deployed AI systems in citizen-facing services

The AISI is arriving after the decisions have been made. It's being established to provide "expert capability to monitor, test and share information", but the technology it's supposed to monitor will already be embedded in government operations.

This isn't insurmountable. The UK AISI was established after GPT-4 was released, and still managed to build valuable capabilities. But it requires the institute to move fast, hire well, and resist pressure to become another advisory body producing reports nobody reads.

## What Actually Matters

The test of Australia's AISI won't be its press releases or international memberships. It will be whether it can answer basic questions that no Australian institution can currently answer:

- What capabilities do the AI systems deployed in Australian government services actually have?
- What are their failure modes?
- How do they perform on Australian-specific contexts (Indigenous names, regional accents, local regulatory frameworks)?
- What happens when they're wrong?

If, in two years, the Australian AISI has tested models, published findings, and built tools that other organisations actually use, it will have succeeded. If it has produced glossy reports about "AI opportunities" and "responsible innovation frameworks" while the real decisions happen elsewhere, it will have failed.

The UK has shown what's possible. The US has shown what happens when politics overrides substance. Australia gets to choose.

---

*The UK AISI's [Inspect framework](https://inspect.aisi.org.uk/) and [Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report) are both publicly available. The US AISI's transformation into CAISI is documented in [Commerce Department statements](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai). Australia's AISI announcement is [here](https://www.minister.industry.gov.au/ministers/timayres/media-releases/establishment-australian-ai-safety-institute).*
