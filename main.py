import os
import colorama
from scripts.args_handler import ArgsHandler
from scripts.config_utils import ConfigLoader, ConfigAnalyzer
from scripts.printer import MessagePrinter
from scripts.file_sorter import FileSorter

def main():
    os.system('cls')
    colorama.init()
    args = ArgsHandler().parse_args()
    loader = ConfigLoader(__file__, args.config)
    analyzer = ConfigAnalyzer(loader.config)
    if analyzer.analyze_config():
        MessagePrinter.print_app_name(
            loader.config.get("version", "UNKNOWN"), 
            loader.config.get("author", "UNKNOWN"))
        fs = FileSorter(loader.config, args)
        fs.sort_files()


if __name__ == "__main__":
    main()