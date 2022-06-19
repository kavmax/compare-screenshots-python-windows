import time

import cv2
import mss
import numpy as np
import pyautogui
import dxcam
from PIL import ImageGrab

camera = dxcam.create()
# Time for dxcam after creation an object
time.sleep(0.1)

cv_wait_time = 1


def screen_record_pyautogui(region=None):
    title = "[PyAutoGUI] FPS benchmark"
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        if region is not None:
            img = np.asarray(pyautogui.screenshot(region=region))
        else:
            img = np.asarray(pyautogui.screenshot())

        fps += 1

        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(cv_wait_time) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


def screen_record_pil(region=None):
    title = "[PIL.ImageGrab] FPS benchmark"
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        if region is not None:
            img = np.asarray(ImageGrab.grab(bbox=region))
        else:
            img = np.asarray(ImageGrab.grab())

        fps += 1

        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(cv_wait_time) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


def screen_record_mss(region=None):
    # 800x600 windowed mode
    mon = {"top": 40, "left": 0, "width": 800, "height": 640}

    title = "[MSS] FPS benchmark"
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    def numpy_flip(im):
        """ Most efficient Numpy version as of now. """
        frame = np.array(im, dtype=np.uint8)
        return np.flip(frame[:, :, :3], 2).tobytes()

    while time.time() - last_time < 1:
        if region is not None:
            img = np.asarray(sct.grab(region))
        else:
            img = np.asarray(sct.grab(sct.monitors[0]))

        fps += 1

        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGRA2RGB))
        if cv2.waitKey(cv_wait_time) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


def screen_record_dxcam(region=None):
    title = "[DXcam] FPS benchmark"

    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        img = None
        while img is None:
            if region is not None:
                img = camera.grab(region=(0, 40, 800, 640))
            else:
                img = camera.grab()
        else:
            fps += 1
            cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            if cv2.waitKey(cv_wait_time) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

    return fps


full_screen = {
    "PyAutoGUI": [],
    "PIL": [],
    "MSS": [],
    "DXcam": [],
}

cropped_screen = {
    "PyAutoGUI": [],
    "PIL": [],
    "MSS": [],
    "DXcam": [],
}

for _ in range(10):
    # Full screen
    full_screen["PyAutoGUI"].append(screen_record_pyautogui())
    full_screen["PIL"].append(screen_record_pil())
    full_screen["MSS"].append(screen_record_mss())
    full_screen["DXcam"].append(screen_record_dxcam())

    # Cropped screen
    cropped_screen["PyAutoGUI"].append(screen_record_pyautogui((0, 40, 800, 640)))
    cropped_screen["PIL"].append(screen_record_pil((0, 40, 800, 640)))
    cropped_screen["MSS"].append(screen_record_mss({"top": 40, "left": 0, "width": 800, "height": 640}))
    cropped_screen["DXcam"].append(screen_record_dxcam((0, 40, 800, 640)))

print("Full screen", [np.array(method).mean() for method in full_screen.values()])
print(full_screen)

print("-----")

print("Cropped screen", [np.array(method).mean() for method in cropped_screen.values()])
print(cropped_screen)
