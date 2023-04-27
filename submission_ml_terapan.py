# -*- coding: utf-8 -*-
"""Submission ML - Terapan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NfbaehYC1uloloXgmHwVuDokRE_BFk55

### Import Key kaggle
"""

! chmod 600 /content/kaggle.json

! KAGGLE_CONFIG_DIR=/content/ kaggle datasets download -d shantanudhakadd/bank-customer-churn-prediction

"""## Import resource data"""

import zipfile
zip_file = zipfile.ZipFile('/content/bank-customer-churn-prediction.zip')
zip_file.extractall('/tmp/')

"""### Install library not available in Google colab"""

pip install skfeature-chappers

pip install catboost

"""## Import all realated libraries"""

# import libraries for data analysis
import numpy as np
import pandas as pd
import random
import os

# import libraries for label encoder
from sklearn.preprocessing import LabelEncoder

# import library for visualization
import seaborn as sns
import matplotlib.pyplot as plt

# import pickle and json file for columns and model file
import pickle
import json

# import warnings for ignore the warnings
import warnings 
warnings.filterwarnings("ignore")

# library for model selection and models
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC

# impory library for scaling purpose
from sklearn.preprocessing import StandardScaler

# evaluation metrics for classification model
from sklearn import metrics
from sklearn.metrics import mean_squared_error as mse, mean_absolute_error as mae, accuracy_score, confusion_matrix, roc_curve, roc_auc_score, classification_report, f1_score

# import libraries for feature selection
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_selection import mutual_info_classif, chi2, f_classif, VarianceThreshold


# import libraries for balancing the data
from imblearn.over_sampling import SMOTE
from collections import Counter
from imblearn.over_sampling import RandomOverSampler

# import libraries for normalize data
from sklearn.preprocessing import MinMaxScaler

# import libraries for comparison algorithm
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# import algorithm classifier
import xgboost as xgb
import lightgbm as lgbm
import catboost as cb


# full display
pd.set_option("display.max_columns",None)

"""### Membuat dataframe dari resource data"""

df = pd.read_csv("/tmp/Churn_Modelling.csv")

"""#### Membuat backup data
#####Agar tidak mengganti data asli


"""

df1 = df.copy()

"""### Mengatur seed agar nilai konsisten ketika diproses"""

def set_seed(seed_value):
    random.seed(seed_value)
    np.random.seed(seed_value)
    os.environ["PYTHONHASHSEED"] = str(seed_value)
    

SEED = 42
set_seed(SEED)

"""### Melihat informasi dataframe"""

df1.info()

"""  ### Cek nilai unik di setiap kolom"""

for col in df1.columns:
    c = df1[col].nunique()
    print(f"Unique count of {col} is {c}")

"""### Melakukan drop pada baris yang kosong"""

df1.isnull().sum()

""" ### Cek nilai yang duplikat pada dataframe"""

df1.duplicated().sum()

"""### Menghapus kolom yang memiliki setiap baris keunikan untuk mempermudah analisa dan proses data"""

del df1["CustomerId"]
del df1["RowNumber"]

"""### Melakukan encoding/memberikan label pada setiap string/object"""

le=LabelEncoder()
df1["Surname"]=le.fit_transform(df1["Surname"])
df1["Geography"]=le.fit_transform(df1["Geography"])
df1["Gender"]=le.fit_transform(df1["Gender"])

"""### Melakukan pengecekan pada kolom memiliki nilai continous"""

for col in ["CreditScore","EstimatedSalary","Age","Balance"]:
    fig,ax=plt.subplots(1,2,figsize=(20,6))
    sns.distplot(df1[col],ax=ax[0],color = "g")
    sns.boxplot(df1[col],ax=ax[1],color = "g")
    plt.title(col)

"""### Melihat persebaran data"""

for col in ["Geography","Gender","Tenure","NumOfProducts","NumOfProducts","HasCrCard","IsActiveMember"]:
    print(col)
    print(f"The value count of {col} is \n{df1[col].value_counts()}")
    print("*"*100)

"""### Membuat heatmap untuk melihat korelasi antar variabel"""

cmap=sns.diverging_palette(150,75,  s=40, l=65, n=9)
corrmat = df1.corr()
plt.subplots(figsize=(12,12))
sns.heatmap(corrmat,cmap=cmap,annot=True, square=True);

"""### IQR"""

Q1=df1.quantile(0.25)
Q3=df1.quantile(0.75)
IQR=Q3-Q1
IQR
print("outlier Counter of the all features")
((df1 < (Q1 - 1.5 * IQR)) | (df1> (Q3 + 1.5 * IQR))).sum()

"""### Cleansing outlier data"""

for col in df1.columns:
    if df1[col].dtypes != 'object':
        q1 , q3 =df1[col].quantile(0.25),df1[col].quantile(0.75)
        iqr = q3 - q1
        ll = q1-1.5*iqr
        ul = q3 + 1.5*iqr
        # df1["CreditScore"] = np.where(df1["CreditScore"]>ul,df1["CreditScore"].mean(),np.where(df1["CreditScore"]<ll,df1["CreditScore"].mean(),df1["CreditScore"]))  
        df1["Age"] = np.where(df1["Age"]>ul,df1["Age"].mean(),np.where(df1["Age"]<ll,df1["Age"].mean(),df1["Age"]))  
        df1["NumOfProducts"] = np.where(df1["NumOfProducts"]>ul,df1["NumOfProducts"].mean(),np.where(df1["NumOfProducts"]<ll,df1["NumOfProducts"].mean(),df1["NumOfProducts"]))

print("outlier Counter of the all features")
((df1 < (Q1 - 1.5 * IQR)) | (df1> (Q3 + 1.5 * IQR))).sum()

df1['Age'].unique()

"""### Melakukan imbalancing data"""

x=df1.iloc[:,:-1].values
y=df1.iloc[:,-1].values
# S=RandomOverSampler()
sm = SMOTE(sampling_strategy=0.75)
x_data,y_data=sm.fit_resample(x,y)
print(Counter(y_data))

"""### Melakukan normalize data"""

mms=MinMaxScaler()
d=mms.fit_transform(x_data)
d

"""### Splitting data"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(d,y_data,random_state=45,test_size=0.20, stratify = y_data)

x_train

"""### Hyperparameter pipeline"""

pipeline_logistic=Pipeline([("scalar1",StandardScaler()),
                     ("lr_classifier",LogisticRegression())])

pipeline_decision_t=Pipeline([("scalar2",StandardScaler()),
                     ("dt_classifier",DecisionTreeClassifier())])


pipeline_random_f=Pipeline([("scalar3",StandardScaler()),
                     ("rf_classifier",RandomForestClassifier())])


pipeline_kn=Pipeline([("scalar4",StandardScaler()),
                     ("kn_classifier",KNeighborsClassifier())])


pipeline_xgb=Pipeline([("scalar5",StandardScaler()),
                     ("xg_classifier",XGBClassifier())])


pipeline_svm=Pipeline([("scalar5",StandardScaler()),
                     ("svm_classifier",SVC())])
pipelines = [pipeline_logistic, pipeline_decision_t, pipeline_random_f, pipeline_kn, pipeline_xgb,pipeline_svm]
pipe_dict = {0: "LogisticRegression", 1: "DecisionTree", 2: "RandomForest",3: "KNeighbors", 4: "XGB",5 : "SCV"}
for pipe in pipelines:
    pipe.fit(x_train, y_train)
cv_results_rms = []
for i, model in enumerate(pipelines):
    cv_score = cross_val_score(model, x_train,y_train,scoring="f1", cv=10)
    cv_results_rms.append(cv_score)
    print("%s: %f " % (pipe_dict[i], cv_score.mean()))

"""### Membuat dataframe untuk hasil akurasi klasifikasi algoritma"""

data = {'Model': [], 'F1 Score (mean)': [], 'F1 Score (std)': []}
for i, model in enumerate(pipelines):
    data['Model'].append(pipe_dict[i])
    data['F1 Score (mean)'].append(cv_results_rms[i].mean())
    data['F1 Score (std)'].append(cv_results_rms[i].std())

# Membuat dataframe dari data
df = pd.DataFrame(data)
print(df)

"""### Fitting Model"""

model = RandomForestClassifier()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
model.score(x_test,y_test)

model.score(x_train,y_train)

"""### Mencari akurasi data training"""

y_pred_train  = model.predict(x_train)
ac_score_tr   = accuracy_score(y_train,y_pred_train)
print("ac_score_tr",ac_score_tr)
conf_mT_tr    = confusion_matrix(y_train,y_pred_train)
print("conf_mT_tr\n",conf_mT_tr)
cls_report_tr = classification_report(y_train,y_pred_train)
print("cls_report_tr\n",cls_report_tr)

"""### Membuat plot confusion matrix"""

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8,8))
sns.heatmap(cm, annot=True, fmt=".0f",linewidth=.5, square=True);
plt.xlabel('Actual Label');
plt.ylabel('Predicted Label');

"""### Report klasifikasi matrix"""

score = metrics.accuracy_score(y_test,y_pred)
print("Accuracy:", score)

print("Report:",metrics.classification_report(y_test,y_pred))

"""### Mengetahui MAE, MSE, RMSE"""

MSE = mse(y_test, y_pred)
MAE = mae(y_test, y_pred)
print("MSE:",MSE)
print("RMSE:",np.sqrt(MSE))
print("MAE:",MAE)

"""### Mengembalikan dalam bentuk dataframe"""

x_train = pd.DataFrame(data=x_train, columns=['Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
       'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember',
       'EstimatedSalary'])
x_test = pd.DataFrame(data=x_test, columns=['Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
       'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember',
       'EstimatedSalary'])

"""### Implementasi cross validation"""

x_train["AV_label"] = 0
x_test["AV_label"]  = 1

# make one big dataset
all_data = pd.concat([x_train, x_test], axis=0, ignore_index=True)

# shuffle
all_data_shuffled = all_data.sample(frac=1)

# define our features and target variable
X = all_data_shuffled.drop(['AV_label'], axis=1)
y = all_data_shuffled['AV_label']
# create our RandomForestClassifier object
rfc = RandomForestClassifier(n_estimators=200, max_depth=5)

# perform cross validation with RandomForest
cross_val_results = cross_val_score(rfc, X, y, cv=5, scoring='accuracy')

# print out the final result
print(cross_val_results.mean())

"""### Membuat Plot Importance"""

# Instantiate a random forest classifier object
rfc = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=2)

# Fit the classifier to the data
rfc.fit(X, y)

# Get the feature importances
importances = rfc.feature_importances_

# Sort the features by importance in descending order
indices = np.argsort(importances)[::-1]

# Plot the feature importances
plt.figure(figsize=(12, 6))
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
plt.show()

