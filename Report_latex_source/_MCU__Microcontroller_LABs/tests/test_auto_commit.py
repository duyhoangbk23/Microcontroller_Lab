import pytest
from scripts.auto_commit import build_commit_message


def test_build_simple():
    staged = ["src/main.c", "src/lib/util.c"]
    unstaged = []
    msg = build_commit_message(staged, unstaged)
    assert msg.startswith("src(") or msg.startswith("chore("), "message should include category"


def test_build_docs():
    staged = ["README.md", "docs/guide.tex"]
    msg = build_commit_message(staged, [])
    assert msg.startswith("docs("), msg
