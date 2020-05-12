import pytest
from .utils import digit_float
import numpy as np


vowel_data_y_dimension = 11


@pytest.fixture
def vowel_data():
    from esl_model.datasets import VowelDataSet
    data = VowelDataSet()
    return data.return_all()


@pytest.fixture
def SAHeart_data():
    from esl_model.datasets import SAHeartDataSet
    data = SAHeartDataSet()
    return data.return_all()


def test_vowel_data():
    from esl_model.datasets import VowelDataSet
    data = VowelDataSet()
    assert list(data.train_y[:5]) == list(range(1, 6))

    data.select_features = data.feature_names[:2]
    assert np.array_equal(data.train_x[:1], data._train_x.iloc[:1, :2].values)

    ft = list(range(3))
    data.select_features = ft
    assert np.array_equal(data.train_x[:1], data._train_x.iloc[:1, ft].values)


def test_indicator_matrix(vowel_data):
    from esl_model.ch4.models import LinearRegressionIndicatorMatrix

    train_x, train_y, test_x, test_y, features = vowel_data

    lrm = LinearRegressionIndicatorMatrix(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension)
    lrm.pre_processing()
    lrm.train()
    print(lrm.error_rate)
    test_result = lrm.test(test_x, test_y)
    print(test_result.error_rate)

    assert digit_float(lrm.error_rate) == 0.477
    assert digit_float(test_result.error_rate) == 0.667


def test_LDA(vowel_data):
    from esl_model.ch4.models import LDAModel
    train_x, train_y, test_x, test_y, features = vowel_data

    lda = LDAModel(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension)
    lda.pre_processing()
    lda.train()

    print(lda.y_hat[:10])
    print(lda.error_rate)

    te = lda.test(test_x, test_y)
    print(te.error_rate)

    assert digit_float(lda.error_rate) == 0.316
    assert digit_float(te.error_rate) == 0.556


def test_QDA(vowel_data):
    from esl_model.ch4.models import QDAModel
    train_x, train_y, test_x, test_y, features = vowel_data

    qda = QDAModel(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension)
    qda.pre_processing()
    qda.train()

    print(qda.y_hat[:10])
    print(qda.error_rate)
    te = qda.test(test_x, test_y).error_rate
    print(te)
    assert digit_float(qda.error_rate) == 0.011
    assert digit_float(te) == 0.528


def test_RDA(vowel_data):
    from esl_model.ch4.models import RDAModel
    train_x, train_y, test_x, test_y, features = vowel_data

    # http://waxworksmath.com/Authors/G_M/Hastie/WriteUp/weatherwax_epstein_hastie_solutions_manual.pdf
    # pp 60
    model = RDAModel(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension, alpha=0.969697)
    model.pre_processing()
    model.train()

    print(model.error_rate)
    te = model.test(test_x, test_y)
    print(te.error_rate)
    assert digit_float(te.error_rate) == 0.478


def test_LDA_computation(vowel_data):
    from esl_model.ch4.models import LDAForComputation
    train_x, train_y, test_x, test_y, features = vowel_data

    model = LDAForComputation(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension)
    model.pre_processing()
    model.train()

    from esl_model.ch4.models import LDAModel
    lda = LDAModel(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension)
    lda.pre_processing()
    lda.train()
    print(model.error_rate)

    assert np.isclose(model.error_rate, lda.error_rate)
    assert np.isclose(model.test(test_x, test_y).error_rate, lda.test(test_x, test_y).error_rate)


def test_RRLDA(vowel_data):
    from esl_model.ch4.models import ReducedRankLDAModel
    train_x, train_y, test_x, test_y, features = vowel_data

    model = ReducedRankLDAModel(train_x=train_x, train_y=train_y, n_class=vowel_data_y_dimension, L=2)
    model.pre_processing()
    model.train()

    print(model.y_hat[:5])
    print(model.error_rate)

    te = model.test(test_x, test_y)
    print(te.error_rate)

    assert digit_float(model.error_rate) == 0.350
    assert digit_float(te.error_rate) == 0.491


def test_SAHeart_data_set(SAHeart_data):
    x, y, *_ = SAHeart_data
    assert x[1, 2] == 4.41
    assert list(y[:4]) == [1, 1, 0, 1]


def test_binary_logistic_regression(SAHeart_data):
    from esl_model.datasets import SAHeartDataSet
    data = SAHeartDataSet(select_features=[1, 2, 4, 8])
    from esl_model.ch4.models import BinaryLogisticRegression
    train_x = data.train_x
    train_y = data.train_y

    model = BinaryLogisticRegression(train_x=train_x, train_y=train_y, n_class=2, do_standardization=False)
    model.pre_processing()
    model.train()
    print(model.beta_hat)
    print(model.error_rate)
    print('yhat', model.y_hat[:5])
    print(repr(model.std_err))
    print('z score', model.z_score)

    eq_beta_hat = np.array([[-4.20427542],
                        [0.08070059],
                        [0.16758415],
                        [0.92411669],
                        [0.04404247]])

    eq_std_err = np.array([0.498348, 0.02551477, 0.05418979, 0.22318295, 0.00974321])


    assert np.allclose(model.beta_hat, eq_beta_hat)
    assert digit_float(model.error_rate) == 0.268
    assert np.allclose(model.std_err, eq_std_err)

    data = SAHeartDataSet(select_features=[0, 1, 2, 4, 6, 7, 8])
    train_x = data.train_x
    train_y = data.train_y
    model = BinaryLogisticRegression(train_x=train_x, train_y=train_y, n_class=2, do_standardization=False)
    model.pre_processing()
    model.train()

    assert digit_float(model.error_rate) == 0.271
