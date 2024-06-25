from pathlib import Path


def help():
    """Help function."""
    print()
    print("Usage: python main.py --data <data_path> --target <target_path>")
    print(
        "\nOptional: --target <target_path> to speicfy where to write the final photos.\n"
    )
    exit()


def read_args(args: list[str]) -> tuple[Path, Path, Path]:
    """
    Arguments:
    --command: Path to the excel of the command
    --data : Directory to find photos
    --target : Directory to save order, if no target provided, data will be written
        where the command is launched
    Returns a 3-tuple of Path objects, the data_path, the target dir and the command_file.
    """
    data_path: Path | None = None
    command_file: Path | None = None

    target: str = Path("./commands/")

    n_args = len(args)
    index = 1
    while index < n_args:
        if args[index] == "--data":
            data = Path(args[index + 1])
            index += 2
        elif args[index] == "--target":
            target = Path(args[index + 1])
            index += 2
        elif args[index] == "--command":
            command_file = Path(args[index + 1])
            if command_file.suffix != ".xlsx":
                print("Command file must be an excel file.")
                help()
            index += 2
        elif args[index] == "--help":
            help()
        else:
            index += 1

    if data_path is None or command_file is None:
        print("Invalid arguments.")
        print("Use --help for more information.")
        help()

    return data_path, target, command_file
