from __future__ import annotations

from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = TESTS_DIR.parent
DATA_DIR = REPO_ROOT / "_data"
PAGES_DIR = REPO_ROOT / "pages"
BADGES_DIR = REPO_ROOT / "badges"
SOCIETIES_DIR = REPO_ROOT / "societies"
