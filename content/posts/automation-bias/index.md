---
title: "Automation Bias in High-Stakes Government: What the Evidence Actually Says"
draft: true
date: 2026-01-07
cover:
  image: "cover.jpg"
  alt: "Automation Bias in High-Stakes Government"
  relative: true
ShowToc: false
params:
  description: What does the empirical research actually say about automation bias in government decision-making? The findings aren't reassuring.
  images:
  - cover.jpg
  title: "Automation Bias in High-Stakes Government: What the Evidence Actually Says"
tags: ["ai", "automation bias", "australia", "policy", "research", "evidence", "government", "welfare", "decision making"]
---

The Australian government's AI strategy rests on a comforting assumption: that human-in-the-loop oversight will catch AI errors. Minister Gallagher [assures us](https://ministers.finance.gov.au/financeminister/media-release/2025/11/12/whole-government-ai-plan-released) that AI won't "decide that someone gets a payment or not" because humans will remain in control. The APS AI Plan requires public servants to "[critically assess generative AI outputs](https://www.digital.gov.au/policy/ai/staff-guidance-public-generative-ai)" for accuracy and bias.

This faith in human oversight contradicts decades of empirical research. The evidence shows that when AI provides recommendations, humans systematically fail to catch errors, frequently override their own correct judgments in favour of flawed AI outputs, and are most susceptible to this bias in exactly the high-stakes contexts where government AI will be deployed.

The phenomenon is called automation bias, and it may be the most significant risk in government AI that almost nobody is talking about.

## What Is Automation Bias?

Automation bias is, according to a [systematic review in the Journal of the American Medical Informatics Association](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/), "the propensity for humans to favor suggestions from automated decision-making systems and to ignore contradictory information made without automation, even if it is correct".

It manifests in two forms:

**Omission errors**: Issues go unnoticed because the system fails to flag them. If the AI doesn't alert you to a problem, you're less likely to spot it yourself.

**Commission errors**: Incorrect automation output is uncritically adopted. If the AI recommends a decision, you're more likely to accept it even when it's wrong.

This isn't about laziness or incompetence. It's a [documented cognitive phenomenon](https://link.springer.com/article/10.1007/s00146-025-02422-7) that affects trained professionals across domains. The more people trust AI systems, and the more cognitive load they're under, the worse it gets.

## The Numbers

Across [multiple empirical studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/), automation bias causes errors in **6% to 11% of decisions** where AI systems provide incorrect advice. That doesn't sound like a lot until you consider the scale of government operations.

Services Australia processes [millions of welfare decisions annually](https://www.servicesaustralia.gov.au/annual-report-2022-23). If AI-assisted decision support has a 6-11% automation bias rate on incorrect recommendations, and even a small fraction of AI recommendations are wrong, the aggregate harm could be substantial.

Some specific findings:

- A [2023 study on AI-assisted pathology](https://arxiv.org/html/2411.00998v1) found a **7% automation bias rate**: initially correct evaluations were overturned after erroneous AI advice. This is trained medical professionals making worse decisions *because* of AI, not despite it.

- An [earlier study by Friedman et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) found clinicians overrode their own correct decisions in favour of erroneous DSS advice in **6% of cases**.

- Research on [breast cancer diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) found that cancers diagnosed in **46%** of cases without automated aids were discovered in only **21%** of cases when automated aids failed to identify them. The AI's miss became the human's miss.

- A [randomized crossover study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10731487/) found that "clinicians of all expertise levels were vulnerable to automation bias", with **nearly half of errors** associated with misleading AI.

These aren't theoretical projections. They're documented outcomes in controlled research environments with motivated, trained participants.

## Public Sector Specific Research

The most directly relevant study for Australian policymakers is [Human–AI Interactions in Public Sector Decision Making](https://academic.oup.com/jpart/article/33/1/153/6524536), published in the *Journal of Public Administration Research and Theory* in 2022.

The researchers conducted an experiment with **1,345 actual Dutch civil servants** from various policy areas and government levels. They were specifically interested in how public sector workers respond to AI recommendations, and they conducted the study shortly after the [Dutch childcare benefits scandal](https://en.wikipedia.org/wiki/Dutch_childcare_benefits_scandal), a case where algorithmic discrimination destroyed thousands of families.

Their findings:

> "Overall, the study speaks to potential negative effects of automation of the administrative state for already vulnerable and disadvantaged citizens."

The researchers found evidence of both automation bias (accepting incorrect AI recommendations) and "selective adherence" (patterns in when officials choose to follow AI). The combination means AI systems can systematically harm particular groups while appearing to work correctly in aggregate.

This isn't an abstract concern. In the Netherlands, algorithmic decision-making in welfare [led to 35,000 families being falsely accused of fraud](https://www.amnesty.org/en/latest/news/2021/10/xenophobic-machines-dutch-child-benefit-scandal/), with [dual nationality used as a risk factor](https://www.amnesty.org/en/documents/eur35/4686/2021/en/). When individuals were flagged, civil servants were required to conduct manual review but [given no information as to why the system generated a higher-risk score](https://www.uva.nl/en/shared-content/faculteiten/en/faculteit-der-rechtsgeleerdheid/news/2023/02/childcare-benefit-scandal-transparency.html). The result was rubber-stamping of discriminatory outputs.

The scandal [brought down the Dutch government in 2021](https://en.wikipedia.org/wiki/Dutch_childcare_benefits_scandal). More than 2,000 children were removed from their families.

## Why Human Oversight Fails

The research identifies several reasons why "human-in-the-loop" protections don't work as intended:

**Cognitive load.** Automation bias [appears to be associated with the degree of cognitive load](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) experienced in decision tasks. Government workers processing high volumes of cases under time pressure are exactly the population most susceptible.

**Opaque systems.** When humans can't understand *why* an AI made a recommendation, they can't effectively evaluate it. [Clinicians require 2.3 times longer](https://pmc.ncbi.nlm.nih.gov/articles/PMC11542778/) to audit deep neural network decisions compared to traditional rule-based systems. In practice, this means they often don't.

**Trust calibration.** If an AI system is usually accurate, humans calibrate their trust accordingly, but this makes them *more* susceptible to the errors that slip through. [Studies show](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) "participants made significantly more AB errors when assisted by automation that was constantly highly accurate compared to automation that varied between high and low accuracy".

**Expertise paradox.** [Non-specialists, who stand to gain the most from AI decision support, are also the most susceptible to automation bias](https://arxiv.org/html/2411.00998v1). The government workers least equipped to catch AI errors are the ones most likely to trust them.

**Time pressure.** Research on [AI-assisted medical decision-making](https://arxiv.org/html/2411.00998v1) found "automation bias, where users uncritically follow automated cues, may worsen when time pressure strains practitioners' cognitive resources". Government service delivery is a high-time-pressure environment.

## Explanations Don't Fix It

A common response is that "explainable AI" will solve the problem: if systems explain their reasoning, humans can catch errors.

The evidence suggests otherwise.

A [2023 study from the University of Melbourne](https://www.sciencedirect.com/science/article/abs/pii/S000437022300098X) found that explanations "did not reduce this aspect of automation bias and sometimes increased it". A [comprehensive review](https://link.springer.com/article/10.1007/s00146-025-02422-7) concluded that "current approaches may unintentionally amplify AB by fostering misplaced trust".

Why? Because explanations can make AI outputs *seem* more trustworthy without actually making them more accurate. A plausible-sounding explanation attached to a wrong answer is worse than a wrong answer with no explanation, because the human is more confident in accepting it.

## What This Means for the APS AI Plan

The [APS AI Plan](https://www.digital.gov.au/policy/ai/australian-public-service-ai-plan-2025) assumes that human oversight will mitigate AI risks. The [staff guidance](https://www.digital.gov.au/policy/ai/staff-guidance-public-generative-ai) tells public servants to "critically assess generative AI outputs" and warns that AI can "produce convincing but inaccurate content".

This is necessary advice. It's also insufficient.

If the empirical research is correct, and there's no reason to think Australia is exempt from documented cognitive phenomena, then:

1. **6-11% of AI errors that should be caught will be accepted.** Public servants will override their own correct judgments in favour of flawed AI recommendations.

2. **Vulnerable populations will be disproportionately affected.** The Dutch experience shows how algorithmic bias interacts with automation bias to systematically harm marginalised groups.

3. **Training won't solve the problem.** While training can help, automation bias affects [trained professionals at all expertise levels](https://arxiv.org/html/2411.00998v1). Telling people to be careful isn't enough.

4. **High-volume, time-pressured environments are highest risk.** These are exactly the government contexts (welfare processing, visa applications, compliance checking) where AI is being promoted for "efficiency" gains.

5. **Errors will be harder to detect than Robodebt.** Robodebt was a rules-based system with deterministic outputs. Its errors could be traced, documented, and litigated. Generative AI systems are probabilistic black boxes. When they contribute to wrong decisions, proving causation is exponentially harder.

## What Actually Mitigates Automation Bias

The research literature identifies some interventions that help:

**Increased accountability.** Making users personally responsible for outcomes, not just for using the system correctly, [reduces inappropriate reliance](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/).

**Dynamic confidence indicators.** Showing users how confident the AI is in its recommendation, updated in real-time, [can improve appropriate reliance](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/).

**Training that emphasises AI fallibility.** Not just how to use the system, but specific training on when and how it fails.

**Reduced cognitive load.** If automation bias worsens under cognitive load, reducing that load, through manageable caseloads, adequate staffing, reasonable time pressures, is protective.

**Meaningful recourse mechanisms.** If affected individuals can challenge AI-influenced decisions through accessible review processes, errors are more likely to be caught.

The [OECD's 2025 report on Governing with Artificial Intelligence](https://www.oecd.org/en/publications/2025/06/governing-with-artificial-intelligence_398fa287.html) makes similar points: "skewed data in AI systems can cause harmful decisions; lack of transparency erodes accountability; and overreliance can widen digital divides and propagate errors, reducing citizen trust".

## The Policy Gap

The Australian government's AI strategy doesn't engage meaningfully with the automation bias literature.

The APS AI Plan mentions the need for "human oversight" but doesn't address what the research says about its limitations. There's no discussion of how to structure decision-making processes to mitigate documented cognitive failures. No acknowledgment that "human-in-the-loop" is a necessary but insufficient safeguard.

The [AI Review Committee](https://ministers.finance.gov.au/financeminister/media-release/2025/11/12/whole-government-ai-plan-released) has no published mandate to assess automation bias risks. The [transparency statements](https://www.digital.gov.au/policy/ai/australian-public-service-ai-plan-2025/what-we-plan-achieve) agencies must publish contain no requirement to disclose error rates or bias testing results. The [Chief AI Officers](https://ia.acs.org.au/article/2025/chief-ai-officers-coming-to-australian-govt-agencies.html) being appointed are tasked with "driving adoption", not managing cognitive risks.

This is a gap that will be filled by errors. And those errors will fall hardest on the people least able to challenge them: welfare recipients, visa applicants, and others who interact with government systems from positions of vulnerability.

## What Should Happen

If the government is serious about avoiding another Robodebt, it should:

1. **Commission Australian research on automation bias in public sector contexts.** The Dutch study shows this can be done. Australia should understand how its own public servants respond to AI recommendations.

2. **Develop evidence-based protocols for human-AI interaction.** Not generic guidance to "be critical", but specific workflows designed to mitigate documented cognitive failures.

3. **Require error rate disclosure.** Agencies deploying AI should be required to track and publish how often AI recommendations are accepted, modified, and rejected, and the outcome accuracy in each category.

4. **Fund affected population research.** Study how AI-influenced government decisions affect Indigenous Australians, CALD communities, people with disabilities, and other groups who historically bear the burden of government system failures.

5. **Build automation bias mitigation into system design.** Before deploying AI decision support, require demonstrated evidence that the design incorporates known mitigation strategies.

None of this is happening. Instead, we're getting reassurances about human oversight and critical assessment, assurances that contradict the empirical evidence on how humans actually interact with AI systems.

The Dutch found out what happens when governments trust algorithms more than evidence. Robodebt showed Australia has the same vulnerabilities. The question is whether we'll learn from either experience before GovAI goes live.

---

*Key sources for this piece include the [systematic review of automation bias](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) in JAMIA, the [Dutch civil servant study](https://academic.oup.com/jpart/article/33/1/153/6524536) in JPART, the [OECD's Governing with AI report](https://www.oecd.org/en/publications/2025/06/governing-with-artificial-intelligence_398fa287.html), and [Amnesty International's investigation](https://www.amnesty.org/en/documents/eur35/4686/2021/en/) of the Dutch childcare benefits scandal. All errors in synthesis remain my own.*
