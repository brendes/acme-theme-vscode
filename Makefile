CONFIGS = $(wildcard src/themes/*.conf)
THEMES = $(patsubst src/themes/%.conf,themes/%-color-theme.json,$(CONFIGS))

.PHONY: build

build:
	mkdir -p themes
	for conf in src/themes/*.conf; do \
		name=$$(basename $$conf .conf); \
		awk -f src/build.awk -v template=src/template.json \
			src/colors.conf src/base.conf $$conf src/template.json \
			> themes/$$name-color-theme.json; \
	done

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json

watch:
	find src/* | entr -c make build

.PHONY: build package publish clean watch
