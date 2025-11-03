from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterator

import pytest
from playwright.sync_api import Page, expect

from tests.pages import HomePage

DEFAULT_BASE_URL = "http://localhost:4000/"


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str:
    cli_url = getattr(pytestconfig.option, "base_url", None)
    url = cli_url or os.getenv("SITE_BASE_URL", DEFAULT_BASE_URL)
    return url if url.endswith("/") else f"{url}/"


@pytest.fixture(scope="session")
def artifacts_dir(pytestconfig: pytest.Config) -> Path:
    root = Path(pytestconfig.invocation_params.dir)
    path = root / "test-results"
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture
def home_page(page: Page, base_url: str) -> HomePage:
    home = HomePage(page=page, base_url=base_url)
    response = home.goto("")
    if response is not None:
        assert response.ok, (
            f"Navigation to {response.url} failed with {response.status}"
        )
    expect(page).to_have_url(base_url)
    return home


def _sanitize_nodeid(nodeid: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", nodeid)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo
) -> Iterator[None]:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def browser_context_args(
    browser_context_args: dict,
    artifacts_dir: Path,
) -> dict:
    video_dir = artifacts_dir / "video-tmp"
    video_dir.mkdir(parents=True, exist_ok=True)
    return {
        **browser_context_args,
        "record_video_dir": video_dir.as_posix(),
    }


@pytest.fixture(autouse=True)
def capture_failure_artifacts(
    request: pytest.FixtureRequest,
    artifacts_dir: Path,
    browser_name: str,
) -> Iterator[None]:
    yield

    page: Page | None = request.node.funcargs.get("page")
    if page is None:
        return

    rep = getattr(request.node, "rep_call", None)
    if not rep:
        return

    file_stem = _sanitize_nodeid(request.node.nodeid)

    if rep.passed:
        if page.video:
            try:
                video_path = Path(page.video.path())
                if video_path.exists():
                    video_path.unlink()
            except Exception:
                pass
        return

    screenshot_path = artifacts_dir / browser_name / f"{file_stem}.png"
    screenshot_path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=screenshot_path.as_posix(), full_page=True)

    if page.video:
        try:
            video_path = page.video.path()
        except Exception:
            return
        target = artifacts_dir / browser_name / f"{file_stem}.webm"
        target.parent.mkdir(parents=True, exist_ok=True)
        Path(video_path).replace(target)
