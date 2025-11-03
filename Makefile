# This is used as shortcuts to run commands

# Playwright stores browser binaries inside the virtualenv.
ROOT := $(PWD)
export PLAYWRIGHT_BROWSERS_PATH := $(ROOT)/.venv/ms-playwright

# 'make serve'
serve: clean
	bundle exec jekyll serve --livereload --incremental --force-polling

# 'make build' etc..
build: clean
	bundle exec jekyll build

.PHONY: venv
venv: .venv/.deps-installed

.venv:
	python3 -m venv .venv

.venv/.deps-installed: .venv requirements.txt
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	touch .venv/.deps-installed

.venv/.browsers-installed: .venv/.deps-installed
	.venv/bin/playwright install chromium firefox webkit
	touch .venv/.browsers-installed

test: .venv/.browsers-installed
	@BASE=$${BASE_URL:-http://localhost:4000/}; \
	if ! curl --silent --head --fail --max-time 5 "$${BASE}" >/dev/null 2>&1; then \
		echo "Error: BASE_URL '$${BASE}' is not reachable. Start the site (e.g. 'make serve') or set BASE_URL." >&2; \
		exit 1; \
	fi
	.venv/bin/pytest --base-url=$${BASE_URL:-http://localhost:4000/}

clean:
	rm -rf _site

# Send an empty commit to force the github action to rebuild the site.
emptyCommit:
	git pull
	git commit --allow-empty -m "Empty commit (Force rebuild)"
	git push

run: clean
	bundle exec jekyll serve --livereload --incremental
