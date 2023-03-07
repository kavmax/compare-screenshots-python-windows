This repo contains comparing of different Python libs for making screenshots. 

Full screen:
```
{
    'Win32Screen': [12, 13, 12, 12, 12, 13, 13, 13, 13, 12], 
    'PilScreen': [14, 13, 12, 13, 13, 15, 15, 13, 12, 12], 
    'MssScreen': [16, 15, 15, 17, 15, 15, 15, 15, 18, 19], 
    'DxcamScreen': [49, 43, 25, 38, 27, 43, 49, 39, 39, 49], 
    'PyautoguiScreen': [12, 12, 11, 12, 12, 11, 12, 11, 11, 11], 
    'AdbBlueStacksScreen': [3, 2, 5, 5, 5, 4, 3, 5, 6, 5]
}
```

Cropped screen:
```
{
    'Win32Screen': [24, 30, 25, 26, 31, 31, 31, 31, 31, 30], 
    'PilScreen': [15, 19, 20, 18, 17, 16, 16, 16, 17, 16], 
    'MssScreen': [37, 53, 60, 59, 55, 53, 58, 60, 58, 58], 
    'DxcamScreen': [40, 35, 32, 31, 36, 37, 30, 37, 58, 37], 
    'PyautoguiScreen': [15, 17, 16, 16, 16, 15, 16, 16, 16, 16], 
    'AdbBlueStacksScreen': [5, 6, 6, 6, 6, 7, 6, 6, 6, 6]
}
```

Mean for each method:
```
Full screen:
{
    'Win32Screen': 12.5, 
    'PilScreen': 13.2, 
    'MssScreen': 16.0, 
    'DxcamScreen': 40.1, 
    'PyautoguiScreen': 11.5, 
    'AdbBlueStacksScreen': 4.3
}

Cropped screen:
{
    'Win32Screen': 29.0, 
    'PilScreen': 17.0, 
    'MssScreen': 55.1, 
    'DxcamScreen': 37.3, 
    'PyautoguiScreen': 15.9, 
    'AdbBlueStacksScreen': 6.0
}
```

**DXcam** seems to be the fastest but for now I got an issue with reading from ```DXcam``` object from main and additional thread simultaneously.

All packages are available from PIP from PyCharm except DXcam. You can find it [here](https://github.com/ra1nty/DXcam)

Also it is possible to read screen via [adb](https://developer.android.com/studio/command-line/adb) connecting it to BlueStacks for example. 
To use adb you need:
```shell
adb start-server
adb connect 127.0.0.1:port
```

# Hardware
All measurements were performed on mini PC GK3V. 

Processor: Intel(R) Celeron(R) N5105 @ 2.00GHz, 2001 Mhz, 4 Core(s), 4 Logical Processor(s)