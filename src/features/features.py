import pandas as pd

def get_hours(time:str) -> int:
    return int(time.split(':')[0])

def add_early_wakeup(df: pd.DataFrame) -> pd.DataFrame:
    df['Жаворонок'] = df['Время пробуждения']
    df['Жаворонок'] = df['Время пробуждения'].apply(lambda x: 1 if get_hours(x) <= 7 else 0)
    return df
