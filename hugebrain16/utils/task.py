import threading
import warnings


class Task:
    def __init__(self, function, interval, count=0):
        self._task = None
        self.function = function
        self.interval = interval / 1000
        self.count = count
        self._count = count
        self.is_running = False

    def _run(self):
        if self.count > 0:
            self.is_running = False
            self.start()
            self.count -= 1
            self.function(*self.args, **self.kwargs)

    def _inf_run(self):
        if self.count == 0:
            self.is_running = False
            self.start()
            self.function()

    def start(self):
        if self.is_running is not True:
            if self.count > 0:
                self._task = threading.Timer(self.interval, self._run)
                self._task.start()
            elif self.count == 0:
                self._task = threading.Timer(self.interval, self._inf_run)
                self._task.start()
            self.is_running = True
        else:
            warnings.warn(f"task for function `{self.function}` is currently running")

    def stop(self):
        if self.is_running is False:
            warnings.warn(
                f"task for function `{self.function.__name__}` is not running"
            )
        else:
            self._task.cancel()
            self.count = self._count
            self.is_running = False
