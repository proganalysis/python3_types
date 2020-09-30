# (generated with --quick)

from typing import Any, Tuple

F: Any
nn: Any
torch: Any

def train_cl_clf(device, category_clf_net, site_clf_net, type_clf_net, data_loader, max_num_batches, optimizer) -> None: ...
def valid_cl_clf(device, category_clf_net, site_clf_net, type_clf_net, data_loader) -> Tuple[Any, Any, Any]: ...
