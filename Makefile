CONFIGS = $(wildcard src/themes/*.conf)
THEMES = $(patsubst src/themes/%.conf,themes/%-color-theme.json,$(CONFIGS))

build: $(THEMES)

themes/%-color-theme.json: src/themes/%.conf src/colors.conf src/base.conf src/template.json src/build.awk
	@mkdir -p themes
	awk -f src/build.awk -v template=src/template.json \
		src/colors.conf src/base.conf $< src/template.json > $@

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json

watch:
	find src/* | entr -c make build

.PHONY: build package publish clean watch
