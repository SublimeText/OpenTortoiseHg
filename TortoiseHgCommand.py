import os
import shutil
import sublime
import sublime_plugin


def thg_binary():
    if sublime.platform() == "windows":
        import winreg
        thg_dir = winreg.QueryValue(winreg.HKEY_LOCAL_MACHINE,
                                    "Software\\TortoiseHg")
        return os.path.join(thg_dir, "thgw.exe")
    else:
        return shutil.which("thg")


class TortoiseHgCommand(sublime_plugin.WindowCommand):
    def run(self, dirs=None, **kwargs):
        cmd_kwargs = {
            "cmd": thg_binary(),
            "suppress_output_panel": True,
            "quiet": True,
            "working_dir": dirs[0] if dirs else "",
        }
        cmd_kwargs.update(kwargs)
        self.window.run_command("exec_ex", cmd_kwargs)

    def is_visible(self, dirs=None):
        return dirs is None or len(dirs) > 0
