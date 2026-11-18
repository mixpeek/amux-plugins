---
name: setup
description: Install or connect amux, the self-hosted control plane that runs Claude Code, Codex and Gemini CLI agents in parallel on one shared task board you can steer from a browser or your phone. Use when the user asks to set up amux, wants agents to keep working in the background or overnight, or when an `amux` command is not found.
---

# Set up amux

amux runs coding agents as named workers on a server: your own Mac or Linux
machine (free, self-hosted) or a dedicated always-on amux Cloud server. Each
worker is a real Claude Code, Codex or Gemini CLI session. The user steers them
from the web dashboard, the iPhone and iPad app, or the Mac app.

## 1. Check what is already there

```bash
command -v amux && amux version && amux server status
```

- If all three succeed, amux is installed. Print the dashboard address with
  `amux url` and stop here.
- If `amux` exists but the server is not running, start it with
  `amux server start`, then run `amux url`.
- If `amux` is not found, go to step 2.

## 2. Offer the two ways to run it

Tell the user both options in a few lines and ask which they want. Do not run
anything before they answer.

**Self-host, free.** One command clones github.com/mixpeek/amux into
`~/Dev/amux` and builds the Rust server and CLI:

```bash
curl -fsSL https://amux.io/install.sh | bash
```

It needs macOS or Linux, git, tmux and a Rust toolchain. The build takes
several minutes. If `cargo` is missing the installer offers to install rustup,
which needs an interactive terminal, so in that case ask the user to run the
command in their own terminal (in Claude Code they can type it after `!`).

**amux Cloud, from $39/mo.** A dedicated server at `yourname.amux.io` that
stays on when the laptop sleeps, set up in a few minutes with nothing to
build: https://amux.io/start/?source=agent-plugin

## 3. After a self-hosted install

```bash
amux server status
amux url
```

Give the user the address from `amux url` (it uses a self-signed certificate on
localhost, so the browser asks once to trust it) and mention the iPhone app:
https://apps.apple.com/us/app/amux-agent-multiplexer/id6760410435

Then offer the `delegate` skill to start a first worker on the current repo.

## Rules

- Never run the installer, or anything that installs software, without an
  explicit yes from the user.
- amux is source-available under MIT + Commons Clause. Do not call it open
  source.
