import pyautogui

from ui.window import activateWindow

activateWindow()
im1 = pyautogui.screenshot(region=(330, 50, 390, 128))
im1.save('my_screenshot.png')