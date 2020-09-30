import numpy as np
from .utils import lazy_method
from numpy import linalg
from scipy.linalg import svd
from scipy.sparse import csr_matrix


class MathCollection:
    def __init__(self):
        self.inv = linalg.inv
        self.sum = np.sum
        self.svd = svd
        self.pinv = linalg.pinv

    def __repr__(self):
        return 'Math Collection'


mathcollection = MathCollection()


class Result:
    def __init__(self, y_hat: np.ndarray, y: np.ndarray):
        self.y_hat = y_hat
        self.y = y
        self.prediction_error = np.power(self.y_hat - self.y, 2)
        self.N = y.shape[0]

    @property
    @lazy_method
    def mse(self):
        """
        mean of prediction error
        :return:
        """
        return mathcollection.sum(self.prediction_error) / self.N

    @property
    @lazy_method
    def std_error(self):
        """
        Standard Error of prediction error
        :return:
        """
        return (np.var(self.prediction_error, ddof=1) / self.N)**0.5

    @property
    def error_rate(self):
        return 1 - (np.sum((self.y_hat == self.y)) / self.N)


class BaseStatModel:
    def __init__(self, train_x: np.ndarray, train_y: np.ndarray, features_name=None, do_standardization=True):
        # ensure that train_y is (N x 1)
        train_y = train_y.reshape((train_y.shape[0], 1))
        self.train_x = train_x
        self._raw_train_x = train_x.copy()
        self._raw_train_y = train_y.copy()
        self.train_y = train_y
        self.features_name = features_name

        self.do_standardization = do_standardization
        self._x_std_ = None
        self._x_mean_ = None

    def standardize(self, x, axis=0, with_mean=True, with_std=True):
        if not self.do_standardization:
            return x

        if getattr(self, '_x_std_', None) is None or getattr(self, '_x_mean_', None) is None:
            self._x_mean_ = x.mean(axis=axis)
            self._x_std_ = x.std(axis=axis, ddof=1)
        if with_mean:
            x = x - self._x_mean_
        if with_std:
            x = x / self._x_std_
        return x

    @property
    def N(self):
        """number of N sample"""
        return self._raw_train_x.shape[0]

    @property
    def p(self):
        """
        number of features exclude intercept one
        :return:
        """
        return self._raw_train_x.shape[1]

    def _pre_processing_x(self, X: np.ndarray):
        return X

    def _pre_processing_y(self, y):
        return y

    def pre_processing(self):
        self.train_x = self._pre_processing_x(self.train_x)
        self.train_y = self._pre_processing_y(self.train_y)

    def train(self):
        raise NotImplementedError

    def predict(self, X: np.ndarray):
        raise NotImplementedError

    def test(self, X, y):
        y_hat = self.predict(X)
        y = y.reshape((y.shape[0], 1))
        return Result(y_hat, y)

    @property
    def math(self):
        return mathcollection


class ClassificationMixin(BaseStatModel):
    def __init__(self, *args, n_class=None, **kwargs):
        self.n_class = n_class
        self._label_map = dict()
        super().__init__(*args, **kwargs)

    @lazy_method
    def _get_unique_sorted_label(self):
        y = self._raw_train_y
        unique_label = np.unique(y)
        sorted_label = np.sort(unique_label)
        return sorted_label

    def _pre_processing_y(self, y):
        y = super()._pre_processing_y(y)

        # reference sklearn.preprocessing.label.py
        sorted_label = self._get_unique_sorted_label()
        if self.n_class is None:
            self.n_class = len(sorted_label)

        cols = np.searchsorted(sorted_label, y.flatten())
        rows = np.arange(0, y.shape[0])
        data = np.ones_like(rows)
        matrix = csr_matrix((data, (rows, cols)), shape=(y.shape[0], self.n_class)).toarray()
        return matrix

    def _inverse_matrix_to_class(self, matrix):
        """
        inverse indicator matrix to multi class
        :param matrix:
        :return:
        """
        index = matrix.argmax(axis=1)
        sorted_label = self._get_unique_sorted_label()
        return sorted_label[index].reshape((-1, 1))