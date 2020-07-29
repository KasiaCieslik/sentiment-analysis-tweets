from typing import List


def downsample_target(df):
    """
    Return balanced dataframe
    Parameters
    ----------
    df: pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    min_target_number = df['sentiment_target'].value_counts().min()
    df = df.groupby('sentiment_target').apply(lambda x: x.sample(min_target_number, replace=False))
    df = df.reset_index(drop=True)#.drop(['level_0','index'],axis=1)
    return df

def remove_dup_tokens(tokens):
    """
    Return list with unique tokens
    Parameters
    ----------
    tokens: token.spacy

    Returns
    -------
    List  
    """
    collect = []
    seen = []
    for token in tokens:
        if str(token) not in seen:
            collect.append(token)
        seen.append(str(token))
    return collect


def unique_tokens(emojis_column: str) -> List[list]:
    """

    Parameters
    ----------
    emojis_column: pandas.core.series.Series

    Returns
    -------
    List[list]
    """
    unique_emoji = []
    for emoji in emojis_column:
        collect = remove_dup_tokens(emoji)
        unique_emoji.append(collect)
    return unique_emoji  



def additional_processing(df):
    """
    Remove rows without emoji
    Parameters
    ----------
    df: pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    df = df[df['emoji'].map(len)!=0]
    return df


