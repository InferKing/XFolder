import shutil
from argparse import Namespace
import os

class FileSorter:
    """
    Class for sorting files based on the configuration.

    Args:
        config (dict): The configuration dictionary.
        args (Namespace): The command line arguments.
    """
    def __init__(self, config: dict, args: Namespace):
        """
        Initializes the FileSorter class.

        Args:
            config (dict): The configuration dictionary.
            args (Namespace): The command line arguments.
        """
        self.__config = config
        self.__args = args



    def sort_files(self):
        """
        Sorts files based on the configuration.

        This method iterates over the files in the specified directory and its subdirectories.
        For each file, it checks if it matches any of the extensions specified in the configuration.
        If the file matches and is not in the ignore list, it moves the file to the corresponding folder.
        If the folder does not exist, it creates the folder.
        """
        ignore_list = self.__args.ignore
        if self.__args.no_ignore:
            ignore_list = []
        matches = self.__config["matches"]
        for key in matches:
            for file in matches[key]["extensions"]:
                for root, dirs, files in os.walk(self.__args.path):
                    if self.__args.no_recursive:
                        dirs.clear()
                    for name in files:
                        folder_name = matches[key]["folder"]
                        if name.endswith(file) and name not in ignore_list:
                            new_path = os.path.join(root, folder_name)
                            if not os.path.exists(new_path):
                                os.mkdir(new_path)
                            shutil.move(os.path.join(root, name), os.path.join(root, folder_name, name))
