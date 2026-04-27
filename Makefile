build:
	mkdir -p themes
	for conf in src/themes/*.conf; do \
		name=$$(basename $$conf .conf); \
		awk -f src/build.awk -v template=src/lib/template.json \
			src/lib/colors.conf src/lib/base.conf $$conf src/lib/template.json \
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
