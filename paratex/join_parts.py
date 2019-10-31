import os
from pathlib import Path
import glob

import pandas as pd

SOURCE_DIR = Path(__file__).resolve().parent.joinpath('output_partitioned')
JOINED_PATH = Path(__file__).resolve().parent.joinpath('joined_csvs')
JOINED_PATH.mkdir(parents=True, exist_ok=True)
assert(os.access(SOURCE_DIR, os.R_OK))

def join_from_output(output_path=SOURCE_DIR):
    """Função usada para juntar os csvs separados para cada sessão,
    caso o extrator seja executado no modo particionado"""
    all_dfs = pd.DataFrame()
    all_csv_files = list(output_path.glob('*.csv'))
    all_csv_files.sort()
    interval_begin = all_csv_files[0].name.strip(".csv")
    interval_end = all_csv_files[-1].name.strip(".csv")
    
    for csv_file in all_csv_files:
        full_path = SOURCE_DIR.joinpath(csv_file)
        all_dfs = pd.concat([all_dfs, pd.read_csv(full_path)])
    
    all_dfs.to_csv(JOINED_PATH.joinpath(f"{interval_begin}_to_{interval_end}.csv"), index=False)

if __name__ == '__main__':
    join_from_output()
