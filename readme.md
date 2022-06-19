This repo contains comparing of different Python libs for making screenshots. 

Full screen:
```
{
    'PyAutoGUI': [9, 12, 12, 12, 12, 12, 12, 12, 12, 12], 
    'PIL': [8, 12, 12, 12, 12, 12, 12, 13, 12, 12], 
    'MSS': [13, 15, 15, 15, 16, 15, 15, 15, 15, 15], 
    'DXcam': [34, 36, 37, 36, 36, 36, 35, 29, 34, 34]
}
```

Cropped screen:
```
{
    'PyAutoGUI': [15, 15, 15, 15, 15, 15, 15, 15, 15, 15], 
    'PIL': [15, 15, 16, 16, 15, 15, 16, 15, 15, 16], 
    'MSS': [32, 35, 34, 35, 34, 35, 35, 34, 36, 36], 
    'DXcam': [58, 60, 58, 56, 59, 58, 59, 60, 59, 60]
}
```

Mean for each method:
```
Full screen [11.7, 11.7, 14.9, 34.7]
Cropped screen [15.0, 15.4, 34.6, 58.7]
```

All packages are available from PIP from PyCharm except DXcam. You can find it [here](https://github.com/ra1nty/DXcam)