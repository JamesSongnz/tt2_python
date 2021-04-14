
import pyautogui

from ui.window import activateWindow


def findImage(image, region):
    try:
        center = pyautogui.locateCenterOnScreen(image, region=region, confidence = 0.9)
        return center
    except pyautogui.ImageNotFoundException:
        return False

if __name__ == '__main__':

    activateWindow()

    im1 = pyautogui.screenshot(region=(330, 50, 390, 128))
    im1.save('my_screenshot.png')

    center = findImage('my_screenshot.png', region=(330,100+  50, 390, 100+128))
    if center != None:
        print("found... ")
    else:
        print("Not ")
