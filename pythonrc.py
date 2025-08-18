import importlib.util as _importlib_util
import os as _os
import sys

_displayhook = sys.displayhook

def pdir(o) -> list[str]:
    return [o for o in dir(o) if not o.startswith("_")]


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
    from pythonrc_manager import restart

    _displayhook = _DisplayHookPatcher.pprinting()
    _displayhook.start()

    if __name__ == "__main__":
        _rc_path = _project_rc_path()
        if _os.path.exists(_rc_path):
            _init_rc_script(_rc_path, globals())
