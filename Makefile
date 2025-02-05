build:
	mkdir -p themes
	python3 src/build.py

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json

.PHONY: build package publish clean
