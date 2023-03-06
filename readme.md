This repo contains comparing of different Python libs for making screenshots. 

Full screen:
```
{
    'PyAutoGUI': [9, 12, 12, 12, 12, 12, 12, 12, 12, 12], 
    'PIL': [6, 12, 12, 12, 12, 12, 12, 12, 12, 12], 
    'MSS': [14, 17, 16, 17, 16, 16, 15, 17, 17, 16], 
    'Win32': [10, 10, 10, 10, 10, 10, 10, 11, 11, 10], 
    'DXcam': [36, 38, 36, 37, 37, 36, 35, 38, 37, 36]
}
```

Cropped screen:
```
{
    'PyAutoGUI': [15, 15, 15, 15, 15, 15, 15, 15, 15, 15], 
    'PIL': [15, 15, 15, 16, 15, 15, 15, 15, 15, 15], 
    'MSS': [39, 42, 37, 37, 41, 41, 39, 40, 38, 36], 
    'Win32': [30, 30, 30, 30, 30, 30, 30, 30, 31, 30], 
    'DXcam': [60, 58, 57, 57, 59, 59, 56, 54, 59, 58]
}
```

Mean for each method:
```
Full screen [11.7, 11.4, 16.1, 10.2, 36.6]
Cropped screen [15.0, 15.1, 39.0, 30.1, 57.7]
```

**DXcam** seems to be the fastest but for now I got an issue with reading from ```DXcam``` object from main and additional thread simultaneously.

All packages are available from PIP from PyCharm except DXcam. You can find it [here](https://github.com/ra1nty/DXcam)

Also it is possible to read screen via [adb](https://developer.android.com/studio/command-line/adb) connecting it to BlueStacks for example. 