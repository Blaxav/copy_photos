from pathlib import Path


def help():
    """Help function."""
    print()
    print("Usage: python main.py --data <data_path> ")
    exit()


def read_args(args: list[str]) -> Path:
    """
    Arguments:
    --data : Directory to find photos
    Returns the data_path.
    """
    data_path: Path | None = None

    target: str = Path("./commands/")
    n_args = len(args)
    index = 1
    while index < n_args:
        if args[index] == "--data":
            data_path = Path(args[index + 1])
            index += 2
        elif args[index] == "--help":
            help()
        else:
            index += 1

    if data_path is None:
        print("Invalid arguments.")
        print("Use --help for more information.")
        help()

    return data_path
