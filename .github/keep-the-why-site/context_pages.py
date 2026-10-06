"""MkDocs hook: publish the repository's context/ on the Keep the Why site.

Every topic file in context/ becomes the page /context/<name>/, generated at
build time from the file itself - no copy under pages/ to keep in sync.
Relative links between topic files resolve to the sibling pages, as they do
in the repository.
"""

from __future__ import annotations

from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTEXT_DIR = REPO_ROOT / "context"

# Directory scaffolding, not topic files: the on-disk README and the agent guards.
NOT_PAGES = {"README.md", "AGENTS.md", "CLAUDE.md"}


def on_config(config: MkDocsConfig) -> MkDocsConfig:
    config.watch.append(str(CONTEXT_DIR))
    return config


def on_files(files: Files, config: MkDocsConfig) -> Files:
    for path in sorted(CONTEXT_DIR.glob("*.md")):
        if path.name in NOT_PAGES:
            continue
        files.append(
            File.generated(config, f"context/{path.name}", content=path.read_text(encoding="utf-8"))
        )
    return files
