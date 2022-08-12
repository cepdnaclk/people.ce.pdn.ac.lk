# This is used as shortcuts to run commands

# 'make serve'
serve: clean
	bundle exec jekyll serve --livereload --incremental --force-polling

# 'make build' etc..
build: clean
	bundle exec jekyll build

test:
	cd tests; python3 -m unittest discover

clean:
	rm -rf _site

# Send an empty commit to force the github action to rebuild the site.
emptyCommit:
	git pull
	git commit --allow-empty -m "Empty commit (Force rebuild)"
	git push