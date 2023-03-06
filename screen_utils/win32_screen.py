import numpy as np
import win32gui
import win32ui
import win32con
import win32api
from PIL import Image


class Win32Screen:
    def __init__(self, window_name, region=None):
        self.window_handler = win32gui.FindWindow(None, window_name)
        self.region = region

    # https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows
    def take_screenshot(self):
        if self.region is None:
            x, y, w, h = 0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
        else:
            x, y, w, h = self.region

        wDC = win32gui.GetWindowDC(self.window_handler)

        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dcObj, (x, y), win32con.SRCCOPY)

        # save to file
        # dataBitMap.SaveBitmapFile(cDC, 'screenshot.png')
        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)
        image = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.window_handler, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return np.array(image)

    def __str__(self):
        return "Win32Screen"
