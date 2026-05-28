def secure_archive(
        file_name: str, action: str = "r", content: str = ""
        ) -> tuple:
    try:
        if action == "r":
            with open(file_name, "r") as file:
                return(True, file.read())
        else:
            with open(file_name, "w") as file:
                file.write(content)
                return(True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print("Using 'secure_archive' to read from a regular file:")
    previous_content = secure_archive("ancient_fragment.txt")
    print(previous_content)
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", previous_content[1]))


if __name__ == "__main__":
    main()
