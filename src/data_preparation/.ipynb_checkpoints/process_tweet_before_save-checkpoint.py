import pandas as pd

def read_csv(path):
    #load data from csv to df
    df = pd.read_csv(path)
    df = pd.DataFrame(df['text'])
    return df



