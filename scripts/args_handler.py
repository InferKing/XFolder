import argparse


class ArgsHandler:
    """
    Class for handling command line arguments.
    """

    def __init__(self):
        """
        Initializes the ArgsHandler class.
        """
        self.__parser = argparse.ArgumentParser(description="Sort files by extension")
        group = self.__parser.add_mutually_exclusive_group()

        self.__parser.add_argument("-c", "--config",
                                   help="Path to config file where file sorting settings are located. Default - config.json",
                                   type=str,
                                   default="config.json")
        self.__parser.add_argument("--path",
                                   help="Path to directory to sort files. Default - current directory.",
                                   type=str,
                                   default="")
        self.__parser.add_argument("--no-recursive", action="store_true", help="Do not sort files in subdirectories.")
        group.add_argument("-i", "--ignore",
                           help="Extensions to ignore. Default - .py",
                           type=str,
                           default=[".py"],
                           action='extend',
                           metavar="EXTENSION",
                           nargs="+")
        group.add_argument("--no-ignore",
                           action="store_true",
                           help="Do not ignore any files.")

    def parse_args(self) -> argparse.Namespace:
        """
        Parses the command line arguments and returns the parsed arguments.

        Returns:
            argparse.Namespace: The parsed arguments.
        """
        return self.__parser.parse_args()
