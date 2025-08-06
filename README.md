# Acme theme

A set of VS Code themes inspired by the [Acme editor](https://en.wikipedia.org/wiki/Acme_%28text_editor%29). 

Two big differences between the main theme and the original Acme editor's color scheme:

1. Comments are a faded foreground color.
2. Some other editor and UI colors are slightly muted compared to the originals, which looks better in VS Code on modern displays IMHO.
3. A white-and-blue variant of the theme is included.

## Screenshot

![screenshot](assets/screenshot.png)

## Recommended Settings

```
{
    "explorer.decorations.colors": false,
    "workbench.editor.decorations.colors": false,
    "search.decorations.colors": false,
}
```

## Build

Requires vsce and Python ≥ 3.11.
- Build themes: `make build`
- Build extension: `make package`