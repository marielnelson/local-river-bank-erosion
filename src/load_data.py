import glob
import os
import pandas as pd
from src.bank_profile import BankProfile

# think about whether these should be separate or a single function that returns both the df and the profiles

def create_bank_profiles_df(file_pattern):

    files = glob.glob(file_pattern)
    dfs = []
    for file in files:
        basename = os.path.basename(file)
        date_str = basename.split('join_')[1].split('-transect')[0]
        df = pd.read_csv(file)
        df['survey_date'] = date_str
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

def create_bank_profiles(profile_df):
    
    profiles = []
    for (idx, date), group in profile_df.groupby(['transect_idx', 'survey_date']):
        t = BankProfile(group, idx, date)
        profiles.append(t)
    
    return profiles