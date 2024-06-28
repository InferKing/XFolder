import os
import json
from jsonschema import Draft202012Validator
from scripts.printer import MessagePrinter

class ConfigLoader:
    """
    Class for loading configuration files.
    """

    def __init__(self, cur_path: str, config_path: str) -> None:
        """
        Initializes the ConfigLoader class.

        Args:
            cur_path (str): The path to the current script.
            config_path (str): The path to the configuration file.
        """
        self.__config_path = config_path
        self.__config = self.__load_config(
            os.path.join(os.path.dirname(cur_path), self.__config_path)
        )


    def __load_config(self, config_path: str) -> dict:
        """
        Loads the configuration file.

        Args:
            config_path (str): The path to the configuration file.

        Returns:
            dict: The loaded configuration.
        """
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except FileNotFoundError as e:
            MessagePrinter.print_error(e.strerror)
            exit(1)
        except json.JSONDecodeError as e:
            MessagePrinter.print_error(e.msg + " in " + config_path)
            exit(1)

    @property
    def config(self) -> dict:
        """
        Returns the loaded configuration.

        Returns:
            dict: The loaded configuration.
        """
        return self.__config


class ConfigAnalyzer:
    """
    This class analyzes the configuration file.
    """
    def __init__(self, config: dict) -> None:
        """
        Initializes the ConfigAnalyzer class.

        Args:
            config (dict): The loaded configuration.
        """
        self.__config = config
        self.__schema = {
            "type": "object",
            "properties": {
                "version": {"type": "string"},
                "author": {"type": "string"},
                "matches": {
                    "type": "object",
                    "properties": {
                        key: {
                            "type": "object",
                            "properties": {
                                "extensions": {"type": "array", "items": {"type": "string"}},
                                "folder": {"type": "string"}
                            }
                        }
                        for key in ["img", "txt", "video", "audio", "archive", "pdf", "code", "other"]
                    },
                    "additionalProperties": True
                }
            },
            "required": ["matches"],
            "additionalProperties": False,
        }

    def analyze_config(self) -> bool:
        """
        Analyzes the configuration file.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        validator = Draft202012Validator(self.__schema)
        if not validator.is_valid(self.__config):
            MessagePrinter.print_error("Config is not valid!", end="\n\n")
            for error in sorted(validator.iter_errors(self.__config), key=lambda e: e.path):
                MessagePrinter.print_error(error.message)
                if error.absolute_path:
                    MessagePrinter.print_error("Path in config: " + " -> ".join(error.absolute_path), end="\n")
                MessagePrinter.print("-"*50 + "\n")
            return False
        return True
