import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_directory_structure(path, prefix=""):

    try:
        items = sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name.lower()))
        total_items = len(items)

        for index, item in enumerate(items):
            is_last = index == total_items - 1
            connector = "┗ " if is_last else "┣ "
            next_prefix = prefix + ("    " if is_last else "┃   ")

            if item.is_dir():
                print(f"{prefix}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                print_directory_structure(item, next_prefix)
            else:
                print(f"{prefix}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"{prefix}{Fore.RED}┗ Access denied{Style.RESET_ALL}")


def main():

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python hw03.py /path/to/directory{Style.RESET_ALL}")
        return

    directory_path = Path(sys.argv[1])


    if not directory_path.exists():
        print(f"{Fore.RED}Error: path does not exist.{Style.RESET_ALL}")
        return


    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: path is not a directory.{Style.RESET_ALL}")
        return
    print(f"{Fore.YELLOW}📦 {directory_path.name}{Style.RESET_ALL}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
