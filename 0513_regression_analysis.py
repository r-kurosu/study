import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

sns.set()  # seabornのスタイルをセット


def polynomial_regression(X_train, Y_train, X_test, Y_test, X, Y):
    # 多項式を基底関数として重回帰
    for deg in range(1, 7):
        model_poly = Pipeline([
            ('poly', PolynomialFeatures(degree=deg)),
            ('linear', LinearRegression())
        ])
        model_poly.fit(X_train, Y_train)
        print(f"=====model poly {deg}=====")
        print(f'train_score: {model_poly.score(X_train, Y_train)}')
        print(f'test_score: {model_poly.score(X_test, Y_test)}')

        # calculate_coer(X.T, Y)

    return 0


# 多項式基底関数を作成
def phi_polynomial(x, j):

    return x**j


# 多項式基底関数の計画行列を作成:(M > 2)
def Phi_polynomial(x_n, M, _x_n=None):
    # 変数を初期化
    phi_x_nm = np.ones((len(x_n), M))

    # 列ごとに多項式基底関数による変換
    for m in range(1, M):
        phi_x_nm[:, m] = phi_polynomial(x_n, m)
    return phi_x_nm


def linear_regression_gousian():
    # 基底関数としてガウスを適用

    return


def lasso_regression(X_train, Y_train, X_test, Y_test):
    hyper_parameter_list = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
    for parm in hyper_parameter_list:
        print("----------------------------")
        print(f"parm = {parm}")
        lasso_model = Lasso(alpha=parm, max_iter=10000).fit(X_train, Y_train)
        print(f'train score : {lasso_model.score(X_train, Y_train)}')
        print(f'test score : {lasso_model.score(X_test, Y_test)}')

    return


def calculate_coer(X, Y):
    # 相関係数を計算
    corr = np.corrcoef(X.T, Y)
    print(corr)

    # 相関係数をヒートマップ化
    sns.heatmap(corr, annot=True)
    plt.show()


def main():
    df = pd.read_csv("winequality-red.csv", sep=";")
    df.head()
    # print(df.head())

    X = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "sulphates", "alcohol"]]
    # X = df[["volatile acidity", "density"]]
    Y = df[["quality"]]
    # Y = df[["alcohol"]]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

    # 実行
    polynomial_regression(X_train, Y_train, X_test, Y_test, X, Y)
    # lasso_regression(X_train, Y_train, X_test, Y_test)


if __name__ == "__main__":
    main()
