---
title: "Back to Linux"
draft: true
date: 2026-01-05
cover:
  image: "cover.jpg"
  alt: "A Framework 13 laptop running Fedora 43"
  relative: true
ShowToc: false
params:
  description: I moved my personal laptop back to Linux, on a second-hand AMD Framework 13 running Fedora 43. It's great—with caveats.
  images:
    - cover.jpg
  title: "Back to Linux"
tags: ["linux", "fedora", "framework", "laptop", "amd", "hardware", "technology", "yarn spinner", "dotnet", "unity", "godot", "apple"]
---

I've moved my personal laptop back to Linux. A second-hand AMD Framework 13, running Fedora 43 Workstation. And honestly? It's pretty great.

If you're wondering why, you might want to read about [my recent Apple ID disaster](/posts/appleid/)—twenty years of digital life, nearly gone in an instant because Apple's gift card fraud detection decided I was guilty until proven innocent. That accelerated some thinking I'd already been doing about reducing my dependence on any single megacorp's ecosystem. This laptop is part of that.

I say "back to" but that's underselling the gap. I haven't been a regular Linux user since 2003. Before that, I ran Slackware for years—back when configuring X11 was a rite of passage and you kept a printed copy of the kernel compilation options next to your desk. I've been an Apple user since childhood—Apple IIs, various Performas, PowerBooks, iMacs—but when OS X arrived and finally gave me a Unix terminal on top of a polished GUI, I switched fully and never really looked back. That was over twenty years ago.

So this isn't "I tried Ubuntu last year and it didn't stick." I'm returning to something I left behind two decades ago, on hardware and with a distribution that didn't exist back then.

But this time feels different. Fedora 43 is *polished*. Not "polished for Linux" polished—actually polished. The kind of polished where I forget I'm running Linux for hours at a time because everything just works the way I expect it to.

GNOME looks good. Fractional scaling works. Bluetooth pairs without rituals. Suspend resumes. Firefox is fast. Flatpak means I don't have to think about dependencies. The terminal is obviously excellent. I plugged in an external monitor and it just... worked. At the correct resolution. With the correct scaling. I didn't have to edit a config file or restart anything.

I know.

## The Framework Factor

Part of this is the Framework 13 itself. Framework builds laptops specifically designed to work well with Linux, and the AMD version in particular is well-supported. Buying second-hand was a nice bonus—someone else dealt with the early adopter firmware updates, and I got a machine that's already settled into its final form.

The hardware is good. The keyboard is good. The screen is good. The modularity is a fun gimmick that I'll probably never actually use, but I appreciate that I *could* swap out ports if I wanted to. It feels like a laptop made by people who actually use laptops, rather than people who think laptops should be thinner than a credit card and missing half their keys.

I'm not entirely sold on Framework as a company, mind you. They've thrown money at some open source projects run by people I'd rather not see platformed—the sort of loud tech contrarians who mistake being obnoxious for being principled. The hardware is good. I can hold my nose about the rest.

## Actually Getting Work Done

Can I actually do my job on this thing? Yes. Very much yes.

[Yarn Spinner](https://yarnspinner.dev) development works. The .NET SDK installs cleanly, runs fast, and everything just works. I expected this to be a pain point—cross-platform .NET on Linux has historically been "technically possible but annoying"—but it's not. It's just normal development. VS Code works exactly as it does everywhere else. The C# extension works. The debugger works. I can build, test, and publish without thinking about what OS I'm on.

Web development is obviously fine. It's Linux. This is its home turf.

Game engines work. Godot runs great, as you'd expect—it's open source and Linux is a first-class citizen. Unity, surprisingly, also works without issue. The Linux editor has come a long way from the "experimental" days, and on this hardware it's smooth. I haven't tried building for every platform yet, but the editor experience is solid.

Creative tools are where it gets complicated. Krita is fine—capable software—but it's not Sketch. The UX is different, the workflow is different, and muscle memory built over years doesn't transfer. I can do what I need to do, but I'm slower and more frustrated doing it. That's not Krita's fault. It's a different tool with different priorities.

Note-taking and knowledge management is the bigger question mark. I've been a DEVONThink user for years—excellent software with no real equivalent on Linux. I'm trying Obsidian as a replacement. Jury's still out. Obsidian is good at what it does, but it's a different paradigm: Markdown files in folders versus a database with AI-powered classification and search. I'm giving it a proper go. We'll see.

## The Caveats

Because there are always caveats.

**Battery drain during sleep.** The laptop loses power while suspended. Not a lot—maybe a few percent an hour—but enough that I can't close the lid on Friday afternoon and expect it to still be alive on Monday morning. This is an AMD thing, not a Fedora thing, and it's apparently related to s2idle versus deep sleep and a bunch of other acronyms I don't care to fully understand. There are workarounds. I haven't bothered yet. I just shut it down if I'm not going to use it for a while.

**PSR hangs.** Panel Self Refresh, a power-saving feature for the display, occasionally causes the whole system to lock up for a few seconds. It's rare—maybe once a week—and it always recovers, but it's annoying. Again, there are kernel parameters I could tweak. Again, I haven't bothered yet. It's not frequent enough to make me actually fix it.

That's it. That's the list. Two things, both minor, both with known workarounds. Compare that to 2003, when getting Linux running on a laptop meant recompiling the kernel for your specific hardware, praying your WiFi chipset was supported, and accepting that suspend/resume was a fantasy.

## The Verdict

I'm keeping it. Fedora 43 on the Framework 13 is the first Linux laptop setup I've used that feels like a complete product rather than a project. It's not perfect—nothing is—but the imperfections are the kind I can live with.

The development story is excellent. .NET, web, Godot, Unity—it all just works. The creative and productivity tool story is more complicated, and I suspect that's where most people will hit friction. If you live in Figma and Google Docs, you're fine. If you depend on specific macOS software with no real equivalent, you'll have to decide whether the trade-offs are worth it.

For me, right now, they are. I'll check back in six months and let you know if the honeymoon phase has worn off. But for now? I'm enjoying using my computer, and that's worth something.
