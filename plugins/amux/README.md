# amux

Hand a task to a background coding agent that keeps working after your
session ends, and check on your agents, from inside Claude Code.

[amux](https://amux.io) is a self-hosted control plane for running an AI
engineering team from one board or your phone. It runs Claude Code, Codex and
Gemini CLI agents in parallel as named workers, with a shared task board, a
scheduler and an iPhone app. This plugin connects your session to it.

## Install

```text
/plugin install amux --marketplace mixpeek/amux-plugins
```

## Skills

- `/amux:setup` checks whether amux is installed, offers the free self-hosted
  install or amux Cloud, and prints the dashboard address.
- `/amux:delegate` starts a background Claude Code, Codex or Gemini CLI worker
  on your repository and sends it the task, or files the task on the amux
  board for any worker to claim.
- `/amux:status` reports which workers are waiting on you, which look stuck,
  and which board cards nobody has claimed.

Claude also uses these on its own when you ask for work to run in the
background, in parallel or overnight.

## How it works

Every skill runs the `amux` command line against the amux server on your own
machine; Mixpeek receives nothing. Where data goes:

- `status` reads your workers' state and your board cards, which can contain
  names or email addresses you put there. It stores nothing.
- `delegate` sends the task text to your local amux server, which types it into
  the worker you chose. That worker is Claude Code, Codex or Gemini CLI running
  under your own account, so the task reaches that agent's model provider
  (Anthropic, OpenAI or Google) the same way it would if you typed it there.
- `setup` downloads the amux installer from amux.io and github.com, and only
  after you say yes.

The plugin asks before it installs software or starts a worker.

## Requirements

macOS or Linux, and amux itself (`/amux:setup` walks you through it). A Codex or
Gemini CLI worker needs that CLI installed and signed in.

## License

MIT + Commons Clause, the same as amux. Source-available: free to use and
modify, including at work; you may not sell it.
