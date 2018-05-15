import time


class Timer(object):
    """A simple timer."""
    def __init__(self, name):
        self.name = name
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.

    def tic(self):
        # using time.time instead of time.clock because time time.clock
        # does not normalize for multithreading
        self.start_time = time.time()

    def toc(self, average=True):
        if self.start_time == 0.:
            raise NameError('There is no tic time.')
        self.diff = time.time() - self.start_time
        self.total_time += self.diff
        self.calls += 1
        self.average_time = self.total_time / self.calls
        if average:
            return self.name, self.average_time
        else:
            return self.name, self.diff

    def clear(self):
        self.total_time = 0.
        self.calls = 0
        self.start_time = 0.
        self.diff = 0.
        self.average_time = 0.


class MultiTimer(object):
    def __init__(self):
        self.timer = dict()

    def __getitem__(self, key):
        if key not in self.timer.keys():
            self.timer[key] = Timer(key)

        return self.timer[key]

    def isStart(self, key):
        if key not in self.timer.keys():
            return False
        else:
            return True

    def reset(self, key):
        if key in self.timer.keys():
            self.timer[key].clear()
