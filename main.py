import time
import cv2

from screen_utils.win32_screen import Win32Screen
from screen_utils.pil_screen import PilScreen
from screen_utils.mss_screen import MssScreen
from screen_utils.dxcam_screen import DxcamScreen
from screen_utils.pyautogui_screen import PyautoguiScreen
from screen_utils.adb_bluestacks_screen import AdbBlueStacksScreen


def run_screen_taker(screen):
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        screenshot = screen.take_screenshot()
        fps += 1

        cv_wait_time = 1
        cv2.imshow(str(screen), cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(cv_wait_time) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    print(f"{screen} - {fps} FPS with region {getattr(screen, 'region', '[region unset]')}")
    return fps


if __name__ == "__main__":
    cropped_screen, full_screen = {}, {}

    screen_methods = [
        Win32Screen(window_name="wnd", region=(0, 40, 800, 640)),
        PilScreen(region=(0, 40, 800, 640)),
        MssScreen(region=(0, 40, 800, 640)),
        DxcamScreen(region=(0, 40, 800, 640)),
        PyautoguiScreen(region=(0, 40, 800, 640)),
        AdbBlueStacksScreen()
    ]

    for screen_method in screen_methods:
        cropped_screen[str(screen_method)] = run_screen_taker(screen_method)

        screen_method.__setattr__("region", None)

        full_screen[str(screen_method)] = run_screen_taker(screen_method)

    print(cropped_screen)
    print(full_screen)
