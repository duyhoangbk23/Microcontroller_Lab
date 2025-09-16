# auto_commit tool

This is a small conservative CLI that suggests git commands and a commit message based on changed files.

Usage:

```
python -m scripts.auto_commit
python -m scripts.auto_commit --apply   # will run the commands (use with caution)
```

It intentionally doesn't push or modify history unless `--apply` is used.
