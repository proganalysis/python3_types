import numpy as np


def var(series, alpha=0.99):
    return VaR(series, alpha).var


def cvar(series, alpha=0.99):
    return VaR(series, alpha).cvar


class VaR(object):
    def __init__(self, series, alpha = 0.99):
        self.__series = series.dropna()
        self.__alpha = alpha

    @property
    def __losses(self):
        return self.__series.pct_change().dropna() * (-1)

    @property
    def __tail(self):
        losses = self.__losses
        return np.sort(losses.values)[int(losses.shape[0] * self.__alpha):]

    @property
    def cvar(self):
        return self.__tail.mean()

    @property
    def var(self):
        return self.__tail[0]