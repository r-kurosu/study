import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D


def main():
    df = pd.read_csv("winequality-red.csv", sep=";")
    df.head()
    print(df.head())

    X = df[["density", "volatile acidity"]]
    X1 = df[["density"]]
    X2 = df[["volatile acidity"]]
    Y = df[["alcohol"]]

    # fig = plt.figure()
    # ax = Axes3D(fig)
    #
    # ax.scatter3D(X1, X2, Y)
    # ax.set_xlabel("X1")
    # ax.set_ylabel("X2")
    # ax.set_zlabel("Y")
    #
    # plt.show()


    # データの分割(訓練データとテストデータ)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    # モデル構築　
    model = LinearRegression()
    # 学習
    model.fit(X_train, Y_train)

    # 結果
    print("【切片】:", model.intercept_)
    print("【決定係数(訓練)】:", model.score(X_train, Y_train))
    print("【決定係数(テスト)】:", model.score(X_test, Y_test))

    print(model.coef_)
    print(f'train_score: {model.score(X_train, Y_train)}')
    print(f'test_score: {model.score(X_test, Y_test)}')


if __name__ == "__main__":
    main()