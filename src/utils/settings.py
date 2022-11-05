import json
import os
import re
from typing import Any, Dict


class ConfigError(Exception):
    """
    Base class for all exceptions related to config.
    """


def get_config() -> Dict[str, Any]:
    """
    Get the config.

    ### Returns
    - The dictionary with the config.

    ### Errors
    - ConfigError: If the config file does not exist.
    """

    config_path = os.path.join(os.getcwd(), "settings", "settings.json")

    if not os.path.exists(config_path):
        raise ConfigError(
            "\n\nConfig file not found.\nPlease check the repo source code to get the settings.json and put the file into the settings folder"
        )

    with open(config_path, "r", encoding="utf-8") as config_file:
        # Read the json file deleting the comments
        json_data = json.loads(
            "".join(re.split(r"(?://|#).*(?=\n)", config_file.read())).strip()
        )
        return validate_settings(json_data)


def validate_settings(settings: Dict[str, Any]) -> Dict[str, Any]:
    for key, default_value in DEFAULT_CONFIG.items():
        config_val = settings.get(key)

        if config_val != default_value and config_val is not None:
            settings[key] = config_val

            if (
                key == "id3_version"
                and settings[key] != "2.3"
                and settings[key] != "2.4"
            ):
                raise ConfigError(
                    "\n\nID3 Version should be 2.3 or 2.4\nPlease check your config file"
                )

        else:
            settings[key] = default_value

    return settings


DEFAULT_CONFIG = {
    "input_path": "input",  # Path where the .mp3 files to edit are
    "output_path": "output",  # Relative path where the edied songs will be stores
    "new_filename_format": "{artist} - {title}",  # Name format that the new generated files will have. Leave it as "" or delete this line if you don't want to change the name of your files. Check the read.me for the avalaible params.
    "id3_version": "2.3",  # 2.3 or 2.4
}
