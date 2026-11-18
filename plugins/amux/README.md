# amux

Hand a task to a background coding agent that keeps working after your
session ends, and check on your agents, from inside Claude Code.

[amux](https://amux.io) is a self-hosted control plane for running an AI
engineering team from one board or your phone. It runs Claude Code, Codex and
Gemini CLI agents in parallel as named workers, with a shared task board, a
scheduler and an iPhone app. This plugin connects your session to it.

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

Every skill runs the `amux` command line and reads the amux server on your own
machine. The plugin sends nothing to any other service. It asks before it
installs software or starts a worker.

## Requirements

macOS or Linux, and amux itself (`/amux:setup` walks you through it). A Codex or
Gemini CLI worker needs that CLI installed and signed in.

## License

MIT + Commons Clause, the same as amux. Source-available: free to use and
modify, including at work; you may not sell it.
