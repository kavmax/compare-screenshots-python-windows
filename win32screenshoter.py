import numpy as np
import win32gui
import win32ui
import win32con
import win32api
from PIL import Image


# https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows
def background_screenshot(hwnd, region=None):
    if region is None:
        x, y, w, h = 0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    else:
        x, y, w, h = region[0], region[1], region[2], region[3]

    wDC = win32gui.GetWindowDC(hwnd)

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
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return np.array(image)
