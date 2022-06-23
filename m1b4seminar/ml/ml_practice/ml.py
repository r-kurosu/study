#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from statistics import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import Lasso
import sys, time
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import statistics
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest, f_regression, f_classif, SelectPercentile


Times = 1
SEED = 0 #予備実験:0, 評価実験:1000
Fold = 5
ZERO_TOL = 0.000001

Deg = 2 # hyper
print(f"deg={Deg}")
################################################
def read_dataset(data_csv, value_txt):
    
    ### read files ###
    # read the csv and the observed values
    fv = pd.read_csv(data_csv) 
    value = pd.read_csv(value_txt)      

    ### prepare data set ###
    # prepare CIDs
    CIDs = np.array(fv['CID'])
    # prepare target, train, test arrays
    target = np.array(value['a'])
    # construct dictionary: CID to feature vector
    fv_dict = {}
    for cid,row in zip(CIDs, fv.values[:,1:]):
        fv_dict[cid] = row
    # construct dictionary: CID to target value
    target_dict = {}
    for cid, val in zip(np.array(value['CID']), np.array(value['a'])):
        target_dict[cid] = val
    # check CIDs: target_values_filename should contain all CIDs that appear in descriptors_filename
    for cid in CIDs:
        if cid not in target_dict:
            sys.stderr.write('error: {} misses the target value of CID {}\n'.format(target_values_filename, cid))
            exit(1)
    # construct x and y so that the CIDs are ordered in ascending order
    CIDs.sort()
    x = np.array([fv_dict[cid] for cid in CIDs])
    y = np.array([target_dict[cid] for cid in CIDs])
    return (CIDs,x,y)


def select_vectors(x_train, y_train, x_test, K):
    # selector = SelectKBest(score_func=f_classif, k=10)
    selector = SelectPercentile(score_func=f_regression, percentile=70)
    selector.fit(x_train, y_train)
    mask = selector.get_support()

    index_list = []
    for i in range(K):
        if mask[i] == False:
            index_list.append(i)
            # x_train_new = np.delete(x_train, i, 1)
            # x_test_new = np.delete(x_test, i, 1)

    x_train_new = np.delete(x_train, index_list, 1)
    x_test_new = np.delete(x_test, index_list, 1)


    return x_train_new, x_test_new

################################################
def learn_Lasso(x_train, y_train, x_test, y_test, a=1.0):
    lasso = Lasso(alpha=a, max_iter=10**5)
    lasso.fit(x_train, y_train)
    r2train = lasso.score(x_train,y_train)
    r2test = lasso.score(x_test,y_test)
    nonzero = len([w for w in lasso.coef_ if abs(w)>=ZERO_TOL])

    return (lasso, nonzero, r2train, r2test)

################################################

def learn_poly(x_train, y_train, x_test, y_test):
    poly = PolynomialFeatures(degree=Deg, interaction_only=False, include_bias=True)
    # n, K = x_train.shape
    # x_train, x_test = select_vectors(x_train, y_train, x_test, K)

    x_train_poly = poly.fit_transform(x_train)
    x_test_poly = poly.fit_transform(x_test)

    n, K = x_train_poly.shape
    x_train_poly, x_test_poly = select_vectors(x_train_poly, y_train, x_test_poly, K)

    if Deg == 1:
        x_train_poly = x_train
        x_test_poly = x_test
    
    linear = LinearRegression()
    linear.fit(x_train_poly, y_train)

    
    r2train = linear.score(x_train_poly, y_train)
    r2test = linear.score(x_test_poly, y_test)
    
    return r2train, r2test


def polynomial_regression(X_train, Y_train, X_test, Y_test):
    model_poly = Pipeline([
        ('poly', PolynomialFeatures(degree=Deg)),
        ('linear', LinearRegression())
    ])
    model_poly.fit(X_train, Y_train)
    
    train_score = model_poly.score(X_train, Y_train)
    test_score = model_poly.score(X_test, Y_test)
    print(f'train_score: {model_poly.score(X_train, Y_train)}')
    print(f'test_score: {model_poly.score(X_test, Y_test)}')



    return train_score, test_score


try:
    CIDs, x, y = read_dataset(sys.argv[1], sys.argv[2])
    # lmd = float(sys.argv[3])
except:
    sys.stderr.write("usage: {} (input_data.csv)(input_values.txt)(lambda)\n\n".format(sys.argv[0]))
    exit(1)

### experiment ###

# print("Lambda\t{}".format(lmd))
f = open(sys.argv[1])
arr = f.readline().split(',')
print("NumDesc\t{}".format(len(arr)-1))
f.close()

R2_Tr_scores = []
R2_Ts_scores = []
for split_seed in range(1, Times+1):
    kf = KFold(n_splits=Fold, shuffle=True, random_state=split_seed+SEED)

    fold = 0
    Tim = []
    NonZ = []
    for train, test in kf.split(x):
        fold += 1
        start_time = time.time()
        # _, nonzero, r2train, r2test = learn_Lasso(x[train], y[train], x[test], y[test], a=lmd)
        r2train, r2test = learn_poly(x[train], y[train], x[test], y[test])
        # r2train, r2test = polynomial_regression(x[train], y[train], x[test], y[test])
        # lasso, nonzero, r2train, r2test = learn_Lasso(x[train], y[train], x[test], y[test], 2)
        # print(nonzero)

        comp_time = time.time() - start_time
        R2_Tr_scores.append(r2train)
        R2_Ts_scores.append(r2test)
        Tim.append(comp_time)
        # print(f"train score = {r2train}")
        # print(f"test score = {r2test}")

    # print("{}\tTrain".format(split_seed), end="")
    # for v in Tr:
    #     print("\t{:.6f}".format(v), end="")
    # print()
    # print(" \tTest", end="")
    # for v in Ts:
    #     print("\t{:.6f}".format(v), end="")
    # print()
    # print(" \tTime", end="")
    # for v in Tim:
    #     print("\t{:.6f}".format(v), end="")
    # print()
    # print(" \tNonzero", end="")
    # for v in NonZ:
    #     print("\t{}".format(v), end="")
    # print()
    
median_Tr_score = statistics.median(R2_Tr_scores)
median_Ts_score = statistics.median(R2_Ts_scores)

print(f"train score (median) = {median_Tr_score}")
print(f"test score (median) = {median_Ts_score}")