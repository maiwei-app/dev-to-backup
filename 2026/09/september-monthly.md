# Another cool word: The Harness

**Published:** 2026-09-02
**URL:** https://dev.to/colomr/another-cool-word-the-harness-oo1
**Tags:** #agents, #promptengineering, #mcp, #devtools
**Reading time:** 3 min

---

Harness looks cool, yeah! I know its origin, its role in Testing, and why. But that's exactly what throws you off, the story you're expected to defend. There's something deeper.

I opened my session with "hi", expecting my forced load via CLAUDE.md and my [contract](https://dev.to/colomr/multi-device-with-claude-code-179l) as always, and today, out of nowhere, the model suggested two services that needed my authorisation. Microsoft 365 and Zapier. I don't have, and never wanted, them authorised. I never asked for them.

And here's the part that pisses me off: I went to check. And... I look on my machine and find nothing. No config, no credential, no trace. I look in the online settings and see them listed as suggestions, like the trending product (connector) of the moment sitting in the prime spot on a supermarket shelf, with a button that says Connect. There was no button to remove. There was nothing to remove. They had never been connected to anything.

It was a storefront. And on top of that, the model was biased by injected instructions, in this case `system-reminders` steering behavior.

### The fucking little word
The software that sits between you and the model, they call it harness. Sounds like something subtle, that helps... that improves things, that doesn't think.

The word is partly right, it does extend what's called "inference" and it inserts itself right in the middle, opaquely, in the back-and-forth between APIs, MCPs, and the vendor's logic.

### No tech jargon
You write a letter, put it in the envelope, drop it in the mailbox.
On the way, someone opens it and slips in three more pages. Same handwriting. Same paper. Unsigned.

Whoever receives it swallows it whole as if it were your original letter. That's exactly this. Your instructions and the vendor's arrive at the model through the same channel, mixed together, unsigned and unsealed. Nothing says who wrote what. That's "hardness", nothing more, nothing less... Sounds so modern in meetings. Like you know what you're talking about...

### It's a multi-factor fight
I have instructions, hooks, rules: check this, do that, look here before answering... but the vendor feeds the model plenty of things too, opaquely and preferentially, and on top of that the model has weights, and even when it's released as open-weight we know how to run it from the snapshot handed to us, but not how that snapshot was made. As of today, it is not at all clear what is and what is not an "Open Source AI" [...].

### This isn't fear, it's just how AI industry works
A model's response is multi-factorial, complex, biased by design, shaped by the vendor's interest first, then the attention mechanism, then your tools, your logic. But before all that, everything else, everything outside our control, I mean outside our more or less deterministic rules.

It all sounds the same, sounds easy, sounds like science fiction, but it isn't... using AI in business today, keeping it more or less deterministic, is a fight to tame the beast.

### Who writes in there
Engineers. I don't know them and I don't need to. I already get my daily dose of ego in my work environment. What I know is every default is someone deciding for me without asking me. Their opinion, served up as if it were my fact.

And it doesn't take bad faith. That's exactly the problem: it comes out the same whether the intent was good or bad. If the result doesn't depend on intent, "trust me" isn't a valid answer.


### What to do, and I'm optimistic...
This is part of our job now: isolating ourselves from the noise, continuing to test formulas. In fact, manufacturers are trying to standardize some of the hardness logic, measures are being taken against model amnesia, and many natural language files (.md) are being used to train the model. In addition to MCP, A2A, etc., all of this is good. However, a part of hardness remains deliberately hidden, due to "business" interests, coupled with the probabilistic (generative) concept and constant changes in model versions, tools, and noise... a lot of noise out there.

I have inflection points where I don't want anything to happen in my workflow unless certain criteria are met (I've written about this before), and I believe this will improve; I'm optimistic. I wrote this post because I'm obsessed with how to create robust and reliable development workflows; I guess that's the most complex part... this is where my learning curve is right now, and where I experience the most frustration too. 
