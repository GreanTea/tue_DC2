# regression model? predictive
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pandas as pd
import numpy as np

final_df = pd.read_csv('/volumes/Seagate DNvG/School/dc2/data/final_dataset.csv')
# Year, month, lsoa, burglaries, drugs
trainval_df, test_df = train_test_split(final_df, test_size=0.2)
train_df, val_df = train_test_split(trainval_df, test_size=0.2)
X_train = train_df[['Month', 'Drugs']] # dataframe with all attributes to predict y
y_train = train_df['Burglaries'] # series with crime rate per lsoa
X_val = val_df[['Month', 'Drugs']]
y_val = val_df['Burglaries']
X_trainval = trainval_df[['Month', 'Drugs']]
y_trainval = trainval_df['Burglaries']
X_test = test_df[['Month', 'Drugs']]
y_test = test_df['Burglaries']

# fit model to training data
# evaluate on test data
logreg = LogisticRegression(max_iter=10000)
logreg.fit(X_trainval, y_trainval)
lr_trs = logreg.score(X_trainval, y_trainval)
lr_tes = logreg.score(X_test, y_test)
print("Logistic Regression\n--Training score: {}\n--Test score: {}".format(lr_trs, lr_tes))

best_score = 0
for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        svm.fit(X_train, y_train)
        score = svm.score(X_val, y_val)
        if score > best_score:
            best_score = score
            bp = {'C': C, 'gamma': gamma}
svm = SVC(gamma=bp['gamma'], C=bp['C'])
svm.fit(X_trainval, y_trainval)
svm_tes = svm.score(X_test, y_test)
print("Linear SVC\n--Best validation score: {}\n--Best parameters: {}\n"
      "--Test score with best parameters: {}".format(best_score, bp, svm_tes))
