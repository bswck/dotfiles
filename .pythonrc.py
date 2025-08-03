import os as _os
from pythonrc_manager import (
    DisplayHookPatcher as _DisplayHookPatcher,
    init_rc_script as _init_rc_script,
    project_rc_path as _project_rc_path,
)

_displayhook = _DisplayHookPatcher.pprinting()
_displayhook.start()

_rc_path = _project_rc_path()
if _os.path.exists(_rc_path):
    _init_rc_script(_rc_path(), globals())
