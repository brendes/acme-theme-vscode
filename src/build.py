#!/usr/bin/env python3

import json
import os

colors = {
    "paleyellow_1": "#ffffea",
    "paleyellow_2": "#f2f2dd",
    "paleyellow_3": "#eeeed9",
    "paleyellow_4": "#ddddc8",
    "black": "#000000",
    "gray_1": "#888888",
    "gray_2": "#e2e2e2",
    "gray_3": "#eeeeee",
    "gray_4": "#f6f6f6",
    "white": "#ffffff",
    "red_1": "#cc5d5d",
    "red_2": "#dd8888",
    "orange_1": "#dd9870",
    "orange_2": "#f8c090",
    "yellow_1": "#99884c",
    "yellow_2": "#eeeea0",
    "green_1": "#558855",
    "green_2": "#a8cca8",
    "green_3": "#eeffee",
    "cyan_1": "#66aaaa",
    "cyan_2": "#99cccc",
    "cyan_3": "#aeeeee",
    "cyan_4": "#eeffff",
    "blue_1": "#4466bb",
    "blue_2": "#a4c4e0",
    "blue_3": "#cce4f2",
    "blue_4": "#f0f8ff",
    "purple_1": "#8888cc",
    "purple_2": "#bbbbff",
    "magenta_1": "#aa6688",
    "magenta_2": "#cc88aa",
    "border": "#00000088",
    "invisible": "#00000000",
}

base_theme = {
    **colors,
    "theme_type": "light",
    "fg": colors["black"],
    "fg_dim": colors["black"] + "6d",
    "fg_faint": colors["black"] + "44",
    "fg_ghost": colors["black"] + "20",
    "blank_bg": colors["white"],
    "neutral_hl": colors["black"] + "10"
}

themes = {
    "acme": {
        **base_theme,
        "theme_name": "Acme",
        "bg_1": colors["paleyellow_1"],
        "bg_2": colors["paleyellow_2"],
        "bg_3": colors["paleyellow_3"],
        "selection_bg": colors["yellow_2"],
        "match_bg": colors["purple_2"] + "ee",
        "ui_bg": colors["cyan_4"],
        "ui_hl": colors["cyan_3"],
        "hover_bg": colors["white"],
        "badge_bg": colors["purple_1"],
        "badge_fg": colors["white"],
        "button_bg": colors["purple_1"],
        "button_fg": colors["white"]
    },
    "acme_modern": {
        **base_theme,
        "theme_name": "Acme Modern",
        "bg_1": "#ffffee",
        "bg_2": "#f2f2e2",
        "bg_3": "#eeeede",
        "selection_bg": "#eeeeaa",
        "match_bg": colors["purple_2"] + "ee",
        "ui_bg": "#eeffff",
        "ui_hl": colors["cyan_3"],
        "hover_bg": colors["white"],
        "badge_bg": colors["purple_1"],
        "badge_fg": colors["white"],
        "button_bg": colors["purple_1"],
        "button_fg": colors["white"]
    },
    "acme_plain": {
        **base_theme,
        "theme_name": "Acme Plain",
        "bg_1": colors["paleyellow_1"],
        "bg_2": colors["paleyellow_2"],
        "bg_3": colors["paleyellow_3"],
        "selection_bg": colors["yellow_2"],
        "match_bg": colors["purple_2"] + "ee",
        "ui_bg": colors["paleyellow_1"],
        "ui_hl": colors["paleyellow_3"],
        "hover_bg": colors["white"],
        "badge_bg": colors["paleyellow_4"],
        "badge_fg": colors["black"],
        "button_bg": colors["purple_1"],
        "button_fg": colors["white"],
        "border": "#00000066"
    },
    "acme_white":{
        **base_theme,
        "theme_name": "Acme White",
        "bg_1": colors["white"],
        "bg_2": colors["gray_4"],
        "bg_3": colors["gray_3"],
        "selection_bg": colors["gray_2"],
        "match_bg": colors["orange_2"] + "ee",
        "ui_bg": colors["blue_4"],
        "ui_hl": colors["blue_3"],
        "hover_bg": colors["gray_4"],
        "badge_bg": colors["purple_1"],
        "badge_fg": colors["white"],
        "button_bg": colors["purple_1"],
        "button_fg": colors["white"]
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
