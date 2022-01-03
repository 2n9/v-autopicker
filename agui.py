import pyautogui
import time


try:
    for _ in range(100):
        mouse = (292, 432)
        pyautogui.moveTo(mouse)
        pyautogui.click()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("stop")