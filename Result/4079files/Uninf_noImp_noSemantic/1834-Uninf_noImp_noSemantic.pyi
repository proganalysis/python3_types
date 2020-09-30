from typing import Any

class PWEDistanceCalculation:
    @staticmethod
    def sym_diff_dist(pw_id_1: Any, pw_id_2: Any, relations: Any, dfs: Any, pws: Any, rls_to_use: list=...) -> Any: ...
    @staticmethod
    def euler_overlap_diff_dist(pw_id_1: Any, pw_id_2: Any, rl_name: Any, col_name: Any, dfs: Any, pws: Any): ...
