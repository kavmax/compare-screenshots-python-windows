import numpy as np
from PIL import ImageGrab


class PilScreen:
    def __init__(self, region=None):
        self.region = region

    def take_screenshot(self):
        if self.region is not None:
            return np.asarray(ImageGrab.grab(bbox=self.region))
        else:
            return np.asarray(ImageGrab.grab())

    def __str__(self):
        return "PilScreen"
