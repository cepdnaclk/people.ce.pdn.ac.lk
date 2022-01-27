# This is used as shortcuts to run commands

# 'make serve'
serve: clean
	bundle exec jekyll serve --livereload --incremental --force-polling

# 'make build' etc..
build: clean
	bundle exec jekyll build

clean:
	rm -rf _site