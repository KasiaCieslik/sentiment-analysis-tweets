from datetime import datetime

def save_tweets(df,path,file_name):
    """
    Function to save data frame with filtered tweets
    File name contains current date"
    Parameters
    ----------
    df: pd.DataFrame
    path: str
    file_name:str

    Returns
    -------
    None
    """

    date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))
    return df.to_csv(path + "/" + file_name + date +".csv")

