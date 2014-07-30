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
    def run(self, **kwargs):
        cmd_kwargs = {
            "cmd": thg_binary(),
            "output_panel_force": False,
            "quiet": True,
        }
        cmd_kwargs.update(kwargs)
        self.window.run_command("exec_ex", cmd_kwargs)
