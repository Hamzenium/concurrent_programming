import threading
import time

class SleepyWorkers(threading.Thread):
    def __init__(self, seconds, **kwargs):
        super(SleepyWorkers, self).__init__(**kwargs)
        self._seconds = seconds
        self.start()

    def sleep_a_little(self):
        time.sleep(self._seconds)

    def run(self):
        self.sleep_a_little()