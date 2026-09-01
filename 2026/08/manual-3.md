# Who Picks the Model That Writes Your Code?

**Published:** 2026-08-27
**URL:** https://dev.to/colomr/who-picks-the-model-that-writes-your-code-402
**Tags:** #ai, #cursor, #spacexai, #programming
**Reading time:** 4 min

---

You fire off a prompt in Cursor. It runs. It works.
Now tell me which model handled it, how much context reached it, and what you just paid.

You don't know, nobody knows :(

## What happened in August

On August 14, 2026, SpaceX closed its acquisition of Anysphere, Cursor's parent company, for $60 billion in stock. Cursor moves into SpaceXAI, the structure that had already absorbed xAI. Three days later came Origin: Git hosting inside the editor.

One group now controls the model, the environment, the infrastructure, and the repository.

## The layer that decides, and nobody looks at

Between your prompt and the model sits a layer. It's called the harness.

Think of a draft harness. It doesn't give the horse strength. It couples that strength to the cart.

Before the call, the harness decides what context goes in, what invisible instructions get added, which tools exist, and what gets dropped. After the call it runs the actions against your terminal, applies permissions, and repeats the loop until the task is done.

Without that loop, the model's answer is an intent in JSON.

> Whoever controls the harness controls the apparent performance of a model they don't build.

Without touching its output. Just by choosing what reaches someone else's model.

## Two pots of credit

Cursor doesn't sell a subscription. It sells credit.
And that credit is split in two:

| Pot | Covers | How much |
| --- | --- | --- |
| In-house | Grok, Composer | "Generous" usage, no published figure |
| Third-party | Claude, GPT | API price, hard number, runs out |

That isn't a billing decision. That's the entire commercial policy: the competition costs you money and eventually runs dry. Antigravity applies the same pattern in a different currency: it serves Claude through Google credits whose conversion to tokens is undocumented.

## The day neutrality stopped paying

Until August, Cursor had every reason to want Claude and GPT performing well. It had no frontier model of its own. Its product was worth whatever someone else's model was worth.

With Grok built inside the same group, that incentive flips.

No bad faith required. A margin test deciding the default is enough.

## The invisible lever

In July 2026, Cursor Router replaced Auto mode. The economy tier keeps its flat rate but stopped being unlimited. The higher tiers bill at the price of whichever model actually runs. And the vendor picks that model.

> Handing the choice to whoever charges differently depending on the choice is the most powerful commercial lever there is. It's also the least visible.

A harness that resells tokens is useless as a model benchmark. What you're observing isn't the model. It's the model plus the decisions of an intermediary you can't audit, one with interests shaped by its own commercial agreements.

## Five things that aren't on the pricing page

1. **Your subscription doesn't come with you.** You can't use your Claude Pro or Max plan inside Cursor. Consumer subscriptions stay tied to the model vendor's own app.
2. **A per-token surcharge** on third-party models in team plans. It applies even when you bring your own key. In-house models are exempt.
3. **A surcharge for regional data residency.**
4. **Migration from fixed seats to per-run billing**, as already happened with Bugbot.
5. **BYOK switches off zero data retention.** Bring your own key and your data falls under the model provider's policy instead. You bought the environment for privacy and lose it precisely by using it that way.

Point 1 has an economic consequence, not just a technical one: the consumer subscription is the cheapest frontier token on the market, and no reseller can match it. A vendor can subsidize its own channel. A middleman can't.

The legitimate alternative is boring, and it costs you something: install the Claude Code extension inside Cursor, which is a VS Code fork anyway, and authenticate with your own account. Cursor becomes your editor. It stops being your harness.

## Origin closes the chain

Origin is Cursor-hosted Git: repos, pull requests, and sync with GitHub without leaving the editor. Repos live at cursor.com/codebase. Early beta since August 17 on Pro, Teams and Enterprise.

Cursor bought Graphite in December 2025, a company built around stacked PRs and merge queues. Origin is the last piece: write, store, review, and merge in the same place.

> The bottleneck isn't writing code anymore. It's reviewing it.

GitHub wasn't designed for this volume or this model of authorship. The timing wasn't accidental either: GitHub went down for six hours and forty-two minutes on launch day.

Almost every closed ecosystem leaves the repository alone. Google and Anthropic don't touch where your project lives. SpaceXAI wants it inside, because a repo holds far more than code: org rulesets, reusable workflows, the identity App, the quality gate, the board that acts as your source of truth.

## Watch, don't act

Swapping GitHub for Origin wouldn't be switching providers, or swapping one piece of my E2E flow. It's moving to a vendor with ambitions to own the whole ecosystem, one that also sells you the harness and the model.

I've used Cursor before, and I'm tempted to give it another shot. With this much noise out there, re-evaluating is tempting on its own. For now I'd rather watch without acting, and wait until Origin shows up in tools that adopt it on merit, not through a commercial agreement.

---

### Sources

- [CNBC — SpaceX announces the Anysphere deal (June 16, 2026)](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html)
- [Seeking Alpha — close confirmed via SEC Form 8-K](https://seekingalpha.com/news/4633335-spacex-completes-60b-acquisition-of-cursor-as-musk-led-firm-tries-to-gain-edge-in-ai-coding)
- [Cryptopolitan — share conversion and the SpaceXAI division](https://www.cryptopolitan.com/spacex-cursor-maker-anysphere-60-billion/)
- [Slashdot / VentureBeat — Origin rollout and the 6h42m GitHub outage](https://developers.slashdot.org/story/26/08/18/2211249/cursor-launches-origin-code-hosting-platform-as-github-alternative)
- [DevOps.com — outage error rates and the Graphite acquisition](https://devops.com/cursor-launches-origin-code-hosting-platform-as-github-rival/)
- [InfoQ — what shipped in Origin's early beta](https://www.infoq.com/news/2026/08/cursor-origin-alternative-github/)
