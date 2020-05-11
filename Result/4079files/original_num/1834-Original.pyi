# (generated with --quick)

from typing import Any, Optional, Union

PWEQuery: Any

class PWEDistanceCalculation:
    @staticmethod
    def euler_overlap_diff_dist(pw_id_1, pw_id_2, rl_name, col_name, dfs, pws) -> Any: ...
    @staticmethod
    def sym_diff_dist(pw_id_1, pw_id_2, relations, dfs, pws, rls_to_use: Optional[list] = ...) -> Union[float, int]: ...
