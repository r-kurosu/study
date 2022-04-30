import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

sns.set()  # seabornのスタイルをセット


def linear_regression(X_train, Y_train, X_test, Y_test):
    # 線形回帰
    model_linear = LinearRegression()
    model_linear.fit(X_train, Y_train)

    print(f"---linear regression---")
    print(f'train_score: {model_linear.score(X_train, Y_train)}')
    print(f'test_score: {model_linear.score(X_test, Y_test)}')

    Y_train_pred = model_linear.predict(X_train)
    Y_test_pred = model_linear.predict(X_test)

    plot_func(Y_train, Y_train_pred, Y_test, Y_test_pred)

    print(r2_score(Y_train, Y_train_pred))
    print(r2_score(Y_test, Y_test_pred))


    return


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

        Y_train_pred = model_poly.predict(X_train)
        Y_test_pred = model_poly.predict(X_test)

        plot_func(Y_train, Y_train_pred, Y_test, Y_test_pred)


    return


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

        Y_train_pred = lasso_model.predict(X_train)
        Y_test_pred = lasso_model.predict(X_test)

        # plot_func(Y_train, Y_train_pred, Y_test, Y_test_pred)

    return


def calculate_coer(X, Y):
    df = pd.read_csv("winequality-red.csv", sep=";")
    # 相関係数を計算
    corr = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "sulphates", "alcohol", "quality"]].corr()
    print(corr)

    # 相関係数をヒートマップ化
    sns.heatmap(corr, annot=True)
    # plt.show()
    # plt.savefig("heatmap-figure.png")

    return


def plot_func(Y_train, Y_train_pred, Y_test, Y_test_pred):
    plt.scatter(Y_train,  # グラフのx値(予測値)
                Y_train_pred - Y_train,  # グラフのy値(予測値と学習値の差)
                c='blue',  # プロットの色
                marker='o',  # マーカーの種類
                s=10,  # マーカーサイズ
                alpha=0.7,  # 透明度
                label='train data')  # ラベルの文字

    # 予測値と残差をプロット（テストデータ）
    plt.scatter(Y_test_pred,
                Y_test_pred - Y_test,
                c='red',
                marker='o',
                s=10,
                alpha=0.7,
                label='test data')

    # グラフ書式設定
    y_min = min(Y_train)
    y_max = max(Y_train)

    plt.xlabel('予測値')
    plt.ylabel('残差')
    plt.legend(loc='upper left')
    plt.hlines(y=0, xmin=0, xmax=10, lw=2, color='black')
    # plt.xlim([-20, 60])
    # plt.ylim([y_min, y_max])
    plt.tight_layout()
    plt.show()

    return


def main():
    df = pd.read_csv("winequality-red.csv", sep=";")
    df.head()
    # print(df.head())

    X = df[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "sulphates", "alcohol"]]
    # X = df[["volatile acidity", "density"]]
    Y = df[["quality"]]
    # Y = df[["alcohol"]]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

    # 相関係数を計算
    # calculate_coer(X, Y)

    # 実行
    # linear_regression(X_train, Y_train, X_test, Y_test)
    # polynomial_regression(X_train, Y_train, X_test, Y_test, X, Y)
    lasso_regression(X_train, Y_train, X_test, Y_test)


    return

if __name__ == "__main__":
    main()
