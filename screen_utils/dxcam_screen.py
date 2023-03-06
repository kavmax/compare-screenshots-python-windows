import dxcam


class DxcamScreen:
    def __init__(self, region):
        self.camera = dxcam.create()
        self.region = region

    def take_screenshot(self):
        screen = None

        while screen is None:
            if self.region is not None:
                screen = self.camera.grab(region=self.region)
            else:
                screen = self.camera.grab()

        return screen

    def __str__(self):
        return "DxcamScreen"
