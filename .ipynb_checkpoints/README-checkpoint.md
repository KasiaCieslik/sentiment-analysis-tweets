
# sentiment-analysis-of-tweets-using-emoticons
In this project I download tweets (Thython) and I semilabeled them using emojis.
I used table with polarity for every emoji and calculted sum of polarity for unique emojis for every tweet. 
Using this information I grouped emojis in two groups (positive/negative). 
I used TfidfVectorizer() and average_tweet_vectorizer() to prepare the features.

## Download data for experiment

Data used for the experiment: 
https://drive.google.com/file/d/1-7yg9HrAqtFvP5K5r35yKThiXKxZaVco/view?usp=sharing

![raw_dataframe.png](static/raw_dataframe.png) 

## Download new data with your own criteria

To download new data use './tweets_scraper.py'
You can change query, language for searching tweets.
To set number of download tweets use 'range_number,tweets_number_for_every_range' parameters

## Data preprocessing and model training

To do data preprocessing and model training use "data_preprocessing_model_training.py"

## What should I install

All needed libraries are to find in 'requirements.txt' file.
 