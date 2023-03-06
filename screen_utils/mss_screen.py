import numpy as np
import mss


class MssScreen:
    def __init__(self, region=None):
        self.sct = mss.mss()
        self.region = region

    def take_screenshot(self):
        if self.region is not None:
            return np.asarray(self.sct.grab(self.region))
        else:
            return np.asarray(self.sct.grab(self.sct.monitors[0]))

    def __str__(self):
        return "MssScreen"
