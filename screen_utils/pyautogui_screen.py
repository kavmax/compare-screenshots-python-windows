import numpy as np
import pyautogui


class PyautoguiScreen:
    def __init__(self, region=None):
        self.region = region

    def take_screenshot(self):
        if self.region is not None:
            return np.asarray(pyautogui.screenshot(region=self.region))
        else:
            return np.asarray(pyautogui.screenshot())

    def __str__(self):
        return "PyautoguiScreen"
