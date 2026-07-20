import typing
import sys


def read_file() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO[str] = open(f"{sys.argv[1]}", "r")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return
        try:
            content = f.read()
        except UnicodeDecodeError as e:
            print(f"Error reading file '{sys.argv[1]}': not valid UTF-8 ({e})")
            return
        except (Exception) as e:
            print(f"Error : {e}")
            return
        finally:
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
        print(modified_lines, end="")
        print("---")
        try:
            new_name = input("Enter new file name (or empty): ")
        except (KeyboardInterrupt, EOFError):
            print("Error")
            return
        if not new_name:
            print("Not saving data.")
        else:
            new_file = open(f"{new_name}", "w")
            print(f"Saving data to '{new_name}'")
            new_file.write(modified_lines)
            new_file.close()
            print(f"Data saved in file '{new_name}'")


def main() -> None:
    read_file()


if __name__ == "__main__":
    main()
