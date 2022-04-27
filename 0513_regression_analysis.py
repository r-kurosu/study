import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline



def main():
    df = pd.read_csv("winequality-red.csv", sep=";")
    df.head()
    # print(df.head())

    X = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
            "total sulfur dioxide", "density", "pH", "sulphates", "sulphates", "alcohol"]]
    Y = df[["quality"]]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

    # 標準化(分散)
    # -numpy-
    # X_train_np = X_train.apply(lambda x: (x - np.mean(x)) / np.std(x))
    # X_test_np = X_test.apply(lambda x: (x - np.mean(x)) / np.std(x))
    # Y_train_np = Y_train.apply(lambda x: (x - np.mean(x)) / np.std(x))
    # Y_test_np = Y_test.apply(lambda x: (x - np.mean(x)) / np.std(x))

    # print(x_np.head())
    # print(y_np.head())
    # print(x_np.std(ddof=0))

    # -sklearn-
    # sscaler = preprocessing.StandardScaler()
    # sscaler.fit(X)
    # xss_sk = sscaler.transform(X)
    # sscaler.fit(Y)
    # yss_sk = sscaler.transform(Y)


    # 実行
    # -標準化なし-
    model = LinearRegression()
    model.fit(X_train, Y_train)

    # 結果
    print("b: ", model.intercept_)
    print("coef: ", model.coef_)
    print(f'train_score: {model.score(X_train, Y_train)}')
    print(f'test_score: {model.score(X_test, Y_test)}')

    # -標準化あり-
    # model_std = LinearRegression()
    # model_std.fit(X_train_np, Y_train_np)
    #
    # print(model_std.coef_)
    # print(model_std.intercept_)
    # print(f'train_score: {model_std.score(X_train_np, Y_train_np)}')
    # print(f'test_score: {model_std.score(X_test_np, Y_test_np)}')


if __name__ == "__main__":
    main()
