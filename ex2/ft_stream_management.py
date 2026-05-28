import typing
import sys


def read_file() -> None:
    if(len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO = open(f"{sys.argv[1]}", "r")
        except OSError as e:
            sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}'"
                             f": {e}\n")
            sys.stderr.flush()
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
        lines = content.splitlines()
        modified_lines = "\n".join(line + "#" for line in lines) + "\n"
        print("---")
        print()
        print(modified_lines)
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_name = sys.stdin.readline().rstrip("\n")
        if not new_name:
            print("Not saving data.")
        else:
            try:
                new_file = open(f"{new_name}", "w")
            except OSError as e:
                print(f"Saving data to '{new_name}'")
                sys.stderr.write(f"[STDERR] Error opening file '{new_name}'"
                                 f": {e}\n")
                sys.stderr.flush()
                print("Data not saved")
                return
            print(f"Saving data to '{new_name}'")
            new_file.write(modified_lines)
            new_file.close()
            print(f"Data saved in file '{new_name}'")


def main() -> None:
    read_file()


if __name__ == "__main__":
    main()
