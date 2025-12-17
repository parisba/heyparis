---
title: "We released Yarn Spinner 3.1"
date: 2025-12-17
cover:
  image: "cover.jpg"
  alt: "Yarn Spinner 3.1 Release"
  relative: true
ShowToc: false
params:
  description: Yarn Spinner 3.1 is out, with async dialogue methods, option fallthrough, and more.
  images:
  - cover.jpg
  title: "Yarn Spinner 3.1 Released"
tags: ["yarn spinner"]
---

We released Yarn Spinner 3.1 on December 3, 2025, introducing several significant improvements to our dialogue system framework. This update emphasizes asynchronous operations, graceful error handling, and enhanced customization options.

## Key Features

**Async Dialogue Runner Methods** — The dialogue runner's core methods now support asynchronous operations. The `StartDialogue` and `Stop` methods are now async and return a task. This ensures that dialogue presenters complete their initialization before scene changes occur.

**Option Fallthrough for Branching** — We've addressed soft-lock scenarios with a new feature: when all dialogue options become unavailable due to unmet conditions, the system can now skip the options entirely and continue the narrative. This prevents players from reaching dead ends when conditional branches fail to provide viable choices.

**Source Tracking for LocalizedLines** — Multi-runner environments benefit from improved line attribution. The `LocalizedLine` object now includes a `Source` property, enabling developers to identify which dialogue runner generated specific content.

**Enhanced Cancellation Tokens** — Options now receive separate "hurry up" and cancellation signals, matching the functionality available for regular lines and allowing more nuanced control over presentation timing.

**Redesigned Typewriter System** — We completely rebuilt the typewriter mechanism around the `IAsyncTypewriter` interface, offering better customization opportunities. Developers can implement character appearance events through `ActionMarkupHandler` subclasses rather than event-based approaches.

## Notable Changes

Legacy `DialogueView` classes have been removed, requiring migration of older projects to the newer `DialoguePresenter` model. Additionally, Text Animator integration is now available in commercial versions, representing the first divergence between our free and paid offerings.

Tim's also put up a great blog on [Saliency Systems and State Mutation](https://yarnspinner.dev/blog/saliency-and-state-mutation/), which was inspired by a conversation we had with a user. It's a deep dive into a subtle but important issue: what happens when functions that check game state also mutate that state during saliency selection. Worth a read if you're working with saliency in your projects.

## What's Next

We've got big plans for 2026. You can read all about them in our [2026 Plans](https://yarnspinner.dev/2026) post, but the highlights include: a Visual Novel Kit, a rebuilt VS Code extension, native Unreal Engine support, continued Godot development, and our new Story Solver narrative debugging tool. We're also pursuing integrations with complementary tools like Rewired and i2Loc.

As always, Yarn Spinner will remain free and open source at its core. We fund development through paid add-ons, web services, and client work—no closing the source code, no AI integration, no seeking acquisition, and no eliminating the free tier.

Get started with Yarn Spinner with our [Beginner's Guide](https://docs.yarnspinner.dev/beginners-guide/welcome), or grab it from the [Unity Asset Store](https://assetstore.unity.com/publishers/91946) or [Itch Store](http://yarnspinner.itch.io).
