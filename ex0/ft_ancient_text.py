import typing
import sys


def read_file() -> None:
    if(len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO = open(f"{sys.argv[1]}", "r")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return
        content = f.read()
        f.close()
        print("---")
        print()
        print(f"{content}")
        print("---")
        print(f"File '{sys.argv[1]}' closed.")


def main() -> None:
    read_file()


if __name__ == "__main__":
    main()
