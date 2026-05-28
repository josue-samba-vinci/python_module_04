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

        print()

        print("Transform data:")
        print("---")
        print()
        lines = content.splitlines()
        modified_lines = "\n".join(line + "#" for line in lines) + "\n"
        print("---")
        print(modified_lines, end="")
        print("---")
        new_name = input("Enter new file name (or empty): ")
        if not new_name:
            print("Not saving data")
        else:
            new_file = open(f"{new_name}", "w")
            new_file.write(modified_lines)
            new_file.close()
            print(f"Saving data to '{new_name}'")
            print(f"Data saved in file '{new_name}'")


def main() -> None:
    read_file()


if __name__ == "__main__":
    main()
