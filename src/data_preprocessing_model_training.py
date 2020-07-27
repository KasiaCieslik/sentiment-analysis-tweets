import sys
import numpy as np
import pandas as pd

sys.path.append('/home/kasia/sentiment-analysis-of-tweets-using-emoticons')
from data_preparation.read_data import read_csv
from data_preprocessing.clean_tweet import preprocess_data
from features.spacy_helpers import setup_spacy, add_spacy_features
from features.prepare_target import add_polarity_scores, sum_polarity, prepare_target
from models.model import random_search_best_estimator, final_model, save_model
from features.train_test_preparation import y_X_preparation, train_test_preparation_for_model
from data_preprocessing.clean_dataframe import additional_processing, downsample_target
from data_preparation.reference_emoji_list import prepare_reference_emoji_list

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression, Lasso
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier

from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score

nlp = setup_spacy()
df = read_csv("../data/raw/raw_tweets.csv")
df = preprocess_data(df)
df = add_spacy_features(df=df, nlp=nlp)
df = additional_processing(df)

emoji_dict = prepare_reference_emoji_list(nlp=nlp)
df = add_polarity_scores(df, emoji_dict, emoji_column='unique_emoji')
df = df[df.polarity_for_unique_emoji.map(bool)]
df = sum_polarity(df)
df = prepare_target(df)
df = downsample_target(df)

X, y = y_X_preparation(df)
X_train, X_test, y_train, y_test = train_test_preparation_for_model(X, y)

logistic = LogisticRegression()
knn = KNeighborsClassifier()
rfc = RandomForestClassifier()
sgd = SGDClassifier()

scorer = make_scorer(accuracy_score)

param_grid = [  # {'alpha': np.linspace(0.00001, 1, 40)},
    {'penalty': ['l2'], 'C': [0.1, 1, 5, 10], 'solver': ['lbfgs', 'liblinear']},
    {'n_neighbors': [1, 3, 5, 10]},
    {'n_estimators': list(range(10, 101, 10)), 'max_features': list(range(6, 32, 5))},
    {'average': [True, False], 'alpha': np.linspace(0.001, 1, 40)}]
model_list = [logistic, knn, rfc, sgd]

grid_search, grid_results, results = random_search_best_estimator(scorer, param_grid, model_list, X_train, X_test,
                                                                  y_train, y_test)
results = pd.DataFrame(results)
best_estimator = results['best_estimator'][results['best_score'] == results['best_score'].max()].iloc[0]
final_accuracy_test,final_accuracy_train,pred_test,pred_train = final_model(X_train, X_test, y_train, y_test, best_estimator)
save_model('../models', 'best_estimator.sav', best_estimator)
