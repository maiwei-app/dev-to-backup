# Your AI Coding Agent Is You... And That's the Problem

**Published:** 2026-08-14
**URL:** https://dev.to/colomr/your-ai-coding-agent-is-you-and-thats-the-problem-5ddc
**Tags:** #security, #github, #devops, #agents
**Reading time:** 2 min

---

Your rulesets are in place. Branch protection, required reviews, no force-push to `main`. Everything by the book.

Then your coding agent pushes straight to `main`. No error. No warning. Clean push.
Your first instinct: the agent bypassed the ruleset. It didn't. The ruleset never applied.


## Identity Inheritance, Not a Bypass
An LLM running inside your VS Code session doesn't authenticate as itself. It uses your SSH keys, your `git config`, your `gh` session. If you're an org admin, the agent operates as an org admin.

GitHub rulesets exempt admins by default. The agent didn't break anything. It acted under your identity, and your identity had a free pass.

The governance layer was never breached. It was never reached.

## Ink vs Cement
A `RULES.md` file telling the agent "never push to main" is probabilistic. The model reads it, interprets it, mostly follows it. Until it doesn't.

A system-level restriction that blocks the push before it happens is cement. No interpretation. No exceptions.

The fix isn't telling the agent to behave. The fix is removing its ability to misbehave.

## An Isolated System User
The agent now runs under `maibot`, a separate Linux user with its own home directory, its own credentials, and zero admin privileges anywhere, just `writer`.

Authentication goes through a GitHub App with three permissions:

- `contents: write`: clone and push to branches
- `pull_requests: write`:open PRs
- `metadata: read`

That's it. No `admin`. No `maintain`. The org-wide ruleset applies in full. `maibot` can't push to `main`, can't approve PRs, can't delete protected branches.

## Two Sessions, One Machine
Both run via VS Code Remote-SSH on the same WSL2 instance:

- `wsl-colomr` → the developer. Admin keys, commit signing, full access.
- `wsl-maibot` → the agent. GitHub App token, scoped permissions, one-hour expiry.


![Logged in to github.com account maibot-app[bot]](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/4oe1idzkcv9q37efvsvj.png)



A shell script generates a JWT from the App's private key, exchanges it for an installation token, and configures `gh` and `git` credentials. The token lives for one hour. Just enough for my "atomic" sessions (_it requires another post, sooner than later_). 

## Why This Matters Beyond My Setup
Every team running AI coding agents inside developer sessions has this problem. The agent doesn't need to be malicious. It doesn't need to hallucinate. It just needs to inherit the wrong identity and make a mistake.

If your developers are admins and your agents share their sessions, your rulesets are decoration.

## What Comes Next
`maibot` isn't just a hotfix. It's the foundation for an agentic layer where every agent operates under `least privilege` by design: isolated identity, scoped credentials, system-enforced boundaries. No agent gets more access than it needs. No exception travels by inheritance.

Cement first. Autonomy second.

