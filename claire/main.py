import shutil
from .command import read_args
from sys import argv
from pathlib import Path


def read_order_excel(command_file: Path) -> list[str]:
    """Read the excel for the current order and returns the list of required files."""
    raise NotImplementedError()


def copy_files(
    data_path: Path, target: Path, files: list[Path], subdir_name: str | None = None
):
    """Copy files from data_path to target."""
    if subdir_name is not None:
        final_dir = target / subdir_name
        final_dir.mkdir(parents=True, exist_ok=True)

    for file in files:
        try:
            shutil.copy(data_path / file, target)
        except FileNotFoundError:
            print(f"Cannot find {data_path / file}.")
            print("Please check the path of data.")


if __name__ == "__main__":
    data_path, target_dir, command_file = read_args(argv)

    orders = read_order_excel(command_file)
    copy_files(data_path, target_dir, orders)
