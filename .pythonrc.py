from pythonrc_manager import (
    DisplayHookPatcher,
    init_rc_script,
    project_rc_path,
)

_displayhook = DisplayHookPatcher.pprinting()
_displayhook.start()

init_rc_script(project_rc_path(), globals())
