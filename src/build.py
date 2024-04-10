#!/usr/bin/env python3

import json
import importlib
import os
import yaml

colors = {
    "bg_1": "#ffffee",
    "bg_2": "#f2f2e2",
    "bg_3": "#eeeedd",
    "black_1": "#000000",
    "black_2": "#333333",
    "gray_1": "#888888",
    "gray_2": "#cccccc",
    "gray_3": "#dddddd",
    "blue_1": "#5577bb",
    "blue_2": "#99bbcc",
    "cyan_1": "#559999",
    "cyan_2": "#99cccc",
    "cyan_3": "#aaeeee",
    "cyan_4": "#f0ffff",
    "green_1": "#559955",
    "green_2": "#99be99",
    "green_3": "#88cc88",
    "green_4": "#eaffea",
    "magenta_1": "#996699",
    "magenta_2": "#bb99bb",
    "orange_1": "#d08770",
    "purple_1": "#8888cc",
    "purple_2": "#bbbbff",
    "red_1": "#bb5d5d",
    "red_2": "#dd8888",
    "white_2": "#ffffff",
    "brown_1": "#99774c",
    "yellow_1": "#998855",
    "yellow_2": "#eeeeaa",
    "border": "#00000088",
    "invisible": "#00000000",
}

acme_theme = {
    **colors,
    "fg": colors["black_1"],
    "dim": colors["black_1"] + "88",
    "fade": colors["black_1"] + "66",
    "faint": colors["black_1"] + "44",
    "ui_bg": colors["cyan_4"],
    "ui_hl": colors["cyan_3"],
    "selection_bg": colors["yellow_2"],
    "button_bg": colors["purple_1"],
    "button_fg": colors["white_2"],
}


def generate_theme(template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_file, "r") as f:
        theme_template = yaml.safe_load(f)

    # Format the strings in the YAML dictionary
    def recursive_format(value):
        if isinstance(value, str):
            return value.format(**acme_theme)
        elif isinstance(value, list):
            return [recursive_format(item) for item in value]
        elif isinstance(value, dict):
            return {key: recursive_format(val) for key, val in value.items()}
        else:
            return value

    theme_output = recursive_format(theme_template)

    with open(output_file, "w") as f:
        json.dump(theme_output, f, indent=2)


def main():
    output_file_name = "acme-color-theme.json"
    output_file_path = os.path.join("themes", output_file_name)
    generate_theme("src/template.yml", output_file_path)


if __name__ == "__main__":
    main()
