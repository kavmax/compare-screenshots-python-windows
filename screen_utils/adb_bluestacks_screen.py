import subprocess
import numpy as np
from PIL import Image


class AdbBlueStacksScreen:
    def __init__(self):
        # Physical size: 720x1280 -> self.width = 720, self.height = 1280
        window_size = subprocess.check_output(['adb', 'shell', 'wm', 'size'])
        window_size = window_size.decode('ascii').replace('Physical size: ', '')
        self.screen_width, self.screen_height = [int(i) for i in window_size.split('x')]

    def take_screenshot(self):
        """
        Take a screenshot of the emulator
        """
        screenshot_bytes = subprocess.run(['adb', 'exec-out', 'screencap'], check=True, capture_output=True).stdout
        screenshot = Image.frombuffer(
            'RGBA', (self.screen_width, self.screen_height), screenshot_bytes[12:], 'raw', 'RGBX', 0, 1)
        screenshot = screenshot.convert('RGB').resize((self.screen_width, self.screen_height), Image.BILINEAR)
        return np.array(screenshot)

    def __str__(self):
        return "AdbBlueStacksScreen"
