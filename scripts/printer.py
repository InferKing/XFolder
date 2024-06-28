import colorama
import art


class MessagePrinter:
    """
    This class provides static methods for printing colored and formatted messages to the console.
    """

    @staticmethod
    def print(message: str, color: str = colorama.Fore.WHITE, end: str = "\n") -> None:
        r"""
        Prints a message to the console in the specified color.

        Args:
            message (str): The message to be printed.
            color (str, optional): The color of the message. Defaults to white.
            end (str, optional): The character to be printed after the message. Defaults to "\n".
        """
        print(color + message + colorama.Style.RESET_ALL, end=end)
    
    @staticmethod
    def print_error(message: str, end: str = "\n") -> None:
        r"""
        Prints an error message to the console in red color.

        Args:
            message (str): The error message to be printed.
            end (str, optional): The character to be printed after the message. Defaults to "\n".
        """
        MessagePrinter.print(message, colorama.Fore.RED, end)
    
    @staticmethod
    def print_app_name(version: str, author: str) -> None:
        """
        Prints the name and version information of the application to the console.

        Args:
            version (str): The version of the application.
            author (str): The author of the application.
        """
        print(colorama.Fore.WHITE + art.decor("sad1") + colorama.Fore.BLUE + "XFolder" + colorama.Style.RESET_ALL + art.decor("sad1", reverse=True))
        print(colorama.Fore.BLUE + "Version: " + version + " by " + author + colorama.Style.RESET_ALL)
