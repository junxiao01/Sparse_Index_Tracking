import numpy as np
import pandas as pd

def comp_sharpe_ratio(X, N, rf):

    '''
    params:
        X: np.array, [T, 1]
        N: trading days per year
        rf: risk-free rate

    return:
        sr
    '''

    mean_ = X.mean() * N - rf
    std_ = X.std() * np.sqrt(N)

    return mean_ / std_


def comp_sortion_ratio(X, N, rf):

    mean_ = X.mean() * N - rf
    std_ = X[X<0].std() * np.sqrt(N)

    return mean_ / std_


def comp_MDD(X):

    '''
        params:
            X: return matrix

    '''

    cumret = (X + 1).cumprod()
    highwatermark = np.zeros(cumret.shape)
    drawdown = np.zeros(cumret.shape)
    drawdownduration = np.zeros(cumret.shape)

    for t in np.arange(1, cumret.shape[0]):
        highwatermark[t] = np.maximum(highwatermark[t - 1], cumret[t])
        drawdown[t] = (1 + cumret[t]) / (1 + highwatermark[t]) - 1
        if drawdown[t] == 0:
            drawdownduration[t] = 0
        else:
            drawdownduration[t] = drawdownduration[t-1] + 1
    
    maxDD, i = np.min(drawdown), np.argmin(drawdown)
    maxDDD = np.max(drawdownduration)
    return drawdown, maxDD, maxDDD, i

def comp_calmar_ratio(X):


    mean_ = X.mean() * 255
    drawdown, maxDD, maxDDD, i = comp_MDD(X)

    return mean_ / abs(maxDD)