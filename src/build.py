#!/usr/bin/env python3

import json
import importlib
import os
import yaml

colors = {
    "black_1": "#000000",
    "black_2": "#333333",
    "gray_1": "#888888",
    "gray_2": "#cccccc",
    "gray_3": "#e2e2e2",
    "gray_4": "#eeeeee",
    "gray_5": "#f6f6f6",
    "blue_1": "#5580bf",
    # "blue_2": "#a0c0dd",
    # "blue_3": "#c8e0ee",
    # "blue_4": "#f0f8ff",
    "blue_2": "#a4c4e0",
    "blue_3": "#cce4f2",
    "blue_4": "#f4fbff",
    "cyan_1": "#66aaaa",
    "cyan_2": "#99cccc",
    "cyan_3": "#aaeeee",
    "cyan_4": "#eeffff",
    # "green_1": "#558844",
    # "green_2": "#99b888",
    "green_1": "#669977",
    "green_2": "#a4ccb0",
    "magenta_1": "#996688",
    "magenta_2": "#cc99aa",
    "orange_1": "#d08770",
    "orange_2": "#f0ccb0",
    "purple_1": "#8888cc",
    "purple_2": "#bbbbff",
    "red_1": "#cc5d5d",
    "red_2": "#dd8888",
    "white": "#ffffff",
    "yellow_1": "#998866",
    "yellow_2": "#eeeeaa",
    "border": "#888888",
    "invisible": "#00000000",
}

acme = {
    **colors,
    "theme_name": "Acme",
    "theme_type": "light",
    "bg_1": "#ffffee",
    "bg_2": "#f2f2e2",
    "bg_3": "#eeeedd",
    "fg": colors["black_1"],
    "bold": colors["black_1"],
    "dim": colors["black_1"] + "88",
    "fade": colors["black_1"] + "66",
    "faint": colors["black_1"] + "44",
    "selection_bg": colors["yellow_2"],
    "match_bg": colors["purple_2"],
    "button_bg": colors["purple_1"],
    "button_fg": colors["white"],
    "ui_bg": colors["cyan_4"],
    "ui_hl": colors["cyan_3"],
    "hover_bg": colors["white"],
    "hover_hl": colors["cyan_3"],
    "blank_bg": colors["white"],
}
acme["string"] = acme["dim"]

acme_white = {
    **acme,
    "theme_name": "Acme White",
    "bg_1": colors["white"],
    "bg_2": colors["gray_5"],
    "bg_3": colors["gray_4"],
    "selection_bg": colors["gray_3"],
    "match_bg": colors["orange_2"],
    "ui_bg": colors["blue_4"],
    "ui_hl": colors["blue_3"],
    "hover_bg": colors["gray_5"],
    "hover_hl": colors["gray_3"],
    "string": "#72899c",
}

colors_dark = {
    "theme_type": "dark",
    "bg_1": "#2e3440",
    "bg_2": "#333947",
    "bg_3": "#434c5e",
    "fg": "#d8dee9",
    "white": "#eceff4",
    "red_1": "#bf616a",
    "orange_1": "#d08770",
    "green_1": "#a3be8c",
    "yellow_1": "#ebcb8b",
    "blue_1": "#81a1c1",
    "magenta_1": "#b48ead",
    "cyan_1": "#88c0d0",
    "invisible": "#00000000",
}

acme_dark = {
    **colors_dark,
    "theme_name": "Acme Dark",
    "bold": colors_dark["white"],
    "black_1": colors_dark["bg_1"],
    "dim": colors_dark["fg"] + "88",
    "fade": colors_dark["fg"] + "66",
    "faint": colors_dark["fg"] + "44",
    "selection_bg": colors_dark["bg_3"],
    "match_bg": colors_dark["magenta_1"] + "bb",
    "button_bg": colors_dark["cyan_1"],
    "button_fg": colors_dark["bg_1"],
    "ui_bg": colors_dark["bg_2"],
    "ui_hl": colors_dark["bg_3"],
    "hover_bg": colors_dark["bg_2"],
    "hover_hl": colors_dark["bg_3"],
    "blank_bg": colors_dark["bg_1"],
    "border": colors_dark["bg_3"],
    "string": colors_dark["blue_1"],
}
for color in ["red", "green", "yellow", "blue", "magenta", "cyan", "orange"]:
    acme_dark[f"{color}_2"] = acme_dark[f"{color}_1"]

def generate_theme(theme_dict, template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_file, "r") as f:
        theme_template = yaml.safe_load(f)

    # Format the strings in the YAML dictionary
    def recursive_format(value):
        if isinstance(value, str):
            return value.format(**theme_dict)
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
    themes = {"acme": acme, "acme_white": acme_white, "acme_dark": acme_dark}
    for theme_name, theme_dict in themes.items():
        output_file_name = f"{theme_name.replace('_', '-')}-color-theme.json"
        output_file_path = os.path.join('themes', output_file_name)
        generate_theme(theme_dict, 'src/template.yml', output_file_path)


if __name__ == "__main__":
    main()
