#!/usr/bin/env python3

import json
import os
import re

from config import themes


def theme_filename(name):
    filename = re.sub(r"[^\w\s-]", "", name.lower())
    filename = re.sub(r"[-\s]+", "-", filename)
    return filename.strip("-")


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
    output_dir = "themes"
    template_file = "src/template.json"
    for theme_dict in themes:
        name = theme_dict.get("name")
        output_name = f"{theme_filename(name)}-color-theme.json"
        output_path = os.path.join(output_dir, output_name)
        generate_theme(theme_dict, template_file, output_path)


if __name__ == "__main__":
    main()
