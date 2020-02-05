import os
from pathlib import Path
import glob

import pandas as pd

PARTITIONED_PATH = Path(__file__).parent / 'partitioned_csvs'
JOINED_PATH = Path(__file__).resolve().parent.joinpath('joined_csvs')

def join_from_output(partitioned_path=PARTITIONED_PATH):
    '''Joins all ".csv" files located in `partitioned_path` (non-recursive)
    into a single file.'''
    assert(os.access(partitioned_path, os.R_OK))
    JOINED_PATH.mkdir(parents=True, exist_ok=True)

    all_dfs = pd.DataFrame()
    all_csv_files = list(partitioned_path.glob('*.csv'))
    all_csv_files.sort()
    interval_begin = all_csv_files[0].name.strip('.csv')
    interval_end = all_csv_files[-1].name.strip('.csv')

    for csv_file in all_csv_files:
        full_path = PARTITIONED_PATH.joinpath(csv_file)
        all_dfs = pd.concat([all_dfs, pd.read_csv(full_path)])

    all_dfs.to_csv(JOINED_PATH.joinpath(f'{interval_begin}_to_{interval_end}.csv'), index=False)

if __name__ == '__main__':
    join_from_output()
