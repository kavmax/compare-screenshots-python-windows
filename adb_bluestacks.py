import subprocess

import numpy as np
from PIL import Image
import time
import cv2

cv_wait_time = 1


def screen_record_pyautogui(screen):
    title = "[ADB at BlueStacks] FPS benchmark"
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        screen_shot = screen.take_screenshot()
        fps += 1
        cv2.imshow(title, screen_shot)
        if cv2.waitKey(cv_wait_time) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


class Screen:
    def __init__(self, screen_width, screen_height):
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


def main():
    cls = Screen(screen_width=540, screen_height=960)
    print(screen_record_pyautogui(cls))


if __name__ == '__main__':
    main()
