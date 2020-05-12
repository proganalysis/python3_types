import numpy as np
from scipy.special import expit
from typing import Any

sigmoid = expit

def generate_orthogonal_matrix(N: Any): ...
def solve_df_lambda(X: np.ndarray, dimension: Any=..., epsilon: Any=..., do_standardization: Any=...) -> list: ...
