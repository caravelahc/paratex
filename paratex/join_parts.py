import csv
import glob
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

PARTITIONED_PATH = Path(__file__).parent / "partitioned_csvs"
JOINED_PATH = Path(__file__).resolve().parent.joinpath("joined_csvs")


@dataclass
class CSV:
    headers: Tuple[str]
    data: List[Tuple[str]]

    @staticmethod
    def load(path: Path):
        with open(path) as f:
            reader = csv.reader(path)

            rows = [row for row in reader]

        return CSV(headers=tuple(rows[0]), data=rows[1:])

    def save(self, path: Path):
        with open(path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data)


def join_from_output(partitioned_path=PARTITIONED_PATH):
    """
    Joins all ".csv" files located in `partitioned_path` (non-recursive)
    into a single file.
    """
    assert os.access(partitioned_path, os.R_OK)
    JOINED_PATH.mkdir(parents=True, exist_ok=True)

    all_dfs = CSV()

    all_csv_files = list(partitioned_path.glob("*.csv"))
    all_csv_files.sort()

    interval_begin = all_csv_files[0].name.strip(".csv")
    interval_end = all_csv_files[-1].name.strip(".csv")

    for csv_file in all_csv_files:
        full_path = PARTITIONED_PATH.joinpath(csv_file)
        all_dfs.data += CSV.load(full_path).data

    all_dfs.save(JOINED_PATH.joinpath(f"{interval_begin}_to_{interval_end}.csv"))


if __name__ == "__main__":
    join_from_output()
