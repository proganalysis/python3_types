# (generated with --quick)

import click.core
from typing import Any, IO, Iterable, Mapping, Optional, Sequence, Union

Amount: Any
Markets: Any
PrettyTable: Any
click: module
conductor: click.core.Group
context_settings: dict
current_signing_key: Any
disable: click.core.Command
disable_witness: Any
enable: click.core.Command
enable_witness: Any
feed: click.core.Command
generate_signing_key: Any
get_config: Any
get_witness: Any
init: click.core.Command
is_witness_enabled: Any
json: module
keygen: click.core.Command
kill_switch: click.core.Command
new_config: Any
run_price_feeds: Any
set_config: Any
silent: Any
spinner: Any
status: click.core.Command
tickers: click.core.Command
total_missed: Any
update: click.core.Command
watchdog: Any
witness_create: Any
witness_set_props: Any

def echo(message: object = ..., file: Optional[IO[str]] = ..., nl: bool = ..., err: bool = ..., color: bool = ...) -> None: ...
def ensure_witness_hook() -> None: ...
def heading(title) -> None: ...
def output(data, title = ...) -> None: ...
def tabulate(tabular_data: Union[Iterable[Iterable], Mapping[str, Iterable]], headers: Union[str, Sequence[str]] = ..., tablefmt: Union[str, tabulate.TableFormat] = ..., floatfmt: Union[str, Iterable[str]] = ..., numalign: Optional[str] = ..., stralign: Optional[str] = ..., missingval: Union[str, Iterable[str]] = ..., showindex: Union[bool, Iterable] = ..., disable_numparse: Union[bool, Iterable[int]] = ..., colalign: Optional[Iterable[Optional[str]]] = ...) -> str: ...
