# Importing all the required libraries
import pandas as pd
import sys
sys.path.append('c:/users/rampu/miniconda3/lib/site-packages')
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.pyplot import figure

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics
 
import warnings
warnings.filterwarnings('ignore')


# Reading the data from the csv file and storing it inside a pandas dataframe

company_name="ADANIPORTS"


stuff_in_string = "D:\COLLEGE\ds203\ds203 project\{}.csv".format(company_name)

df = pd.read_csv(stuff_in_string)
def f1(company__name):
    global company_name
    company_name=company__name

    # Analysing the number of rows and the number of columns in the dataframe
    size = df.shape
    print("COMPANY NAME IS ",company_name)
    print("Number of Rows Present : " , size[0])
    print("Number of Columns Present :" , size[1])

def f2():
    print("COMPANY NAME IS ",company_name)
    f = df.plot(x='Date', y='Prev Close')
    plt.rcParams["figure.figsize"] = (30,7)
    plt.show()

def f3():
    plt.figure(figsize=(7,5))
    sns.heatmap(df.corr(),cmap='Blues',annot=True)
    plt.show()

def f4():
    df['Daily Returns'] = (df['Prev Close']/df['Open']) -1
    df.head()

def f5():
    mean = df['Daily Returns'].mean()
    std = df['Daily Returns'].std()
    print('Mean =',mean)
    print('Standard Deviation =',std)


    print("Kurtosis Variability - ", df['Daily Returns'].kurtosis())


    df['Daily Returns'].hist(bins=20)
    plt.rcParams["figure.figsize"] = (20,5)
    plt.axvline(mean,color='red',linestyle='dashed',linewidth=4)
    plt.axvline(std,color='g',linestyle='dashed',linewidth=4)
    plt.axvline(-std,color='g',linestyle='dashed',linewidth=4)
    
def f8():
    df.isnull().sum()

def f9():
    features = ['Open', 'High', 'Low', 'Close', 'Volume']
 
    plt.subplots(figsize=(20,10))
    
    for i, col in enumerate(features):
        plt.subplot(2,3,i+1)
        sns.distplot(df[col])
    plt.show()

def f10():
    features = ['Open', 'High', 'Low', 'Close', 'Volume']
    
    plt.subplots(figsize=(20,10))
    for i, col in enumerate(features):
        plt.subplot(2,3,i+1)
        sns.boxplot(df[col])
    plt.show()

def f11():
    splitted = df['Date'].str.split('-', expand=True)
 
    df['day'] = splitted[2].astype('int')
    df['month'] = splitted[1].astype('int')
    df['year'] = splitted[0].astype('int')

def f12():
    df['is_quarter_end'] = np.where(df['month']%3==0,1,0)
    df.head()

def f13():
    data_grouped = df.groupby('year').mean()
    plt.subplots(figsize=(20,10))
    
    for i, col in enumerate(['Open', 'High', 'Low', 'Close']):
        plt.subplot(2,2,i+1)
        data_grouped[col].plot.bar()
    plt.show()

def f14():
    df.groupby('is_quarter_end').mean()


    df['open-close']  = df['Open'] - df['Close']
    df['low-high']  = df['Low'] - df['High']
    df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)


    features = df[['open-close', 'low-high', 'is_quarter_end']]
    target = df['target']
    
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    
    X_train, X_valid, Y_train, Y_valid = train_test_split(
        features, target, test_size=0.1, random_state=2022)
    print(X_train.shape, X_valid.shape)


    models = [LogisticRegression(), SVC(
    kernel='poly', probability=True), XGBClassifier()]
    
    for i in range(3):
        models[i].fit(X_train, Y_train)
        
        print(f'{models[i]} : ')
        print('Training Accuracy : ', metrics.roc_auc_score(
            Y_train, models[i].predict_proba(X_train)[:,1]))
        print('Validation Accuracy : ', metrics.roc_auc_score(
            Y_valid, models[i].predict_proba(X_valid)[:,1]))
        print()

    metrics.plot_confusion_matrix(models[0], X_valid, Y_valid)
    plt.show()