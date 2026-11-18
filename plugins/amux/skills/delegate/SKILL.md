---
name: delegate
description: Hand a task to a background amux worker (Claude Code, Codex or Gemini CLI) that keeps running after this session ends, or file it as a card on the amux task board. Use when the user wants work done in parallel, in the background, overnight, or by a different agent.
---

# Delegate work to an amux worker

A worker is a named agent session that amux runs and supervises. It keeps
working after this conversation ends, and the user can watch and steer it from
the amux dashboard or the iPhone app.

## 1. Make sure amux is running

```bash
command -v amux && amux server status
```

If either fails, use the `setup` skill first.

## 2. Pick or create the worker

To reuse a worker the user names, check that it exists (exit 0 means it does)
and skip to step 3:

```bash
amux info <name>
```

To see every running worker and whether it is `active`, `idle` or `waiting`:

```bash
curl -sk --max-time 20 "$(amux url)/api/sessions" | python3 -c '
import json, sys
for s in json.load(sys.stdin):
    if s.get("status"):
        print(s["name"].ljust(24), s["status"])'
```

To create one, choose:

- a short name in lowercase with dashes, such as `api-tests`;
- the absolute path of the repository it should work in (usually the current
  directory, `pwd`);
- the agent: `claude` (default), `codex` or `gemini`, which must already be
  installed and signed in on this machine.

```bash
amux register <name> --dir <absolute-path> --provider <claude|codex|gemini>
amux start <name> --detach
```

Always pass `--detach`; without it `amux start` attaches to the worker's
terminal and blocks this shell. Do not add permission-skipping flags such as
`--yolo` unless the user asks for them.

## 3. Give it the task

Send the task as a message. Use `--stdin` with a quoted heredoc so the shell
does not expand backticks or `$(...)` inside it:

```bash
amux send <name> --stdin <<'EOF'
<the task, with the files, the goal and how to know it is done>
EOF
```

Write the task so it stands on its own: the worker cannot see this
conversation.

To queue work for later instead of starting it now, put it on the shared
board, where any worker can claim it:

```bash
amux board add "<short title>" --desc-stdin <<'EOF'
<what done looks like>
EOF
```

## 4. Tell the user where to watch

Report the worker's name and these ways to follow it:

- `amux peek <name> 60` prints its last 60 lines;
- the dashboard at the address `amux url` prints;
- the amux iPhone app, connected to the same server.
