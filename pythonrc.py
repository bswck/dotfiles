import os
import sys
from collections.abc import Callable
from typing import Any

from pythonrc_manager import DisplayHookPatcher as _DisplayHookPatcher
from pythonrc_manager import init_rc_script as _init_rc_script
from pythonrc_manager import project_rc_path as _project_rc_path


def pdir(o: object) -> list[str]:
    return [o for o in dir(o) if not o.startswith("_")]


def pvars(o: object) -> dict[str, object]:
    return {k: v for k, v in vars(o).items() if not k.startswith("_")}


def report(
    *args: object,
    stack_offset: int = 1,
    print_fn: Callable[..., None] = print,
    add_location: bool = True,
    important: bool = False,
    **kwargs: Any,
) -> None:
    if not int(os.environ.get("PYTHONRC_VERBOSE", "0")) and not important:
        return
    caller = sys._getframe(stack_offset)
    if add_location:
        location = f"{os.path.relpath(caller.f_code.co_filename)}:{caller.f_lineno}"
        args = (f"[{location}]",) + args
    print_fn(*args, **kwargs)


try:
    from rich.pretty import pprint as rich_pprint

    do_pprint = rich_pprint
    report("Using rich for display hook")
except ImportError:
    from pprint import pprint as pprint_pprint

    do_pprint = pprint_pprint
    report("Using pprint as display hook")

_dp = _DisplayHookPatcher(do_pprint)  # 🦈
_dp.start()
report(f"Initialized (using {_dp.printer.__qualname__} displayhook)", important=True)

d = sys.displayhook

if __name__ == "__main__":
    _rc = _project_rc_path()
    if _rc and os.path.exists(_rc):
        _init_rc_script(_rc, globals())
        report(f"Loaded project rc script: {_rc}", important=True)
