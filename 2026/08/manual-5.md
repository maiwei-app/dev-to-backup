# Multi-Device with Claude Code

**Published:** 2026-08-07
**URL:** https://dev.to/colomr/multi-device-with-claude-code-179l
**Tags:** #claude, #claudecode, #programming, #tooling
**Reading time:** 3 min

---

## The Problem
Using Claude Code across different devices in my end-to-end workflow leads to a frustration you might find familiar: when I switch devices, it's like having an intern who's forgotten everything I taught them by Monday morning.

It's not that the code disappears. The code is on GitHub. But those settings, personalised instructions in `CLAUDE.md`, hooks that automated your workflows, even your preferences for which models to use in each context... they vanish as if they never existed.

Then there's another problem I call **cognitive inconsistency**. You work in the evening on your laptop with one set of rules, tomorrow on your desktop those rules don't work. It's not a technical bug, it's an accumulation of circumstances (_keep reading_…).

There's a constant battle of weights. Your instructions in `CLAUDE.md` compete with the system's weights: the defaults Anthropic puts in place, the "safe" behaviors baked into the model. Sometimes you win, sometimes you don't. It's probabilistic, and it changes subtly depending on the machine, the model, on what the system decides is "prioritary" that day when calling the model's endpoint. It's really like having an employee who says "yes, I understand your rules" but then does what the corporate boss ordered months ago because it gets higher priority in the weights when instructions contradict.

And this multiplies. With 2 devices it's annoying. With 3 or 4 devices you never know exactly which version of "your Claude" you're working with.

That frustration is what led me to create [claude-sync](https://github.com/colomr-cc/claude-sync).

## Claude-Sync
What I built is simple in concept: a repository that syncs your approved Claude Code configuration (_contract-id_) across all your devices.

Instead of each machine being its own configuration isolated, I now have a single source of truth on GitHub. Every time a `SessionStart` runs, a script asks: "What's the approved configuration on main? Fetch it and apply it to this machine right now."

This means your personalised `CLAUDE.md`, your automation hooks, your model preferences stay consistent across all devices. And most importantly: it's audited. If something changed in your configuration, it's in git history. You know exactly what changed, when, and why.

Each session, Claude Code shows you if there are synced changes and which version of the "contract" you're working with. This prevents _silent sync failures_ where you think you have your rules but you don't.

![Claude Code SessionStart](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/n3l5q79mymq3kln46225.png)

The intern who forgot everything now has a notebook they review every morning. And that notebook is under version control.

## Why I Built It
It wasn't a tool I planned to create. It came from accumulated frustration.

I work across multiple devices and each one is its own fragmented universe of Claude Code. I'd spend time configuring hooks, writing instructions in `CLAUDE.md`, tweaking behaviors. Then I'd sit down at another machine and have to start over. Or worse: I'd work assuming I had my personalised rules, and halfway through a project discover they weren't there.

Then there's the control problem. If your configuration is "magical" (living only on each machine), you have no visibility. You don't know what's synced, what changed, when. With `claude-sync`, it's all explicit. If it fails, you see exactly why.

It's the same principle we use for code: versioned, audited, deliberate. It shouldn't be different for the configuration that tells Claude how to work with you.

## Important: This is Beta
`claude-sync` is tailored to my specific use case. My workflow, my machines, my way of working with Claude. It probably won't be plug-and-play for you.

But that doesn't make it useless. It means it's a starting point that can inspire you to adapt it to your own flow. If you recognise the problem, you can probably take the ideas from this project and make them yours.

## Deliberate Synchronisation
It's worth exploring what happens when you turn your configuration into something versioned, audited, synchronised. The `claude-sync` repo is available. Check the [README](https://github.com/colomr-cc/claude-sync), see if it works for you as-is or if it needs custom setup.

The point isn't that you use my exact solution. The point is that you start thinking of your Claude configuration as something that deserves _version control_. Because once you do, your Claude stops being that intern who forgets everything every Monday.
