import os
import sys
from pythonrc_manager import DisplayHookPatcher as _DisplayHookPatcher
from pythonrc_manager import init_rc_script as _init_rc_script
from pythonrc_manager import project_rc_path as _project_rc_path

def pdir(o: object) -> list[str]:
    return [o for o in dir(o) if not o.startswith("_")]

def pvars(o: object) -> dict[str, object]:
    return {k: v for k, v in vars(o).items() if not k.startswith("_")}

try:
    from rich.pretty import pprint as rich_pprint
    do_pprint = rich_pprint
except ImportError:
    from pprint import pprint as pprint_pprint
    do_pprint = pprint_pprint

_dp = _DisplayHookPatcher(do_pprint)  # 🦈
_dp.start()

d = sys.displayhook

if __name__ == "__main__":
    _rc = _project_rc_path()
    if _rc and os.path.exists(_rc):
        _init_rc_script(_rc, globals())
