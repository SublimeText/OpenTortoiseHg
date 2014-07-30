from unittest.mock import patch
import Default.exec


# Planet of the Monkey-Patch Apes.
class ExecExCommand(Default.exec.ExecCommand):
    _real_window_run_command = None

    def _window_run_command(self, cmd, *args, **kwargs):
        if self.suppress_output_panel and cmd == "show_panel":
            return
        else:
            self._real_window_run_command(cmd, *args, **kwargs)

    def run(self, suppress_output_panel=False, **kwargs):
        self.suppress_output_panel = suppress_output_panel
        self._real_window_run_command = self.window.run_command
        with patch.dict(self.window.__dict__,
                        run_command=self._window_run_command):
            return super().run(**kwargs)
