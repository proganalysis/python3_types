import numpy as np
from scipy.special import expit


sigmoid = expit


def generate_orthogonal_matrix(N):
    """
    with random permutation of coordinate axes
    :param N: dimension of matrix
    :return: NxN orthogonal matrix contains 0 and 1

    Ref: http://stackoverflow.com/questions/33003341/how-to-randomly-generate-a-nonnegative-orthogonal-matrix-in-numpy
    """
    I = np.eye(N)
    p = np.random.permutation(N)
    return I[p]


def solve_df_lambda(X: np.ndarray, dimension=None, epsilon=1e-3, do_standardization=True) -> list:
    """
    Using Newton Method to solve df(lambda) = k, k in [1..p]
    :param X:
    :return: list of lambda

    ref
    ----
    https://en.wikipedia.org/wiki/Newton%27s_method
    """
    if dimension is None:
        dimension = X.shape[1]

    if do_standardization:
        X  = (X-np.mean(X, axis=0)) / np.std(X, axis=0, ddof=1)

    u, d_, vt = np.linalg.svd(X)
    ds = d_**2

    func_d = lambda lam, k: np.sum(ds/(ds + lam)) - k
    func_d_derivative = lambda lam: -np.sum(ds/(ds + lam)**2)

    # init lambda_p is 0
    lambdas = [0] * (dimension + 1)

    for k in reversed(range(1, dimension)):
        last_lam = lambdas[k+1]
        while True:
            new_lambda = last_lam - func_d(last_lam, k) / func_d_derivative(last_lam)
            if abs((new_lambda - last_lam)/new_lambda) < epsilon:
                lambdas[k] = new_lambda
                break
            last_lam = new_lambda

    lambdas[0] = np.inf
    return lambdas