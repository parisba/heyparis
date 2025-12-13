---
title: "20 Years of Digital Life, Gone in an Instant"
date: 2025-12-13
cover:
  image: "cover.jpg"
  alt: "20 Years of Digital Life, Gone in an Instant"
  relative: true
ShowToc: false
params:
  description: 20 Years of Digital Life, Gone in an Instant
  images:
  - cover.jpg
  title: "20 Years of Digital Life, Gone in an Instant"
tags: ["apple", "megacorp", "help", "angry", "rant", "liars"]
---

Here’s how Apple “Permanently” locked my Apple ID.

I am writing this as a desperate measure. After nearly 30 years as a loyal customer, authoring technical books on Apple’s own programming languages (Objective-C and Swift), and spending over tens and tens of thousands of dollars on devices, I have been locked out of my digital life with no explanation and no recourse.

## The Situation

My Apple ID, which I have held for around two decades, has been permanently disabled. This isn’t just an email address; it is my core digital identity. It holds terabytes of family photos, my entire message history, and is the key to syncing my work across the ecosystem.

* **The Trigger:** The only recent activity on my account was a recent attempt to redeem a $500 Apple Gift Card to pay for my 6TB iCloud+ storage plan. The code failed. The vendor suggested that the card number was likely compromised and agreed to reissue it. Shortly after, my account was locked. An Apple Support representative suggested that this was the cause of the issue.

[![](/cardfail.png#center)]()

* **The Consequence:** My account is flagged as "closed in accordance with the Apple Media Services Terms and Conditions".
* **The Damage:** I effectively have over $30,000 worth of previously-active “bricked" hardware. My iPhone, iPad, Watch, and Macs cannot sync, update, or function properly. I have lost access to thousands of dollars in purchased software and media.
  * Apple representatives claim that only the “Media and Services” side of my account is blocked, but now my devices have signed me out of iMessage, and I can’t sign out of the blocked iCloud account because… it’s barred from the sign-out API, as far as I can tell.
  * I can’t even login to the “Secure File Transfer” system Apple uses to exchange information, because it relies on an Apple ID…

[![](/locked.png#center)]()

## The Support Nightmare**
I contacted Apple Support immediately (Case ID: 102774689968). The experience was terrifyingly dismissive:

1. **No Information:** Support staff refused to tell me *why* the account was banned or provide specific details on the decision.
2. **No Escalation:** When I begged for an escalation to Executive Customer Relations (ECR), noting that I would lose the ability to do my job and that my devices were useless, I was told that "an additional escalation won't lead to a different outcome".

[![](/chat.png#center)]()


## The "New Account" Trap
Most insultingly, the official advice from the Senior Advisor was to "create a new Apple account... and update the payment information".

This advice is technically disastrous:

* **The Legal Catch:** Apple's Terms and Conditions rely on "Termination of Access." By closing my account, they have revoked my license to use their services.
* **The Technical Trap:** If I follow their advice and create a new account on my current devices (which are likely hardware-flagged due to the gift card error), the new account will be instantly linked to the banned one and disabled for circumventing security measures.
* **The Developer Risk:** As a professional Apple Developer, attempting to "dodge" a ban by creating a new ID could lead to my Developer Program membership being permanently blacklisted, amongst other things.

## Who I Am
I am not a casual user. I have literally written the book on Apple development (taking over the *Learning Cocoa with Objective-C* series, which Apple themselves used to write, for O'Reilly Media, and then 20+ books following that). I help run the longest-running Apple developer event not run by Apple themselves, /dev/world. I have effectively been an evangelist for this company’s technology for my entire professional life.

## My Plea
I am asking for a human at Apple to review this case. I suspect an automated fraud flag regarding the bad gift card triggered a nuclear response that frontline support cannot override.

I am desperate to resolve this and restore my digital life. If you can help, please email paris AT paris.id.au
