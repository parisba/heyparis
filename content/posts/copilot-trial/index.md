---
title: "Microsoft's Copilot Trial Report: Reading Between the Lines"
draft: true
date: 2026-01-07
cover:
  image: "cover.jpg"
  alt: "Microsoft's Copilot Trial Report"
  relative: true
ShowToc: false
params:
  description: The Australian Government's Copilot trial report is a masterclass in presenting concerning findings as successes. What does the data actually show?
  images:
  - cover.jpg
  title: "Microsoft's Copilot Trial Report: Reading Between the Lines"
tags: ["ai", "microsoft", "copilot", "australia", "policy", "auspol", "analysis", "government", "trial"]
---

From January to June 2024, the Digital Transformation Agency coordinated [Australia's whole-of-government trial of Microsoft 365 Copilot](https://www.digital.gov.au/initiatives/copilot-trial), distributing over 7,769 licenses across almost 60 participating agencies. It was, according to [Nous Group](https://nousgroup.com/case-studies/copilot-comes-to-canberra), "the world's largest whole-of-government AI trial".

The [evaluation report](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full) released alongside the APS AI Plan has been presented as evidence that generative AI is ready for government deployment. Minister Gallagher cited it as demonstrating the potential for AI to "[free up staff for work requiring human insight, empathy, and judgment](https://ministers.finance.gov.au/financeminister/media-release/2025/11/12/whole-government-ai-plan-released)". [Microsoft's press release](https://news.microsoft.com/en-au/features/microsoft-365-copilot-delivers-productivity-gains-with-australian-public-servants/) celebrated "productivity gains with Australian public servants".

Read the actual report, though, and a different picture emerges. One where the majority of users found little value in the tool. Where 60% of outputs required "moderate to significant" editing. Where the system exposed sensitive data that staff shouldn't have accessed. Where the government was explicitly warned that women would be disproportionately affected.

Let's look at what the report actually says.

## The Expectations Gap

Before the trial, [75% of staff expected](https://www.theregister.com/2025/02/12/australian_treasury_copilot_pilot_assessment/) that Copilot would be useful for some of their work tasks. Only 6% thought it would be of little or no use.

After the trial? **59% found they had little or no use for it.** Only 38% said they used it for some of their tasks.

That's a remarkable reversal. The government rolled out an AI tool to thousands of public servants, and the majority concluded it wasn't useful for their work. This isn't a minor disappointment, it's a fundamental mismatch between promise and reality.

[Treasury's separate evaluation](https://evaluation.treasury.gov.au/publications/evaluation-generative-artificial-intelligence) found the same pattern: "The use of Microsoft Copilot in Treasury failed to meet the high expectations of public servants but proved helpful with basic tasks."

Helpful with basic tasks. That's not the transformative productivity revolution the government is promising.

## The 60% Edit Rate

One of the most significant findings is buried in the middle of the report. [According to the DTA](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/productivity):

> "60% of trial participants claiming they had to make a moderate to significant number of edits to outputs."

Think about what this means. In a majority of cases, the AI's output couldn't be used as-is. Public servants had to substantially rework what Copilot produced.

The report frames this as needing to "tailor content for the audience or context". That's one interpretation. Another interpretation is that the AI produced outputs that were wrong, inappropriate, or inadequate 60% of the time.

The report acknowledges that "due to fears of hallucinations, [participants] combed through Copilot's outputs to verify its accuracy. In some cases, this involved reading the entire document Copilot produced to check for any errors which significantly reduced any efficiency gains."

Reading an entire AI-generated document to check for errors isn't productivity. It's extra work.

[Up to 7% of respondents](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/productivity) reported that Copilot actually **added time** to tasks, partly due to the verification effort required.

## The Sensitive Data Problem

Perhaps the most alarming finding relates to data security. From the [report](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/whole-government-adoption-generative-ai):

> "Use of Copilot enabled some participants to access documents that they should not have had permission to access."

And:

> "Trial participants raised instances where Copilot surfaced sensitive data that staff had not classified or stored appropriately."

[IDM Magazine reported](https://idm.net.au/article/0014949-aps-copilot-trial-highlights-information-governance-shortcomings) that the trial revealed "inappropriate access and sharing of sensitive information" due to "poor information, data management practices and permissions".

The report attributes this to pre-existing data governance failures rather than Copilot itself. That's technically accurate. But it raises an obvious question: **if government agencies can't properly classify and secure their data, should they be deploying AI systems that surface and synthesise that data?**

The report notes that "without the appropriate data infrastructure and governance in place, the use of Copilot may further exacerbate risks of data and security breaches in the APS."

This warning wasn't heeded. The APS AI Plan proceeds with GovAI deployment in April 2026, built on the same SharePoint infrastructure with the same data governance gaps.

The [Queensland Government's guidance](https://www.forgov.qld.gov.au/information-technology/queensland-government-enterprise-architecture-qgea/qgea-directions-and-guidance/qgea-policies-standards-and-guidelines/controlling-data-exposure-copilot-and-copilot-for-m365-guideline) now explicitly warns that "data sources accessed by M365 Copilot may contain personal, protected, sensitive, or official information that has been misclassified or secured appropriately. This may lead to the uncontrolled or unauthorised exposure of data."

## The Janusseal Integration Failure

The trial also revealed integration problems with Janusseal, the software that enables data classification for Windows users across government. [ARN reported](https://www.arnnet.com.au/article/3583551/dta-trial-of-microsoft-copilot-flags-integration-data-permission-issues.html):

> "There was a lack of Copilot integration with third-party software, in particular with Janusseal... Interviews conducted by the DTA noted a lack of integration with Janusseal could lead to APS staff gaining access to information they did not have permissions for."

Microsoft's response was to call it "a third-party labelling issue, not a security issue". They advised that "a more permanent fix to the labelling issue is in the pipeline".

"In the pipeline" means not fixed. The government is proceeding with broader AI deployment while a known security integration remains unresolved.

## The Women Warning

The [unintended outcomes section](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full/unintended-outcomes) of the report contains an explicit warning about gendered impacts:

> "Interviews with Australian Government agencies highlighted that women could be disproportionately impacted as they currently comprise most APS administration staff."

And:

> "Interviewees remarked that entry-level administration jobs are important pathways for women and other marginalised groups to enter the APS."

And:

> "It was feared that time savings from administrative tasks, such as note-taking and producing minutes, could lead to job loss among administration staff."

This isn't speculation from external critics. This is what government agencies told the DTA during the trial. They explicitly flagged that the technology they were testing could disproportionately harm women's employment.

The report recommends that "generative AI's impact on employment opportunities across different demographics should be regularly monitored". But there's no indication this is happening. The APS AI Plan contains [no gender impact analysis](https://www.bpw.com.au/Blog/13527111). No job security guarantees. No commitments to protect the pathways for women into the public service.

Minister Gallagher, who is also Minister for Women, champions a plan that her own department's trial explicitly warned would disproportionately harm women.

## The Productivity Claims

The trial did find some productivity benefits. [Microsoft's press release](https://news.microsoft.com/en-au/features/microsoft-365-copilot-delivers-productivity-gains-with-australian-public-servants/) headlines "about an hour per day" saved on tasks.

But look at the context. The same report notes that:

- Only 22% of participants used Copilot 4-5 times per week
- Only a third used it daily
- 59% found little or no use for it
- 7% found it added time to tasks

If you only measure productivity gains among the minority who actually found the tool useful, you'll find productivity gains. That's selection bias, not evidence of broad benefit.

The [cost-benefit analysis](https://ia.acs.org.au/article/2025/treasury-releases-microsoft-copilot-trial-results.html) is revealing: "A public servant at the level of APS6, a mid-level employee, would only need to redirect about 13 minutes of time from low-value to high-value tasks per week to offset these expenses."

Thirteen minutes per week is the bar for justifying Copilot's cost. That's an admission that the productivity gains are marginal at best. It's not "transforming work for the 21st century". It's barely breaking even.

## The Cultural Data Problem

The report also flags risks around cultural sensitivity:

> "Outputs may skew toward Western norms and could mishandle cultural data (e.g., First Nations words or imagery) without safeguards."

This is a significant concern for an Australian government AI deployment. The APS serves all Australians, including Indigenous communities with specific cultural and linguistic requirements. A system trained on predominantly Western data may produce outputs that are inappropriate, offensive, or simply wrong in these contexts.

The report doesn't indicate how this risk is being mitigated. The APS AI Plan contains no specific provisions for Indigenous data sovereignty or cultural appropriateness testing.

## The Bias Perpetuation Risk

The report acknowledges another fundamental concern:

> "Generative AI models can inadvertently amplify societal biases present in their training data. This could lead to outputs that reflect historical inequalities and stereotypes."

This isn't theoretical. AI systems have documented track records of [racial bias in healthcare](https://pmc.ncbi.nlm.nih.gov/articles/PMC11542778/), [gender bias in hiring](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G/), and [discrimination against non-English names](https://www.amnesty.org/en/documents/eur35/4686/2021/en/) in government systems.

The Copilot trial identified this risk. The APS AI Plan doesn't meaningfully address it.

## What the Report Actually Shows

Strip away the ministerial spin and the Microsoft marketing, and here's what the Copilot trial demonstrated:

1. **Most users didn't find it useful.** 59% reported little or no use after the trial, despite 75% expecting it would help.

2. **Most outputs required significant editing.** 60% needed moderate to substantial rework, negating efficiency claims.

3. **It created security vulnerabilities.** The system surfaced sensitive data that staff shouldn't access, exposing pre-existing governance gaps.

4. **It poses equity risks to women.** The government's own trial flagged disproportionate impact on women in administration roles.

5. **Cultural and bias risks remain unaddressed.** The system may perpetuate Western norms and historical biases without safeguards.

6. **Productivity gains are marginal.** The break-even point is 13 minutes of value per week per user.

This is the evidence base on which the government is building GovAI and planning whole-of-APS deployment.

## What Should Have Happened

A responsible response to these findings would have been:

- **Pause broader deployment** until the security integration issues are resolved
- **Commission gender impact analysis** given the explicit warnings about women
- **Develop cultural appropriateness testing** before deploying in contexts affecting Indigenous Australians
- **Set minimum utility thresholds** requiring evidence that most users (not just 38%) find value before mandating adoption
- **Address the data governance gaps** that the trial exposed before deploying AI that exacerbates them

Instead, the government took a trial with mixed-to-concerning results and used it to justify accelerating deployment.

The Copilot trial wasn't evidence that AI is ready for government. It was evidence that AI deployment outpaces both technical readiness and policy consideration. The government chose to read it as the former.

---

*The full Copilot trial report is available [here](https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full). Treasury's separate evaluation is [here](https://evaluation.treasury.gov.au/publications/evaluation-generative-artificial-intelligence). If you're a public servant who participated in the trial and want to share your experience, I'd be interested to hear from you.*
