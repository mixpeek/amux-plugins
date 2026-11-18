# amux plugins for Claude Code, Codex and Gemini CLI

Hand a task to a background agent that keeps working after your session ends,
check on your agents, and set up [amux](https://amux.io) from inside the coding
agent you already use.

amux is a self-hosted control plane for running an AI engineering team from one
board or your phone. It runs Claude Code, Codex and Gemini CLI agents in
parallel as named workers, with a shared task board, a scheduler, and an iPhone
app. Self-host it free, or use [amux Cloud](https://amux.io/start/?source=amux-plugins-readme)
for a dedicated server that stays on when your laptop sleeps.

## Install

**Claude Code**

```text
/plugin marketplace add mixpeek/amux-plugins
/plugin install amux@amux
```

**Codex**

```bash
codex plugin marketplace add mixpeek/amux-plugins
codex plugin add amux@amux
```

**Gemini CLI**

```bash
gemini extensions install https://github.com/mixpeek/amux-plugins
```

## What you get

| Skill | Claude Code | Codex | Gemini CLI | What it does |
|---|---|---|---|---|
| setup | `/amux:setup` | `$amux:setup` | `/amux:setup` | Checks for amux, offers the free self-hosted install or amux Cloud, prints the dashboard address |
| delegate | `/amux:delegate` | `$amux:delegate` | `/amux:delegate` | Starts a background Claude Code, Codex or Gemini CLI worker on your repo and sends it the task, or files it on the amux board |
| status | `/amux:status` | `$amux:status` | `/amux:status` | Lists which workers are waiting on you, which look stuck, and what is on the board |

The agent can also pick these up on its own when you ask for work "in the
background", "overnight" or "in parallel".

Everything goes through the `amux` command line on your machine. The plugin
sends nothing anywhere else, and it asks before it installs anything or starts
a worker.

## Requirements

- macOS or Linux.
- amux itself: `curl -fsSL https://amux.io/install.sh | bash` (needs git, tmux
  and a Rust toolchain), or `/amux:setup` walks you through it.
- For a Codex or Gemini CLI worker, that CLI installed and signed in.

## Layout

```text
.claude-plugin/marketplace.json   Claude Code marketplace
.agents/plugins/marketplace.json  Codex marketplace
gemini-extension.json, GEMINI.md  Gemini CLI extension
commands/amux/*.toml              Gemini commands, generated from the skills
plugins/amux/                     the plugin: skills/ plus Claude and Codex manifests
```

The three skills in `plugins/amux/skills/` are the only source. After editing
one, run `python3 scripts/sync-gemini.py` to regenerate the Gemini commands;
CI fails when they are out of date.

## License

MIT + Commons Clause, the same as [amux](https://github.com/mixpeek/amux).
Source-available: free to use and modify, including at work; you may not sell
it.
