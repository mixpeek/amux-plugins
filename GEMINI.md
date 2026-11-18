# amux

amux runs coding agents as named background workers on a server: the user's
own Mac or Linux machine, or a dedicated always-on amux Cloud server. Workers
keep running after this session ends, share one task board, and the user
steers them from a browser or the amux iPhone app.

This extension adds three commands:

- `/amux:setup` installs or connects amux. Use it when `amux` is not found.
  In the other commands, "the `setup` skill" means this command.
- `/amux:delegate` hands a task to a background Claude Code, Codex or Gemini CLI
  worker, or files it on the amux board.
- `/amux:status` reports which workers need the user, which are stuck and what
  is on the board.

When the user asks for work to run in the background, in parallel, overnight
or by another agent, suggest `/amux:delegate`. Never install software or start
a worker without the user's yes.
