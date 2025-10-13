import glob
import os
import pandas as pd

def load_transects(file_pattern):
    csv_files = glob.glob(file_pattern)
    
    dfs = []
    for file in csv_files:
        basename = os.path.basename(file)
        date_str = basename.split('join_')[1].split('-transect')[0]
        df = pd.read_csv(file)
        df['survey_date'] = date_str
        dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)