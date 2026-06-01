# .claude/

Claude Code project-level configuration. Files here are picked up
automatically by Claude Code when it runs in this project.

## Files

- `settings.json` — team-shared project settings (permissions, hooks,
  default model, env vars). **Committed** to version control. Keep
  this conservative: permissions granted here apply to anyone using
  the project.
- `settings.local.json` — **gitignored**. Personal overrides for the
  settings above. Copy `settings.local.json.example` to get started.
- `settings.local.json.example` — template showing the shape of a
  local-overrides file.

## Precedence

From highest to lowest:
1. CLI flags passed to `claude`
2. `settings.local.json` (personal)
3. `settings.json` (project, committed)
4. `~/.claude/settings.json` (your global user settings)

## References

- [Claude Code settings reference](https://code.claude.com/docs/en/settings.md)
- [Explore the `.claude/` directory](https://code.claude.com/docs/en/claude-directory.md)
- [Hooks reference](https://code.claude.com/docs/en/hooks.md)
