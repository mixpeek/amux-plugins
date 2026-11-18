---
name: status
description: Report what the user's amux workers and task board are doing right now, who is waiting on the user, and what is stuck. Use when the user asks how their agents are doing, what is running, or what needs them.
---

# Check on amux workers

## 1. Read the state

Ask the amux server for every running worker's state (it uses a self-signed
certificate on localhost, hence `-k`):

```bash
curl -sk --max-time 20 "$(amux url)/api/sessions" | python3 -c '
import json, sys
for s in json.load(sys.stdin):
    if s.get("status"):
        print(s["name"].ljust(24), s["status"])'
amux board ls
```

`status` is `waiting` (it needs the user), `active` (working) or `idle`;
workers with no status are not running. If the request fails, `amux ls` lists
the same workers, but it reads every worker's terminal and can take minutes on
a large fleet. `amux board ls` lists the open cards on the
shared task board.

For any worker that looks stuck, waiting or failed, read more of its output:

```bash
amux peek <name> 80
```

If `amux` is not found or the server is not running, use the `setup` skill.

## 2. Report

Keep it short and in this order:

1. Workers waiting on the user (a question, a permission prompt, a login), with
   the exact thing each one needs.
2. Workers that look stuck or failed, with the last relevant line.
3. Workers working normally, one line each.
4. Open board cards nobody has claimed.

Offer to answer a waiting worker for the user with
`amux send <name> --stdin`, and only send after the user says what to send.
