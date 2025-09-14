import importlib.util as _importlib_util
import os as _os
import sys

_displayhook = sys.displayhook

def pdir(o) -> list[str]:
    return [o for o in dir(o) if not o.startswith("_")]

def pvars(o) -> dict[str, object]:
    return {k: v for k, v in vars(o).items() if not k.startswith("_")}

if _importlib_util.find_spec("pythonrc_manager"):
    from pythonrc_manager import (
        DisplayHookPatcher as _DisplayHookPatcher,
    )
    from pythonrc_manager import (
        init_rc_script as _init_rc_script,
    )
    from pythonrc_manager import (
        project_rc_path as _project_rc_path,
    )

    try:
        import rich.pretty as rich_pretty
        _pprinter = rich_pretty.pprint
    except ImportError:
        import pprint
        _pprinter = pprint.pprint

    _displayhook = _DisplayHookPatcher(_pprinter)
    _displayhook.start()

    if __name__ == "__main__":
        _rc_path = _project_rc_path()
        if _rc_path and _os.path.exists(_rc_path):
            _init_rc_script(_rc_path, globals())
