#!/usr/bin/env python3

import json
import os

colors = {
    "paleyellow_1": "#ffffee",
    "paleyellow_2": "#f2f2e2",
    "paleyellow_3": "#eeeede",
    "paleyellow_4": "#ddddcd",
    "paleyellow_5": "#777770",
    "brightyellow": "#eeeeaa",
    "black": "#000000",
    "gray_1": "#888888",
    "gray_2": "#e2e2e2",
    "gray_3": "#eeeeee",
    "gray_4": "#f6f6f6",
    "white": "#ffffff",
    "red_1": "#cc5d5d",
    "red_2": "#dd8888",
    "orange_1": "#c78f67",
    "orange_2": "#f8dfc8",
    "yellow_1": "#b8925a", 
    "green_1": "#558855",
    "green_2": "#a8cca8",
    "green_3": "#eeffee",
    "cyan_1": "#5aaaaa",
    "cyan_2": "#8ccccc",
    "cyan_3": "#aeeeee",
    "cyan_4": "#eeffff",
    "blue_1": "#4682b4",
    "blue_2": "#afdbff",
    "blue_3": "#cbe7ff",
    "blue_4": "#f0f8ff",
    "purple_1": "#8888cc",
    "purple_2": "#bbbbff",
    "magenta_1": "#aa6688",
    "magenta_2": "#d08eaa",
    "border": "#00000078",
    "invisible": "#00000000",
}

base_theme = {
    **colors,
    "theme_type": "light",
    "bg_1": colors["paleyellow_1"],
    "bg_2": colors["paleyellow_2"],
    "bg_3": colors["paleyellow_3"],
    "yellow_2": colors["brightyellow"],
    "blank_bg": colors["white"],
    "hover_bg": colors["white"],
    "selection_bg": colors["brightyellow"],
    "fg": colors["black"],
    "fg_dim": colors["black"] + "78",
    "fg_faint": colors["black"] + "40",
    "fg_ghost": colors["black"] + "20",
    "neutral_hl": colors["black"] + "10",
    "match_bg": colors["purple_2"] + "aa",
    "badge_bg": colors["purple_1"],
    "badge_fg": colors["white"],
    "button_bg": colors["purple_1"],
    "button_fg": colors["white"],
}

themes = {
    "acme": {
        **base_theme,
        "theme_name": "Acme",
        "ui_bg": colors["cyan_4"],
        "ui_hl": colors["cyan_3"],
        "gray": "#888880",
    },
    "acme_white":{
        **base_theme,
        "theme_name": "Acme White",
        "bg_1": colors["white"],
        "bg_2": colors["gray_4"],
        "bg_3": colors["gray_3"],
        "yellow_2": colors["orange_2"],
        "selection_bg": colors["orange_2"],
        "match_bg": colors["blue_3"] + "ee",
        "ui_bg": colors["blue_4"],
        "ui_hl": colors["blue_2"],
        "gray": colors["gray_1"],
        "border": "#00000058",
    }
}

def generate_theme(theme_dict, template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_file, "r") as f:
        theme_template = json.load(f)

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
    for theme_name, theme_dict in themes.items():
        output_file_name = f"{theme_name.replace('_', '-')}-color-theme.json"
        output_file_path = os.path.join('themes', output_file_name)
        generate_theme(theme_dict, 'src/template.json', output_file_path)


if __name__ == "__main__":
    main()
