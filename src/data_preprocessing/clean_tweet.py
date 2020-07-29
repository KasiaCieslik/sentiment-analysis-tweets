import re
import string
import numpy as np

def remove_pattern_from_tweet(input_txt, pattern):
    """
    Remove pattern from text like retweets, hashtags etc.
    Parameters
    ----------
    input_txt: str
    pattern: str

    Returns
    -------
    str
    """
    try:
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)
        
        return input_txt  
    except:
        return None
    
def cleanString(strval):
    """
    Remove punctation
    Parameters
    ----------
    strval: str

    Returns
    -------
    str
    """
    return "".join(" " if i in string.punctuation else i for i in strval.strip(string.punctuation))


def preprocess_data(df):
    """
    Add column with preprocessed text without pattern
    Parameters
    ----------
    df: pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    df['tidy_text'] = np.vectorize(remove_pattern_from_tweet)(df['text'], "RT\s.\w+:") #remove retweets
    df['tidy_text'] = np.vectorize(remove_pattern_from_tweet)(df['tidy_text'], "(@[A-Za-z0-9_]+)") #remove twitter user name
    df['tidy_text'] = np.vectorize(remove_pattern_from_tweet)(df['tidy_text'], "(#\w+)")#remove hashtags
    df['tidy_text'] = np.vectorize(remove_pattern_from_tweet)(df['tidy_text'], "(?P<url>https?://[^\s]+)")
    df['tidy_text'] = np.vectorize(cleanString)(df['tidy_text'])#remove punctation   
    return df


