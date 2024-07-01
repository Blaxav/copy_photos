import shutil
from command import read_args
from sys import argv
from pathlib import Path
import pandas as pd
import numpy as np
import os


PHOTO_EXTENSION = ".JPG"


def read_order_excel(command_file: Path) -> list[str]:
    """Read the excel for the current order and returns the list of required files."""
    data = pd.read_excel(command_file)
    # Fill missing data with python's None
    data = data.fillna(np.nan).replace([np.nan], [None])
    res = []

    row_id = 0
    col_id = 0
    found = False
    while not found:
        try:
            value = data.iloc[row_id, col_id]
            if value == "N° Photo":
                found = True
                break
            else:
                col_id += 1
        except IndexError:
            row_id += 1
            col_id = 0

    row_id += 1
    while True:
        val = data.iloc[row_id, col_id]
        if val is not None:
            res.append(str(val))
            row_id += 1
        else:
            break
    return res


def copy_files(data_path: Path, target: Path, files: list[Path]):
    """Copy files from data_path to target."""

    target.mkdir(parents=True, exist_ok=True)

    for order in orders:
        filename = order + PHOTO_EXTENSION
        try:
            shutil.copy(data_path / filename, target / filename)
        except FileNotFoundError:
            print(f"Cannot find {data_path / filename}.")
            print("Please check the path of data.")


if __name__ == "__main__":
    data_path, _, _ = read_args(argv)

    # Get files prefix
    prefixes = set()
    for _file in os.listdir(data_path):
        if _file.endswith(PHOTO_EXTENSION):
            prefixes.add(_file[:4])

    if len(prefixes) > 1:
        raise ValueError("All files must have the same four charactersprefix.")

    prefix = list(prefixes)[0]

    for _file in os.listdir(data_path):
        if _file.endswith(".xlsx"):
            command_file = data_path / _file
            orders = [prefix + elt for elt in read_order_excel(command_file)]

            target = data_path / _file.split(".", 1)[0].replace(" ", "_")
            copy_files(data_path, target, orders)
