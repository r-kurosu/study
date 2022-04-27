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


def polynomial_regression(X_train, Y_train, X_test, Y_test):
    # 実行(polynomial function)
    for deg in range(1, 10):
        model_poly = Pipeline([
            ('poly', PolynomialFeatures(degree=deg)),
            ('linear', LinearRegression())
        ])
        model_poly.fit(X_train, Y_train)
        print(f"=====model poly {deg}=====")
        print(f'train_score: {model_poly.score(X_train, Y_train)}')
        print(f'test_score: {model_poly.score(X_test, Y_test)}')

    return 0


def main():
    df = pd.read_csv("winequality-red.csv", sep=";")
    df.head()
    # print(df.head())

    X = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
            "total sulfur dioxide", "density", "pH", "sulphates", "sulphates", "alcohol"]]
    # X = df[["volatile acidity", "citric acid", "chlorides", "alcohol"]]

    Y = df[["quality"]]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

    polynomial_regression(X_train, Y_train, X_test, Y_test)


if __name__ == "__main__":
    main()
